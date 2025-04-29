# 🚀 DiscordPriceWatcher

DiscordPriceWatcher is a lightweight, modular Discord bot built with `discord.py` that fetches real-time cryptocurrency prices from the CoinGecko API.

This project is structured for scalability, clean code, and future feature upgrades.

---

## 📚 Features

- Fetch current price of a cryptocurrency using the `!price <symbol>` command.
- Modular architecture with separate services, commands, and event handlers.
- CoinGecko public API integration without the need for API keys.

---

## 🛠 Technologies

- Python 3.10+
- discord.py 2.x
- requests
- python-dotenv

---

## ▶️ Usage

1. Clone the repository.
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Create a `.env` file and add your Discord bot token:
    ```plaintext
    DISCORD_BOT_TOKEN=your_token_here
    ```
4. Run the bot:
    ```bash
    python main.py
    ```

---

## 📦 Current Structure

```
DiscordPriceWatcher/
├── bot
│   ├── commands
│   │   ├── __init__.py
│   │   ├── price.py 
│   ├── events
│   │   ├── on_ready.py
│   ├── __init__.py
├── main.py
├── README.md
├── requirements.txt
├── services
│   ├── coingecko_service.py
│   ├── __init__.py
└── utils
    └── __init__.py
```

---

## 🧩 Planned Future Improvements

- ✅ **Typo correction**: detect mistyped coin names and suggest the closest match (e.g., "bitcion" → "bitcoin").
- ✅ **Price tracking over time**: monitor price increase or decrease over a specified period (e.g., 24h, 7d).
- ✅ **Top coins analysis**:
  - Show the most popular coins.
  - Show the most expensive coins.
  - Show the cheapest coins.

---

## 🌟 Additional Planned Features for Full Version

- [ ] Slash command support (`/price`, `/topcoins`) for modern Discord UX.
- [ ] Alert system: automatic notifications when a coin reaches a certain price.
- [ ] Multi-currency support (USD, EUR, BTC, ETH prices).
- [ ] Caching API responses to reduce API calls and improve performance.
- [ ] Error handling for Discord API rate limits.
- [ ] Administrative panel (commands only accessible to admins).
- [ ] Simple web dashboard (optional future phase).

---

## 📬 Contact

Feel free to open an issue if you find bugs, have suggestions, or want to contribute!

---

⭐ If you like this project, give it a star!