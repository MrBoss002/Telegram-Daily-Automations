import os, requests

BOT_TOKEN, CHAT_ID = os.getenv("BOT_TOKEN"), "@MYB4T"
TMDB_KEY = os.getenv("TMDB_API_KEY")

res = requests.get(f"https://api.themoviedb.org/3/trending/movie/day?api_key={TMDB_KEY}").json()['results'][0]
caption = f"🎬 <b>Daily Movie Spotlight: {res['title']}</b>\n⭐ <b>Rating:</b> {res['vote_average']}/10\n📝 <i>{res['overview'][:180]}...</i>\n\n🤖 <i>Executed automatically via <a href=\"https://github.com/MrBoss002/Telegram-Daily-Automations\">GitHub Actions Cloud Workflow</a>.</i>\n\n❖ <b>Powered By:</b> @MrBossTG ❤️\n❖ <b>Developed By:</b> @MrBossRobot ❤️"

requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto", json={"chat_id": CHAT_ID, "photo": f"https://image.tmdb.org/t/p/w500{res['poster_path']}", "caption": caption, "parse_mode": "HTML"})
