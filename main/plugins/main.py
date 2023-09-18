# Github.com/Vasusen-code


from telethon import events

from main.plugins.helpers import get_link, join
from main.plugins.pyroplug import get_msg

from .. import FORCESUB as fs
from .. import Bot
from .. import bot as Drone
from .. import userbot

ft = f"To use this bot you've to join @{fs}.\n\nلاستخدام هذا الروبوت ، عليك الانضمام إلى @{fs}."

# To-Do:
# Make these codes shorter and clean
# ofc will never do it.


@Drone.on(events.NewMessage(incoming=True, func=lambda e: e.is_private))
async def clone(event):
    if event.is_reply:
        return
    try:
        link = get_link(event.text)
        if not link:
            return
    except TypeError:
        return

    edit = await event.reply("⏳")
    if "t.me/+" in link:
        q = await join(userbot, link)
        await edit.edit(q)
        return
    if "t.me/" in link:
        await get_msg(userbot, Bot, event.sender_id, edit.id, link, 0)
