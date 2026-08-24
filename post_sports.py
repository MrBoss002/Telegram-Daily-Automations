import os, requests
import xml.etree.ElementTree as ET

BOT_TOKEN, CHAT_ID = os.getenv("BOT_TOKEN"), "@MYB4T"

# Fetch latest sports news from BBC RSS Feed
rss_url = "https://feeds.bbci.co.uk/sport/rss.xml"

try:
    response = requests.get(rss_url, timeout=10)
    root = ET.fromstring(response.content)
    
    # Grab top 5 headlines
    items = root.findall(".//item")[:5]
    
    headlines_text = ""
    for idx, item in enumerate(items, 1):
        title = item.find("title").text.strip()
        link = item.find("link").text.strip()
        headlines_text += f"<b>{idx}. {title}</b>\n🔗 <a href='{link}'>Read Article</a>\n\n"

    caption = (
        "⚽ <b>Top 5 Sports Headlines Today</b>\n\n"
        f"{headlines_text}"
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

except Exception as e:
    # Fallback message
    caption = (
        "⚽ <b>Daily Sports Briefing</b>\n\n"
        "🔥 Global match highlights & league standings updated!\n\n"
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
