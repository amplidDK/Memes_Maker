import asyncio
import config
import asyncpraw
from aiogram import Bot, types

API_TOKEN = config.settings['TOKEN']
CHANNEL_ID = config.settings['CHANNEL_ID']  # channel id for sending memes

bot = Bot(token=API_TOKEN, parse_mode=types.ParseMode.HTML)

reddit = asyncpraw.Reddit(client_id=config.settings['CLIENT_ID'],
                          client_secret=config.settings['SECRET_CODE'],
                          user_agent='random_tg_bot/0.0.1')

mems = []
TIMEOUT = 600
SUBREDDIT_NAME = 'memes'
POST_LIMIT = 1


async def send_message(channel_id: int, text: str):
    await bot.send_message(channel_id, text)


async def main():
    while True:
        await asyncio.sleep(TIMEOUT)
        memes_submissions = await reddit.subreddit(SUBREDDIT_NAME)
        memes_submissions = memes_submissions.new(limit=POST_LIMIT)
        item = await memes_submissions.__anext__()
        if item not in mems:
            mems.append(item.title)
            await send_message(CHANNEL_ID, item.url)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
