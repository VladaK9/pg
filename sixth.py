import sys
import requests
from bs4 import BeautifulSoup


def download_url_and_get_all_hrefs(url):
    """
    Funkce stahne url predanou v parametru url pomoci volani response = requests.get(),
    zkontroluje navratovy kod response.status_code, ktery musi byt 200,
    pokud ano, najdete ve stazenem obsahu stranky response.content vsechny vyskyty
    <a href="url">odkaz</a> a z nich nactete url, ktere vratite jako seznam pomoci return
    """
    hrefs = []

    # Provedení HTTP GET požadavku
    response = requests.get(url)

    # Kontrola stavového kódu (vyžadován kód 200)
    if response.status_code == 200:
        # Načtení HTML obsahu pomocí BeautifulSoup
        soup = BeautifulSoup(response.content, "html.parser")

        # Vyhledání všech tagů <a> a vytažení atributu 'href'
        for anchor in soup.find_all("a"):
            href = anchor.get("href")
            if href:  # Ošetření případů, kdy <a> nemá atribut href
                hrefs.append(href)
    else:
        raise Exception(f"Stránku se nepodařilo stáhnout. HTTP kód: {response.status_code}")

    return hrefs


if __name__ == "__main__":
    try:
        if len(sys.argv) < 2:
            print("Chyba: Chybí parametr URL.")
            print("Použití: python sixth.py <URL>")
            sys.exit(1)

        url = sys.argv[1]
        links = download_url_and_get_all_hrefs(url)

        print(f"Nalezeno {len(links)} odkazů:")
        print(links)

    # Ošetření potenciálních chyb
    except Exception as e:
        print(f"Program skoncil chybou: {e}")