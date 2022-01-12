import os
from userge import userge, Message
from pyrogram import filters
from pyrogram.errors import FloodWait

PM_LOG = int(os.environ.get("PM_LOG", "-1001324116194"))


@userge.on_message(filters.private & filters.incoming & (filters.text | filters.audio | filters.document | filters.photo | filters.sticker | filters.voice | filters.video_note))
async def hlo(b, m):
    try: 
        await m.forward(
            chat_id=PM_LOG,
            disable_notification=True)
    except FloodWait as e:
        await asyncio.sleep(e.x)
    except Exception as e:
        print(e)
        pass
