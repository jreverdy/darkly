import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import sys

BASE_URL = "http://10.12.200.60/.hidden/"
OUTPUT_FILE = "results.txt"
visited = set()

def get_links(url):
    """Retourne tous les liens d'une page d'index."""
    try:
        r = requests.get(url, timeout=5)
        if r.status_code != 200:
            return []
        soup = BeautifulSoup(r.text, "html.parser")
        links = []
        for a in soup.find_all("a", href=True):
            href = a["href"]
            # Ignore les liens de navigation parent
            if href in ("../", "./", "/"):
                continue
            links.append(urljoin(url, href))
        return links
    except requests.RequestException as e:
        print(f"[ERREUR] {url} → {e}", file=sys.stderr)
        return []

def crawl(url, output, depth=0):
    """Crawl récursif : explore les dossiers et lit les README."""
    if url in visited:
        return
    visited.add(url)

    print(f"{'  ' * depth}📂 {url}")
    links = get_links(url)

    for link in links:
        if link in visited:
            continue

        if link.endswith("/"):
            # C'est un sous-dossier → on recurse
            crawl(link, output, depth + 1)
        elif link.split("/")[-1].upper() == "README":
            # C'est un fichier README → on le télécharge
            try:
                r = requests.get(link, timeout=5)
                if r.status_code == 200 and r.text.strip():
                    print(f"{'  ' * depth}  ✅ README trouvé : {link}")
                    output.write(f"=== {link} ===\n")
                    output.write(r.text.strip())
                    output.write("\n\n")
            except requests.RequestException as e:
                print(f"[ERREUR] {link} → {e}", file=sys.stderr)

def main():
    print(f"🚀 Démarrage du crawl sur {BASE_URL}")
    print(f"📝 Résultats écrits dans : {OUTPUT_FILE}\n")

    with open(OUTPUT_FILE, "w", encoding="utf-8") as output:
        crawl(BASE_URL, output)

    print(f"\n✅ Terminé ! Consultez {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
