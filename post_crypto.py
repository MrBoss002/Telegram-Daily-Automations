import os, requests

BOT_TOKEN, CHAT_ID = os.getenv("BOT_TOKEN"), "@MYB4T"

fx = requests.get("https://open.er-api.com/v6/latest/USD").json()["rates"]
inr, aed = fx["INR"], fx["AED"]

crypto = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,solana&vs_currencies=usd").json()
btc, eth, sol = crypto["bitcoin"]["usd"], crypto["ethereum"]["usd"], crypto["solana"]["usd"]

caption = f"🪙 <b>Crypto Market Overview</b>\n\n• <b>BTC:</b> ${btc:,} (₹{btc * inr:,.0f} | {btc * aed:,.0f} AED)\n• <b>ETH:</b> ${eth:,}\n• <b>SOL:</b> ${sol:,}\n\n🤖 <i>Executed automatically via <a href=\"https://github.com/MrBoss002/Telegram-Daily-Automations\">GitHub Actions Cloud Workflow</a>.</i>\n\n❖ <b>Powered By:</b> @MrBossTG ❤️\n❖ <b>Developed By:</b> @MrBossRobot ❤️"

requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage", json={"chat_id": CHAT_ID, "text": caption, "parse_mode": "HTML"})
