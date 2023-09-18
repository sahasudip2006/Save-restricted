# Github.com/Vasusen-code

import os

from telethon import Button, events
from telethon.errors.rpcerrorlist import UserNotParticipantError
from telethon.tl.functions.channels import GetParticipantRequest

# What the hell is it??
from telethon.tl.functions.users import GetFullUserRequest

from .. import bot as Drone

# end

S = "/" + "s" + "t" + "a" + "r" + "t"
# join check
async def check_user(id):
    ok = True
    try:
        await Drone(GetParticipantRequest(channel="@O_W_B", participant=id))
        ok = True
    except UserNotParticipantError:
        ok = False
    return ok


# end
@Drone.on(events.NewMessage(pattern="^/thumb$"))
async def sett(event):
    Drone = event.client

    async with Drone.conversation(event.chat_id) as conv:
        xx = await conv.send_message(
            "Alright, now send me image file to use it for thumbnail.\n\nحسنًا ، أرسل لي الآن ملف صورة لاستخدامه كصورة مصغرة",
            buttons=Button.force_reply(),
        )
        x = await conv.get_reply()
        if not x.media:
            xx.edit("Please send media file.\n\nالرجاء إرسال ملف الوسائط.")
        mime = x.file.mime_type
        if not "png" in mime:
            if not "jpg" in mime:
                if not "jpeg" in mime:
                    return await xx.edit("Image not found.\n\n")
        await xx.delete()
        t = await event.client.send_message(event.chat_id, "⏳")
        path = await event.client.download_media(x.media)
        if os.path.exists(f"{event.sender_id}.jpg"):
            os.remove(f"{event.sender_id}.jpg")
        os.rename(path, f"./{event.sender_id}.jpg")
        await t.edit(
            "✅ Thumbnail successfully saved.\n\n✅ تم حفظ الصورة المصغرة بنجاح."
        )


@Drone.on(events.NewMessage(incoming=True, pattern=f"{S}"))
async def start(event):
    await Drone(GetFullUserRequest(event.sender_id))
    if (await check_user(event.sender_id)) == False:
        return await event.reply(
            f"please join @O_W_B my channel to use me!",
            buttons=[Button.url("Join Channel", url="https://t.me/O_W_B")],
        )
    await event.reply(
        f"Hii,\n**I am save restricted contents bot, I can save files of restricted channels as well as group.\n**Hit /help to learn more.\n\nحفظ المحتويات المقيدة بوت ، يمكنني حفظ ملفات القنوات المقيدة وكذلك المجموع\n اضغط /help لمعرفة المزيد.",
        buttons=[
            [
                Button.url("Updates Channel", url="https://t.me/U_E_K"),
                Button.url("Support Group", url="https://t.me/SESSIONSUPPORT"),
            ],
            [
              Button.url("Bot channel", url="https://t.me/S8Y8S"), 
              Button.url("DEV", url="https://t.me/N_B_0")
              
              ],
        ],
    )
    # start help Message


@Drone.on(events.NewMessage(pattern="^/help$"))
async def search(event):
    ok = await Drone(GetFullUserRequest(event.sender_id))
    if (await check_user(event.sender_id)) == False:
        return await event.reply(
            f"{ok.user.first_name}, please join my channel to use me!",
            buttons=[Button.url("Join Channel", url="https://t.me/O_W_B")],
        )
    await event.reply(
        "<b><u>For Public Restricted Channel contents.</b></u>\nTo get public restricted Channel contents, just send your Post link i will give you that post without Downloading.\n\nللحصول على محتويات القناة العامة المقيدة ، ما عليك سوى إرسال رابط المنشور الخاص بك ، وسأعطيك هذا المنشور دون تنزيل\n\n<b><u>For Private Restricted Channel contents.</b></u>\nTo get private restricted Channel contents, First send Channel invite link so that i can join your channel after that send me post link of your restricted Channel to get that post.\n\nللحصول على محتويات القناة المقيدة الخاصة ، أرسل أولاً رابط دعوة القناة حتى أتمكن من الانضمام إلى قناتك بعد ذلك أرسل لي رابط النشر الخاص بقناتك المقيدة للحصول على هذا المنشور.\n\n\n\n Bot Commands\n\n /help\n\n/thumb : Convert a file to a thumbnail \n\n /bulk : To save a group of pictures at once ",
        parse_mode="HTML",
    )


# end help Message
