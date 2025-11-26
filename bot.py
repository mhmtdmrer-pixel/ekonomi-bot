import requests

API_KEY = "YOUR_API_KEY"
URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/USD"

def main():
    response = requests.get(URL)
    data = response.json()

    # Hata kontrolü
    if data.get("result") != "success":
        print("API Hatası:", data)
        return

    rates = data["conversion_rates"]

    usd_try = rates["TRY"]
    eur_try = rates["EUR"]

    print(f"USD/TRY: {usd_try}")
    print(f"EUR/TRY: {eur_try}")

if __name__ == "__main__":
    main()
