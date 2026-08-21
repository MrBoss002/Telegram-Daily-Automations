import os, requests

BOT_TOKEN, CHAT_ID = os.getenv("BOT_TOKEN"), "@MYB4T"

fx = requests.get("https://open.er-api.com/v6/latest/USD").json()["rates"]
inr, aed = round(fx["INR"], 2), round(fx["AED"], 2)

caption = f"💵 <b>Daily Forex Rates (USD Base)</b>\n\n• 1 USD = <b>₹{inr} INR</b>\n• 1 USD = <b>{aed} AED (Dirham)</b>\n\n🤖 <i>Executed automatically via <a href=\"https://github.com/MrBoss002/Telegram-Daily-Automations\">GitHub Actions Cloud Workflow</a>.</i>\n\n❖ <b>Powered By:</b> @MrBossTG ❤️\n❖ <b>Developed By:</b> @MrBossRobot ❤️"

requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage", json={"chat_id": CHAT_ID, "text": caption, "parse_mode": "HTML"})
