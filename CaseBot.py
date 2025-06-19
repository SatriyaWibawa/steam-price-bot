import requests
import time
import re

# Konfigurasi
item_name = "Dreams & Nightmares Case"
steam_url = "https://steamcommunity.com/market/priceoverview/"
appid = 730  # CS2
currency_usd = 1
usd_to_idr = 16000  # Ganti sesuai kurs terbaru

# Telegram
bot_token = "8052627436:AAHsHDt3McXFvyPj5FXPbD8FYN8m449B5h8"
chat_id = "6781127136"

def get_price_usd():
    params = {
        "country": "US",
        "currency": 1,
        "appid": 730,
        "market_hash_name": "Dreams & Nightmares Case"
    }
    response = requests.get("https://steamcommunity.com/market/priceoverview/", params=params)
    
    print("Steam API Status:", response.status_code)
    print("Steam API Response:", response.text)

    try:
        data = response.json()
        if "lowest_price" in data:
            price_str = re.sub(r"[^\d.]", "", data["lowest_price"])
            price_float = float(price_str)
            return int(price_float * 16000)  # kurs USD to IDR
        else:
            print("Key 'lowest_price' gak ditemukan.")
            return None
    except Exception as e:
        print("Error parsing JSON:", e)
        return None


def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {"chat_id": chat_id, "text": message}
    response = requests.post(url, data=payload)
    print("Status:", response.status_code)
    print("Response:", response.text)


# Loop update tiap 1 jam
while True:
    price = get_price_usd()
    if price:
        message = f"[Update Harga Steam]\n📦 {item_name}\n💰 Harga Sekarang: Rp{price:,}"
        print("Harga (debug):", price)
        send_telegram_message(message)
        print(f"Sent: {message}")
    else:
        print("Gagal ambil harga.")
    
    time.sleep(3600)  # Tunggu 1 jam (3600 detik)
