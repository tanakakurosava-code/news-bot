import os
import feedparser
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

RSS_FEEDS = [
    "https://feeds.bbci.co.uk/news/world/rss.xml",
    "https://www.aljazeera.com/xml/rss/all.xml"
]

def get_news():
    news = []
    for url in RSS_FEEDS:
        feed = feedparser.parse(url)
        for e in feed.entries[:5]:
            news.append(f"{e.title}\n{e.link}")
    return news

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🧠 Бот работает в облаке")

async def latest(update: Update, context: ContextTypes.DEFAULT_TYPE):
    news = get_news()
    await update.message.reply_text("\n\n".join(news[:5]))

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("latest", latest))

app.run_polling()
