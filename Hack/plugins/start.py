import env
from Hack import bot
from Hack.helpers import MENU1, KEYBOARD1, PM_TEXT, PM_BUTTON
from Hack.database import DB
from pyrogram import filters
from pyrogram.types import CallbackQuery


@bot.on_message(filters.command("start") & filters.private)
async def _start(_, message):
    user_id = message.from_user.id
    user = message.from_user.mention
    bot = (await _.get_me()).mention
    if DB:
        await DB.add_user(id)
    if env.LOG_GROUP_ID:
        await bot.send_message(env.LOG_GROUP_ID,
                               f'{mention} Has Just Started The Bot')
    await message.reply_photo(
       photo = env.START_IMG_URL,
       caption = PM_TEXT.format(user, bot),
       reply_markup = PM_BUTTON) 


@bot.on_message(filters.command("hack") & filters.private)
async def _hack(_, message):
    await message.reply_text(MENU1,
              reply_markup = KEYBOARD1) 


@bot.on_callback_query(filters.regex("hack_btn"))
async def heck_callback(bot : app, query : CallbackQuery):
    await query.message.delete()
    await query.message.reply_text(MENU1,
              reply_markup = KEYBOARD1)

