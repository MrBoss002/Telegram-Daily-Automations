import os
import requests

# -------------------------------------------------------------------
# CONFIGURATION & SECRETS
# -------------------------------------------------------------------
BOT_TOKEN = os.getenv("BOT_TOKEN")
TMDB_API_KEY = os.getenv("TMDB_API_KEY")
RAWG_API_KEY = os.getenv("RAWG_API_KEY")
CHAT_ID = "@MYB4T"

GITHUB_REPO_URL = "https://github.com/MrBoss002/Telegram-Daily-Automations"

# -------------------------------------------------------------------
# 1. FOREX & CRYPTO (ExchangeRate-API & CoinGecko)
# -------------------------------------------------------------------
fx_data = requests.get("https://open.er-api.com/v6/latest/USD").json()
inr_rate = round(fx_data["rates"]["INR"], 2)
aed_rate = round(fx_data["rates"]["AED"], 2)

crypto_url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,solana&vs_currencies=usd"
crypto_data = requests.get(crypto_url).json()

btc_usd = crypto_data["bitcoin"]["usd"]
eth_usd = crypto_data["ethereum"]["usd"]
sol_usd = crypto_data["solana"]["usd"]

btc_inr = f"{btc_usd * inr_rate:,.0f}"
btc_aed = f"{btc_usd * aed_rate:,.0f}"

# -------------------------------------------------------------------
# 2. MOVIES & TV (TMDb)
# -------------------------------------------------------------------
tmdb_url = f"https://api.themoviedb.org/3/trending/movie/day?api_key={TMDB_API_KEY}"
tmdb_res = requests.get(tmdb_url).json()
movie = tmdb_res['results'][0]

movie_title = movie['title']
movie_rating = movie['vote_average']
movie_overview = movie['overview'][:150] + "..."
poster_url = f"https://image.tmdb.org/t/p/w500{movie['poster_path']}"

# -------------------------------------------------------------------
# 3. VIDEO GAMES (RAWG)
# -------------------------------------------------------------------
rawg_url = f"https://api.rawg.io/api/games?key={RAWG_API_KEY}&page_size=1"
rawg_res = requests.get(rawg_url).json()
game = rawg_res['results'][0]

game_name = game['name']
game_rating = game['rating']

# -------------------------------------------------------------------
# 4. SPORTS HIGHLIGHTS (TheSportsDB)
# -------------------------------------------------------------------
sports_url = "https://www.thesportsdb.com/api/v1/json/3/searchevents.php?e=Arsenal_vs_Chelsea"
try:
    sports_res = requests.get(sports_url).json()
    sports_event = sports_res['event'][0]
    sports_info = f"{sports_event['strEvent']} ({sports_event['strLeague']})"
except Exception:
    sports_info = "Premier League & International Matches Updated"

# -------------------------------------------------------------------
# 5. CAPTION & BRANDING FOOTER
# -------------------------------------------------------------------
caption = f"""
🎬 <b>Daily Movie Spotlight: {movie_title}</b>
⭐ <b>Rating:</b> {movie_rating}/10
📝 <i>{movie_overview}</i>

🎮 <b>Trending Game:</b> {game_name} (⭐ {game_rating}/5)
⚽ <b>Sports Highlight:</b> {sports_info}

------------------------------------
💵 <b>Forex Rates (USD Base)</b>
• 1 USD = <b>₹{inr_rate} INR</b>
• 1 USD = <b>{aed_rate} AED (Dirham)</b>

🪙 <b>Crypto Overview</b>
• BTC: <b>${btc_usd:,}</b> (₹{btc_inr} | {btc_aed} AED)
• ETH: <b>${eth_usd:,}</b>
• SOL: <b>${sol_usd:,}</b>

🤖 <i>Executed automatically via <a href="{GITHUB_REPO_URL}">GitHub Actions Cloud Workflow</a>.</i>

❖ <b>Powered By:</b> @MrBossTG ❤️
❖ <b>Developed By:</b> @MrBossRobot ❤️
"""

# -------------------------------------------------------------------
# 6. SEND TO TELEGRAM
# -------------------------------------------------------------------
send_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"
payload = {
    "chat_id": CHAT_ID,
    "photo": poster_url,
    "caption": caption,
    "parse_mode": "HTML"
}

requests.post(send_url, json=payload)
