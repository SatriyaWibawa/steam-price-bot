# 🔔 Steam Price Bot (Telegram)

Bot Telegram yang mengirim harga terbaru item di Steam Market secara otomatis setiap 1 jam.

> Contoh item: **Dreams & Nightmares Case (CS2)**

## 🚀 Fitur

* Ambil data harga langsung dari Steam Community Market
* Konversi ke Rupiah otomatis
* Kirim update harga ke Telegram setiap jam
* Bisa berjalan 24 jam gratis via Replit + UptimeRobot

---

## 🧹 Tech Stack

* Python 3
* Telegram Bot API
* Steam Market PriceOverview API
* Flask (untuk keep-alive Replit)
* Replit + UptimeRobot (gratis hosting)

---

## ⚙️ Cara Install

### 1. Clone Repo

```bash
git clone https://github.com/USERNAME/steam-price-bot.git
cd steam-price-bot
```

### 2. Buat Virtual Environment (opsional)

```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Siapkan File `.env`

Buat file `.env` berdasarkan `.env.example`, lalu isi:

```
BOT_TOKEN=isi_token_telegram_bot
CHAT_ID=isi_chat_id_telegram
```

> Cara ambil token: via @BotFather di Telegram
> Cara ambil chat\_id: kirim pesan ke bot, lalu buka:
> `https://api.telegram.org/bot<BOT_TOKEN>/getUpdates`

---

## ▶️ Jalankan Bot

```bash
python main.py
```

Bot akan otomatis mengirim update harga item ke Telegram setiap 1 jam.

---

## 🖉 Jalankan 24 Jam Gratis (Replit + UptimeRobot)

### A. Upload ke Replit

1. Buka [https://replit.com](https://replit.com)
2. Buat project baru, upload semua file (`main.py`, `keep_alive.py`, `.env`, dll)
3. Tambahkan file `.replit`:

```toml
entrypoint = "main.py"
```

4. Klik **Run** untuk menjalankan bot

### B. Buka URL Bot

* Klik tombol ↗ (open in new tab) di kanan atas
* Copy URL bot kamu (biasanya bentuknya: `https://project.username.repl.co`)

### C. Setup UptimeRobot

1. Buka [https://uptimerobot.com](https://uptimerobot.com)
2. Daftar / login
3. Klik **"Add New Monitor"**

   * Type: HTTP(s)
   * Name: `Steam Price Bot`
   * URL: masukkan URL dari Replit kamu
   * Interval: 5 menit
4. Simpan dan aktifkan

---

## 📦 Contoh Pesan Telegram

```
[Update Harga Steam]
📦 Dreams & Nightmares Case
💰 Harga Sekarang: Rp36,320
```

---

## 🤝 Kontribusi

Pull request sangat terbuka! Kamu bisa bantu:

* Tambahkan target notifikasi harga
* Logging ke CSV atau Google Sheets
* Buat grafik tren harga mingguan

---

## 📄 License

MIT License
