
# Github.com/Vasusen-code

"""
Plugin for both public & private channels!\n\nالبرنامج المساعد لكل من القنوات العامة والخاصة!
"""

import time

from pyrogram.errors import FloodWait
from telethon import Button, events

from main.plugins.helpers import get_link
from main.plugins.pyroplug import check, get_bulk_msg

from .. import AUTH
from .. import FORCESUB as fs
from .. import Bot
from .. import bot as Drone
from .. import userbot

ft = f"To use this bot you've to join @{fs}."

batch = []


async def get_pvt_content(event, chat, id):
    msg = await userbot.get_messages(chat, ids=id)
    await event.client.send_message(event.chat_id, msg)


@Drone.on(events.NewMessage(incoming=True, pattern="/bulk"))
async def _batch(event):
    if not event.is_private:
        return
    # wtf is the use of fsub here if the command is meant for the owner?
    # well am too lazy to clean

    if f"{event.sender_id}" in batch:
        return await event.reply(
            "One bulk saving is already going on.\n\nيجري بالفعل توفير مجمع واحد."
        )
    async with Drone.conversation(event.chat_id) as conv:

        await conv.send_message(
            "Send me the message link from where you want to initialise bulk saving.\n\nأرسل لي رابط الرسالة من حيث تريد بدء الحفظ المجمع.",
            buttons=Button.force_reply(),
        )
        try:
            link = await conv.get_reply()
            try:
                _link = get_link(link.text)
            except Exception:
                await conv.send_message(
                    "⚠️No valid link found.\n\n⚠️ لم يتم العثور على رابط صالح."
                )
        except Exception as e:
            print(e)
            return await conv.send_message("Timed out!")
        await conv.send_message(
            "Send the number of files that you want to save upto 400.\n\nأرسل عدد الملفات التي تريد حفظها حتى 400 ملف.",
            buttons=Button.force_reply(),
        )
        try:
            _range = await conv.get_reply()
        except Exception as e:
            print(e)
            return await conv.send_message("Timed out!")
        try:
            value = int(_range.text)
            if value > 400:
                return await conv.send_message(
                    "You can only get upto 400 files in a single bulk save.\n\nيمكنك فقط الحصول على ما يصل إلى 400 ملف في عملية حفظ مجمعة واحدة."
                )
        except ValueError:
            return await conv.send_message(
                "Please send only number!\n\nالرجاء ارسال الرقم فقط!"
            )
        s, r = await check(userbot, Bot, _link)
        if s != True:
            await conv.send_message(r)
            return
        batch.append(f"{event.sender_id}")
        await run_batch(userbot, Bot, event.sender_id, _link, value)
        conv.cancel()
        batch.pop(0)


async def run_batch(userbot, client, sender, link, _range):
    for i in range(_range):
        timer = 60
        if i < 25:
            timer = 5
        if i < 50 and i > 25:
            timer = 10
        if i < 100 and i > 50:
            timer = 15
        if not "t.me/c/" in link:
            if i < 25:
                timer = 2
            else:
                timer = 3
        try:
            await get_bulk_msg(userbot, client, sender, link, i)
        except FloodWait as fw:
            await asyncio.sleep(fw.seconds + 5)
            await get_bulk_msg(userbot, client, sender, link, i)
        protection = await client.send_message(
            sender,
            f"Sending Next File In `{timer}` seconds.\n\nإرسال الملف التالي في غضون `{timer}` ثانية.",
        )
        time.sleep(timer)
        await protection.delete()
