import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import sys
import time

BASE_URL = "http://10.13.200.230/.hidden/"
STOP_WORD = "flag"
DELAY = 0.02  # petite pause entre requêtes (secondes), 0 pour désactiver

visited = set()


def make_session():
    """Session avec pool de connexions + retries : réutilise les sockets (keep-alive)."""
    session = requests.Session()
    retries = Retry(total=3, backoff_factor=0.5, status_forcelist=[500, 502, 503, 504])
    adapter = HTTPAdapter(pool_connections=10, pool_maxsize=10, max_retries=retries)
    session.mount("http://", adapter)
    session.mount("https://", adapter)
    return session


def get_links(session, url):
    """Retourne les liens d'une page d'index Apache, filtrés sous BASE_URL."""
    try:
        r = session.get(url, timeout=5)
        if r.status_code != 200:
            return []
        soup = BeautifulSoup(r.text, "html.parser")
        links = []
        for a in soup.find_all("a", href=True):
            href = a["href"]
            if href in ("../", "./", "/"):
                continue
            full = urljoin(url, href)
            if full.startswith(BASE_URL):
                links.append(full)
        return links
    except requests.RequestException as e:
        print(f"\n[ERREUR] {url} → {e}", file=sys.stderr)
        return []


def crawl(session, start_url):
    """Crawl itératif. Retourne (url, contenu) du README contenant STOP_WORD, sinon (None, None)."""
    stack = [start_url]
    count = 0

    while stack:
        url = stack.pop()
        if url in visited:
            continue
        visited.add(url)

        count += 1
        if count % 50 == 0:  # progression discrète, réécrite sur la même ligne
            print(f"\r{count} dossiers explorés, {len(stack)} en attente…",
                  end="", flush=True)

        if DELAY:
            time.sleep(DELAY)

        for link in get_links(session, url):
            if link in visited:
                continue
            if link.endswith("/"):
                stack.append(link)
            elif link.rsplit("/", 1)[-1].upper() == "README":
                try:
                    r = session.get(link, timeout=5)
                    if r.status_code == 200 and STOP_WORD in r.text.lower():
                        return link, r.text.strip()
                except requests.RequestException as e:
                    print(f"\n[ERREUR] {link} → {e}", file=sys.stderr)

    return None, None


def main():
    print(f"Crawl de {BASE_URL} (arrêt sur « {STOP_WORD} »)")
    session = make_session()
    found_url, content = crawl(session, BASE_URL)

    print()  # saut de ligne après la progression
    if found_url:
        print(f"Trouvé dans : {found_url}\n")
        print(content)
    else:
        print(f"Aucun README avec « {STOP_WORD} ». {len(visited)} dossiers explorés.")


if __name__ == "__main__":
    main()