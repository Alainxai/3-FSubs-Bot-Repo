#(©)Codexbotz
#Recoded By @Its_Tartaglia_Childe

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>┏━━━━━•◦●◉✿ ❟❛❟ ✿◉●◦•━━━━━━┓\n× ɢᴏᴅ : <a href='https://t.me/Lucifer_x0o'>ᴀʙʀᴀʜᴀᴍ™</a>\n× ʜᴇɴᴛᴀɪ ᴄʜᴀɴɴᴇʟ : <a href='https://t.me/Hentaii_flix'>ʜᴇɴᴛᴀɪ ꜰʟɪx</a>\n× ʙᴏᴛ ꜰᴏʀ : <a href='https://t.me/Anime_Flix_Network'>ᴀɴɪᴍᴇ ꜰʟɪx ɴᴇᴛᴡᴏʀᴋ</a>\n┗━━━━━•◦●◉✿ ❟❛❟ ✿◉●◦•━━━━━━┛</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("☠️ ᴄʟᴏꜱᴇ ☠️", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
