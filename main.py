from aiogram import *
from config import Bot_token
from icrawler.builtin import GoogleImageCrawler
import os

bot = Bot(Bot_token)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_message(message: types.Message):
    chat_id = message.chat.id
    await bot.send_message(chat_id, 'Hi i can search photos')


@dp.message_handler()
async def type_search(message: types.Message):
    filters = dict(
        type='photo',
        color='red',
        size='large',
        # license='noncommercial, commercial'
    )
    crawler = GoogleImageCrawler(storage={'root_dir': './img'})
    crawler.crawl(keyword=message.text,
                  max_num=1,
                  overwrite=True,
                  filters=filters,
                  file_idx_offset='auto'
                  )
    with open(r'C:\Student life and project\project\tg _bot\search\img\000001.jpg', 'rb+') as f:
        await bot.send_photo(message.chat.id, f)
        os.remove('img/000001.jpg')


if __name__ == '__main__':
    executor.start_polling(dp)
