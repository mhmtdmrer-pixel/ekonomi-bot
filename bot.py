import os
import requests
import tweepy

# Veri çekme fonksiyonu
def get_prices():
    url_xau = "https://www.goldapi.io/api/XAU/TRY"
    url_xag = "https://www.goldapi.io/api/XAG/TRY"

    headers = {
        "x-access-token": os.getenv("GOLDAPI_KEY"),
        "Content-Type": "application/json"
    }

    # Altın
    r1 = requests.get(url_xau, headers=headers)
    r1.raise_for_status()
    data_xau = r1.json()

    # Gümüş
    r2 = requests.get(url_xag, headers=headers)
    r2.raise_for_status()
    data_xag = r2.json()

    # Döviz kuru (GoldAPI tüm kurları verir)
    usd_try = data_xau["exchange_rate"]["USD"]
    eur_try = data_xau["exchange_rate"]["EUR"]

    # Altın gram
    gram_altin = data_xau["price_gram_24k"]

    # Gümüş gram
    gram_gumus = data_xag["price_gram_24k"]

    return usd_try, eur_try, gram_altin, gram_gumus


# Tweet gönderme fonksiyonu
def send_tweet(text):
    client = tweepy.Client(
        consumer_key=os.getenv("X_API_KEY"),
        consumer_secret=os.getenv("X_API_SECRET"),
        access_token=os.getenv("X_ACCESS_TOKEN"),
        access_token_secret=os.getenv("X_ACCESS_SECRET")
    )
    client.create_tweet(text=text)


# Ana fonksiyon
def main():
    usd, eur, altin, gumus = get_prices()

    tweet_text = f"""
📊 Günlük Finans Özeti

💵 USD/TRY: {usd}
💶 EUR/TRY: {eur}
🥇 Gram Altın: {altin} TL
🥈 Gram Gümüş: {gumus} TL

#Dolar #Euro #Altın #Gümüş #Finans #Piyasalar
"""

    print("Tweet oluşturuldu:")
    print(tweet_text)

    send_tweet(tweet_text)
    print("Tweet gönderildi!")


if __name__ == "__main__":
    main()
