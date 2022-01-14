from pyrogram.errors.exceptions.bad_request_400 import YouBlockedUser

from userge import userge, Message
from userge.utils.exceptions import StopConversation
import asyncio

@userge.on_cmd(
    "recognise",
    about={
        "header": "Image Recognise",
        "description": "Get information about an image using AWS Recognition.",
        "usage": "Find out information including detected labels, faces. text and moderation tags.",
        "example": ".recognise [reply]",
    },
)
async def recog(message: Message):
    replied = message.reply_to_message

    if not replied:
        await message.err("reply to media")
        return
    chat = "@Rekognition_Bot"
    try:
        msg = await message.edit("`Recognising this media...`")
        async with userge.conversation(chat) as conv:
            try:
                await conv.send_message("/start")
                check = await conv.get_response()
                await replied.forward(chat)
                res = await conv.get_response()
                if res.media:
                    info = await conv.get_response()
                await userge.send_read_acknowledge(conv.chat_id)
                
            except YouBlockedUser:
                await message.err(f"**Please Unblock {chat} then try again**", del_in=5)
                return
            else:
               # await msg.delete()
                await message.edit(info.text.html)
    except StopConversation:
        pass
