import os, random, requests
from datetime import datetime, timedelta

BOT_TOKEN, CHAT_ID = os.getenv("BOT_TOKEN"), "@MYB4T"
RAWG_KEY = os.getenv("RAWG_API_KEY")

# Set date window (last 60 days to today) for active, trending releases
today = datetime.now().strftime("%Y-%m-%d")
start_date = (datetime.now() - timedelta(days=60)).strftime("%Y-%m-%d")

# Fetch top 10 trending games within the date window
url = f"https://api.rawg.io/api/games?key={RAWG_KEY}&dates={start_date},{today}&ordering=-added&page_size=10"
res_data = requests.get(url).json().get('results', [])

# Pick one game randomly so daily posts don't repeat
res = random.choice(res_data) if res_data else requests.get(f"https://api.rawg.io/api/games?key={RAWG_KEY}&page_size=1").json()['results'][0]

caption = f"🎮 <b>Trending Game: {res['name']}</b>\n⭐ <b>Rating:</b> {res['rating']}/5\n\n🤖 <i>Executed automatically via <a href=\"https://github.com/MrBoss002/Telegram-Daily-Automations\">GitHub Actions Cloud Workflow</a>.</i>\n\n❖ <b>Powered By:</b> @MrBossTG ❤️\n❖ <b>Developed By:</b> @MrBossRobot ❤️"

requests.post(
    f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto", 
    json={
        "chat_id": CHAT_ID, 
        "photo": res['background_image'], 
        "caption": caption, 
        "parse_mode": "HTML"
    }
)
