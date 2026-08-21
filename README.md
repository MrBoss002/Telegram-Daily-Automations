<div align="center">

  # 🚀 Telegram Daily Automations

[![License: MIT](https://img.shields.io/badge/License-MIT-a855f7?style=for-the-badge&logo=opensourceinitiative&logoColor=white)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.10-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![GitHub Actions](https://img.shields.io/badge/Automated-GitHub_Actions-ec4899?style=for-the-badge&logo=githubactions&logoColor=white)](https://github.com/features/actions)

**A fully serverless, automated Python suite that fetches daily trending content and market updates, broadcasting them directly to a Telegram channel. Hosted 100% free using GitHub Actions.**

</div>

---

## 📢 Live Demo

Want to see this project in action? Check out the live automated posts delivered straight to our Telegram channel:

<div align="center">

  [![Join @MYB4T on Telegram](https://img.shields.io/badge/Telegram-Join_@MYB4T-8b5cf6?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/MYB4T)

</div>

---

## ✨ Features

This repository contains 5 independent automation scripts, each scheduled to run at specific times throughout the day:

| Feature | Script | Description | Powered By |
| :--- | :--- | :--- | :--- |
| **💵 Forex Rates** | `post_forex.py` | Daily USD conversion rates to INR and AED (Dirham) | Open Exchange Rates |
| **🎬 Movie Spotlight** | `post_movie.py` | Top trending movie of the day with poster, rating, and summary | TMDb |
| **🎮 Gaming Update** | `post_game.py` | Top trending video game with its rating and artwork | RAWG |
| **🪙 Crypto Market** | `post_crypto.py` | Live prices for BTC, ETH, and SOL in USD, INR, and AED | CoinGecko |
| **⚽ Sports Highlights** | `post_sports.py` | Latest match updates, scores, and league information | TheSportsDB |

---

## 🛠️ Prerequisites

To deploy this project yourself, you will need:
1. A **Telegram Bot Token** (Get this from [@BotFather](https://t.me/botfather) on Telegram).
2. A public Telegram Channel (Your bot must be added as an **Administrator** with posting permissions).
3. Free API Keys from:
   * [TMDb](https://www.themoviedb.org/) (For movie updates)
   * [RAWG](https://rawg.io/apidocs) (For gaming updates)

---

## 🚀 Setup & Installation

**1. Get the Repository**

* **Option A — Fork on GitHub (Recommended):** If you plan to host the automated workflows directly on GitHub Actions, you must fork this repository to your own account:  

<div align="center">
  
  [![Fork Repository](https://img.shields.io/badge/Fork-This_Repo-10B981?style=for-the-badge&logo=github&logoColor=white)](https://github.com/MrBoss002/Telegram-Daily-Automations/fork)

</div>

* **Option B — Clone via Terminal:** If you just want to run or test the scripts locally on your computer, clone the repository directly (no fork required):

```bash
  git clone [https://github.com/MrBoss002/Telegram-Daily-Automations.git](https://github.com/MrBoss002/Telegram-Daily-Automations.git)
```

<br\>

**2. Configure GitHub Secrets**
Go to your repository settings: Settings > Secrets and variables > Actions > New repository secret. Add the following:

- `BOT_TOKEN`: Your Telegram Bot API token.

- `TMDB_API_KEY`: Your TMDb developer key.

- `RAWG_API_KEY`: Your RAWG developer key.

<br\>

**3. Update Channel ID**
By default, the scripts broadcast to **@MYB4T**. If you fork this repository, update the CHAT_ID variable inside each .py file to your own channel's handle (e.g., @YourChannelName).


---

## ⏱️ Automation Schedule (UTC)
The workflow (.github/workflows/daily.yml) automatically triggers the scripts based on this daily schedule:

- 04:00 AM: Forex Rates

- 08:00 AM: Movie Spotlight

- 12:00 PM: Trending Game

- 04:00 PM: Crypto Overview

- 08:00 PM: Sports Highlights

Note: You can manually trigger all scripts at once anytime by going to the Actions tab in GitHub and clicking Run workflow.

---

## 🎨 Formatting
Captions are styled using Telegram's HTML parse mode for clean, keyword-focused layouts, ensuring maximum visual clarity.

* **Clean Visual Hierarchy:** Uses bold headers and HTML tags (`<b>`, `<i>`, `<a>`) for high readability without cluttering posts with extra hashtags.
* **Smart Content Truncation:** Descriptions and plot summaries are automatically shortened to maintain crisp, scannable posts on mobile and desktop screens.

---

## ☕ Support & Community

<div align="center">
  
If this automation workflow saved you time or helped power your Telegram channels, consider supporting the ongoing development of this project!

| ☕ Support Developer | 🌐 Official Channel | ⛑ Need Assistance |
| :---: | :---: | :---: |
| [![Buy Me A Coffee](https://img.shields.io/badge/Buy%20Me%20A%20Coffee-FFDD00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black)](https://www.buymeacoffee.com/MrBoss002) | [![Powered By](https://img.shields.io/badge/Powered%20By-%40MrBossTG-FF0055?style=for-the-badge&logo=telegram&logoColor=blue)](https://t.me/MrBossTG) | [![Dev Help](https://img.shields.io/badge/Contact-Developer-229ED9?style=for-the-badge&logo=telegram&logoColor=blue)](https://t.me/ZeroTwoCare) |

<br />

[![Developed By](https://img.shields.io/badge/Developed%20By-%40MrBoss002-00C853?style=flat-square&logo=github)](https://github.com/MrBoss002)

**Telegram Daily Automations** • Built with ❤️ for open-source developers.

</div>
