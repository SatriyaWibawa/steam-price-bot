from dotenv import load_dotenv
import os
import requests
import time
import re
from keep_alive import keep_alive

load_dotenv()
keep_alive()

item_name = "Dreams & Nightmares Case"
steam_url = "https://steamcommunity.com/market/priceoverview/"
usd_to_idr = 16000  # Ganti sesuai kurs

bot_token = os.getenv("BOT_TOKEN")
chat_id = os.getenv("CHAT_ID")

def get_price_usd():
    params = {
        "country": "US",
        "currency": 1,
        "appid": 730,
        "market_hash_name": item_name
    }
    response = requests.get(steam_url, params=params)
    print("Steam API Status:", response.status_code)
    print("Steam API Response:", response.text)
    try:
        data = response.json()
        if "lowest_price" in data:
            price_str = re.sub(r"[^\d.]", "", data["lowest_price"])
            price_float = float(price_str)
            return int(price_float * usd_to_idr)
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

while True:
    price = get_price_usd()
    if price:
        message = f"[Update Harga Steam]\n📦 {item_name}\n💰 Harga Sekarang: Rp{price:,}"
        print("Harga (debug):", price)
        send_telegram_message(message)
    else:
        print("Gagal ambil harga.")

    time.sleep(3600)  # Tiap jam
