import asyncio
import json
import logging
import sys

from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from datetime import datetime
import time
import schedule

import api

TOKEN = "6484926032:AAFejkyFe6Rk4s2_pN0NjqwX6YZPPw9DuQ8"
ADMIN = 951880371

dp = Dispatcher()
bot = Bot(TOKEN, parse_mode=ParseMode.HTML)

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, {hbold(message.from_user.full_name)}!")

@dp.message()
async def echo_handler(message: types.Message) -> None:
    await message.answer(message)


async def remainder_birthday(message: types.Message) -> None:
    try:
        result_array = []
        response = api.get_staffs().text;
        data = json.loads(response)

        for i in data:
            target_date = datetime.strptime(i["staff_birthday"], '%Y-%m-%d')
            current_date = datetime.now()
            if target_date.month == current_date.month and target_date.day == current_date.day:
                result_array.append(i);

        if len(result_array)==0:
            await bot.send_message(chat_id=ADMIN, text="Today is nobody's birthday")
            return


        for k in range(len(result_array)):
            response_text = ("Today is birthday of " + "\n\n"
                             + "Fullname: " + str(result_array[k]["staff_name"]) + " " +
                             str(result_array[k]["staff_surname"]) + "\n" +
                             "Birthday: " + str(result_array[k]["staff_birthday"])
                             )
            await bot.send_message(chat_id=ADMIN, text=response_text)
            image_path = 'https://picsum.photos/200/300'

            await bot.send_photo(chat_id=ADMIN, photo=image_path)

    except TypeError:
        await message.answer("Nice try!")


schedule.every(10).seconds.do(remainder_birthday());

while True:
   schedule.run_pending()
   time.sleep(1)


async def main() -> None:
    # bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())

