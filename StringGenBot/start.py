from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from config import OWNER_ID


def filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)

@Client.on_message(filter("start"))
async def start(bot: Client, msg: Message):
    me2 = (await bot.get_me()).mention
    await bot.send_message(
        chat_id=msg.chat.id,
        text=f"""✷ مـرحبا بـك عزيزي {msg.from_user.mention},

✷ انا {me2},
✷ لاستخراج جلسات البايروجرام و تيرمكس,

✷ يمكنك استخراج الجلسه من الاوامر والازرار ادناه 👇🏻✔️

المطور ʙʏ : [𝗞𝗜𝗡𝗗𝗜 〄](tg://user?id={OWNER_ID}) !""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="بدء الان", callback_data="generate")
                ],
                [
                    InlineKeyboardButton("قناة البوت", url="https://t.me/NNINB"),
                    InlineKeyboardButton("المطور", user_id=OWNER_ID)
                ]
            ]
        ),
        disable_web_page_preview=True,
    )
