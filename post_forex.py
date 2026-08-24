import os, requests

BOT_TOKEN, CHAT_ID = os.getenv("BOT_TOKEN"), "@MYB4T"

# Fetch rates based on 1 USD
fx = requests.get("https://open.er-api.com/v6/latest/USD").json()["rates"]

usd_inr = fx["INR"]

# Calculate direct rates to INR
aed_inr = round(usd_inr / fx["AED"], 2)
sar_inr = round(usd_inr / fx["SAR"], 2)
kwd_inr = round(usd_inr / fx["KWD"], 2)
eur_inr = round(usd_inr / fx["EUR"], 2)
gbp_inr = round(usd_inr / fx["GBP"], 2)

# Calculate values in USD
eur_usd = round(1 / fx["EUR"], 2)
gbp_usd = round(1 / fx["GBP"], 2)

caption = (
    "💵 <b>Daily Forex & Currency Rates</b>\n\n"
    f"• <b>1 USD:</b> ₹{usd_inr:.2f} INR\n"
    f"• <b>1 AED:</b> ₹{aed_inr} INR\n"
    f"• <b>1 SAR:</b> ₹{sar_inr} INR\n"
    f"• <b>1 KWD:</b> ₹{kwd_inr} INR\n"
    f"• <b>1 EUR:</b> ${eur_usd} USD | ₹{eur_inr} INR\n"
    f"• <b>1 GBP:</b> ${gbp_usd} USD | ₹{gbp_inr} INR\n\n"
    "🤖 <i>Executed automatically via <a href=\"https://github.com/MrBoss002/Telegram-Daily-Automations\">GitHub Actions Cloud Workflow</a>.</i>\n\n"
    "❖ <b>Powered By:</b> @MrBossTG ❤️\n"
    "❖ <b>Developed By:</b> @MrBossRobot ❤️"
)

requests.post(
    f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
    json={
        "chat_id": CHAT_ID,
        "text": caption,
        "parse_mode": "HTML",
        "disable_web_page_preview": True
    }
)
