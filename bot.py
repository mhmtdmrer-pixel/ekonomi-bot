import os
import requests

def get_data():
    url = "https://www.goldapi.io/api/XAU/TRY"
    headers = {
        "x-access-token": os.getenv("GOLDAPI_KEY"),
        "Content-Type": "application/json"
    }
    r = requests.get(url, headers=headers)
    r.raise_for_status()
    return r.json()

def main():
    data = get_data()

    usd_try = data["exchange_rate"]["USD"]
    eur_try = data["exchange_rate"]["EUR"]
    gram_altin = data["price_gram_24k"]

    print("USD/TRY:", usd_try)
    print("EUR/TRY:", eur_try)
    print("Gram Altın (24K):", gram_altin)

if __name__ == "__main__":
    main()
