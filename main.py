# imports
from pyrogram import Client, filters, types
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import requests, json
from pytz import utc
import random as raffy
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# config
CONFIG = json.load(open(f"config.json", encoding = 'utf-8'))

# get bot token from https://t.me/BotFather
BOT = Client(CONFIG['SESSION_NAME'], CONFIG['API_ID'], CONFIG['API_HASH'], bot_token=CONFIG['BOT_TOKEN'])

# api used to get porn & from which subreddits, follow the key if u wanna add more! (can not be porn as well, just subreddit.
API = CONFIG['URL_API']
ENDPOINTS = ["pussy", "ass", "boobs", "milf", "teen", "asian"]

# channel chat id where the bot will send porns every 30 seconds, make sure the bot is admin
CHANNEL = -1001654351009

# function to send the message
async def funzione():
    ENDPOINT = raffy.choice(ENDPOINTS)
    r = requests.get(API + ENDPOINT)
    PK = r.json()
    KEYBOARD = [
        [
            InlineKeyboardButton("🔗 Post Link", url=PK.get('postLink')),
            InlineKeyboardButton("🌠 Photo Link", url=PK.get('url'))
        ],      
        [
            InlineKeyboardButton("📌 CircusClan", url="https://t.me/CircusClan")
        ]       
    ]
        
    try:
        await BOT.send_photo(CHANNEL, PK.get('url'), caption=f"ℹ️ | {PK.get('title')}\n\n☁️ Subreddit: {ENDPOINT.capitalize()}\n🍑 NSFW Content: ✅\n👍 UPs: {PK.get('ups')}", reply_markup=InlineKeyboardMarkup(KEYBOARD))
    except:
        await BOT.send_photo(CHANNEL, PK.get('url'), caption=f"ℹ️ | {PK.get('title')}\n\n☁️ Subreddit: {ENDPOINT.capitalize()}\n🍑 NSFW Content: ✅\n👍 UPs: {PK.get('ups')}", reply_markup=InlineKeyboardMarkup(KEYBOARD))
        
#scheduler things, dont touch if u dont know what u doin'        
scheduler = AsyncIOScheduler()
scheduler.add_job(funzione, "interval", timezone=utc, seconds=30)
scheduler.start()
BOT.run()
