import os, requests

BOT_TOKEN, CHAT_ID = os.getenv("BOT_TOKEN"), "@MYB4T"

# Fetch recent/upcoming sports events (using free test key 3 or 123)
url = "https://www.thesportsdb.com/api/v1/json/3/searchevents.php?e=Arsenal_vs_Chelsea"
try:
    res = requests.get(url).json()
    event = res['event'][0]
    match_title = event['strEvent']
    league = event['strLeague']
    thumb = event['strThumb'] if event.get('strThumb') else "https://www.thesportsdb.com/images/media/event/thumb/sp80111693821035.jpg"
    caption = f"⚽ <b>Sports Highlight: {match_title}</b>\n🏆 <b>League:</b> {league}\n\n🤖 <i>Executed automatically via <a href=\"https://github.com/MrBoss002/Telegram-Daily-Automations\">GitHub Actions Cloud Workflow</a>.</i>\n\n❖ <b>Powered By:</b> @MrBossTG ❤️\n❖ <b>Developed By:</b> @MrBossRobot ❤️"
    
    # Send as photo post
    requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto", json={"chat_id": CHAT_ID, "photo": thumb, "caption": caption, "parse_mode": "HTML"})
except Exception:
    # Fallback text if endpoint is busy
    caption = "⚽ <b>Daily Sports Briefing</b>\n\n🔥 Match highlights & league standings updated!\n\n🤖 <i>Executed automatically via <a href=\"https://github.com/MrBoss002/Telegram-Daily-Automations\">GitHub Actions Cloud Workflow</a>.</i>\n\n❖ <b>Powered By:</b> @MrBossTG ❤️\n❖ <b>Developed By:</b> @MrBossRobot ❤️"
    requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage", json={"chat_id": CHAT_ID, "text": caption, "parse_mode": "HTML"})
