import os, random, requests

BOT_TOKEN, CHAT_ID = os.getenv("BOT_TOKEN"), "@MYB4T"
TMDB_KEY = os.getenv("TMDB_API_KEY")

# Supported language codes: ml (Malayalam), hi (Hindi), ta (Tamil), en (English)
LANGUAGES = [
    {"code": "ml", "name": "Malayalam 🌴"},
    {"code": "hi", "name": "Hindi 🍿"},
    {"code": "ta", "name": "Tamil ⚡"},
    {"code": "en", "name": "Hollywood 🎬"}
]

selected_lang = random.choice(LANGUAGES)

# Fetch trending movies filtering by original language
url = f"https://api.themoviedb.org/3/discover/movie?api_key={TMDB_KEY}&with_original_language={selected_lang['code']}&sort_by=popularity.desc&page=1"

try:
    data = requests.get(url, timeout=10).json().get('results', [])
    
    # Pick randomly from the top 5 results to ensure daily variety
    res = random.choice(data[:5]) if data else requests.get(f"https://api.themoviedb.org/3/trending/movie/day?api_key={TMDB_KEY}").json()['results'][0]
    
    title = res.get('title') or res.get('original_title')
    rating = round(res.get('vote_average', 0), 1)
    overview = res.get('overview', 'No plot summary available.')
    overview = overview[:180] + "..." if len(overview) > 180 else overview
    poster_path = res.get('poster_path')
    
    poster_url = f"https://image.tmdb.org/t/p/w500{poster_path}" if poster_path else "https://via.placeholder.com/500x750?text=No+Poster+Available"

    caption = (
        f"🎬 <b>Movie Spotlight: {title}</b> ({selected_lang['name']})\n"
        f"⭐ <b>Rating:</b> {rating}/10\n"
        f"📝 <i>{overview}</i>\n\n"
        "🤖 <i>Executed automatically via <a href=\"https://github.com/MrBoss002/Telegram-Daily-Automations\">GitHub Actions Cloud Workflow</a>.</i>\n\n"
        "❖ <b>Powered By:</b> @MrBossTG ❤️\n"
        "❖ <b>Developed By:</b> @MrBossRobot ❤️"
    )

    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto",
        json={
            "chat_id": CHAT_ID,
            "photo": poster_url,
            "caption": caption,
            "parse_mode": "HTML"
        }
    )

except Exception as e:
    # Basic fallback if API call fails
    caption = (
        "🎬 <b>Daily Movie Spotlight</b>\n\n"
        "🍿 Check out today's trending cinema releases!\n\n"
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
