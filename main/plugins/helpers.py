# Github.com/Vasusen-code

import asyncio
import os
import re
import time
from datetime import datetime as dt

from pyrogram.errors import (
    FloodWait,
    InviteHashExpired,
    InviteHashInvalid,
    UserAlreadyParticipant,
)

# Join private chat-------------------------------------------------------------------------------------------------------------


async def join(client, invite_link):
    try:
        await client.join_chat(invite_link)
        return "✅ Successfully joined the channel.\n\n✅ انضم بنجاح إلى القناة."
    except UserAlreadyParticipant:
        return (
            "I have already joined this channel.\n\nلقد انضممت بالفعل إلى هذه القناة."
        )
    except (InviteHashInvalid, InviteHashExpired):
        return "Unable to join your channel, I think your link is invalid or expired.\n\nغير قادر على الانضمام إلى قناتك ، أعتقد أن الرابط الخاص بك غير صالح أو منتهي الصلاحية."
    except FloodWait:
        return "FloodWait error, please try again later.\n\nخطأ ، يرجى المحاولة مرة أخرى لاحقًا.\nاو ان القناه فيه طلب انضمام فيجب على المشرفين الموافقه على الانضمام"
    except Exception as e:
        print(e)
        return "❌Something went wrong.\n\n❌ حدث خطأ ما.\nاو ان القناه فيه طلب انضمام فيجب على المشرفين الموافقه على الانضمام"


# Regex---------------------------------------------------------------------------------------------------------------
# to get the url from event


def get_link(string):
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(regex, string)
    try:
        link = [x[0] for x in url][0]
        if link:
            return link
        else:
            return False
    except Exception:
        return False


# Screenshot---------------------------------------------------------------------------------------------------------------


def hhmmss(seconds):
    x = time.strftime("%H:%M:%S", time.gmtime(seconds))
    return x


async def screenshot(video, duration, sender):
    if os.path.exists(f"{sender}.jpg"):
        return f"{sender}.jpg"
    time_stamp = hhmmss(int(duration) / 2)
    out = dt.now().isoformat("_", "seconds") + ".jpg"
    cmd = [
        "ffmpeg",
        "-ss",
        f"{time_stamp}",
        "-i",
        f"{video}",
        "-frames:v",
        "1",
        f"{out}",
        "-y",
    ]
    process = await asyncio.create_subprocess_exec(
        *cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    stderr.decode().strip()
    stdout.decode().strip()
    if os.path.isfile(out):
        return out
    else:
        None
