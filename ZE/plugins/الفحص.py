import random
import time
from datetime import datetime
from platform import python_version

import requests
from telethon import Button, events, version
from telethon.errors.rpcerrorlist import (
    MediaEmptyError,
    WebpageCurlFailedError,
    WebpageMediaEmptyError,
)

from ZE import StartTime, jmthonversion, ZE

from ..Config import Config
from ..core.managers import edit_or_reply
from ..helpers.functions import check_data_base_heal_th, get_readable_time
from ..helpers.utils import reply_id
from ..sql_helper.globals import gvarstatus
from . import mention


@ZE.ar_cmd(pattern="فحص$")
async def amireallyalive(event):
    reply_to_id = await reply_id(event)
    ANIME = None
    jmthon_caption = gvarstatus("ALIVE_TEMPLATE") or temp
    if "ANIME" in jmthon_caption:
        data = requests.get("https://animechan.vercel.app/api/random").json()
        ANIME = f"**“{data['quote']}” - {data['character']} ({data['anime']})**"
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    jmthonevent = await edit_or_reply(event, "**- جار التأكد انتظر قليلا**")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    _, check_sgnirts = check_data_base_heal_th()
    EMOJI = gvarstatus("ALIVE_EMOJI") or "  - "
    ALIVE_TEXT = gvarstatus("ALIVE_TEXT") or "**سورس زد إي يعمل بنجاح**"
    JMTHON_IMG = gvarstatus("ALIVE_PIC")
    caption = jmthon_caption.format(
        ALIVE_TEXT=ALIVE_TEXT,
        ANIME=ANIME,
        EMOJI=EMOJI,
        mention=mention,
        uptime=uptime,
        telever=version.__version__,
        jmver=jmthonversion,
        pyver=python_version(),
        dbhealth=check_sgnirts,
        ping=ms,
    )
    if JMTHON_IMG:
        JMTHON = list(JMTHON_IMG.split())
        PIC = random.choice(JMTHON)
        try:
            await event.client.send_file(
                event.chat_id, PIC, caption=caption, reply_to=reply_to_id
            )
            await jmthonevent.delete()
        except (WebpageMediaEmptyError, MediaEmptyError, WebpageCurlFailedError):
            return await edit_or_reply(
                jmthonevent,
                f"**رابط الصورة غير صحيح**\nعليك الرد على رابط الصورة ب .اضف صورة الفحص",
            )
    else:
        await edit_or_reply(
            jmthonevent,
            caption,
        )


temp = """{ALIVE_TEXT}
**{EMOJI} قاعدة البيانات :** `{dbhealth}`
**{EMOJI} اصدار التيليثون:** `{telever}`
**{EMOJI} اصدار زد إي :** `{jmver}`
**{EMOJI} اصدار البايثون :** `{pyver}`
**{EMOJI} الوقت :** `{uptime}`
**{EMOJI} المالك:** {mention}"""


def jmthonalive_text():
    EMOJI = gvarstatus("ALIVE_EMOJI") or "  ✥ "
    jmthon_caption = "**سورس زد إي يعمل بنجاح**\n"
    jmthon_caption += f"**{EMOJI} اصدار التيليثون :** `{version.__version__}\n`"
    jmthon_caption += f"**{EMOJI} اصدار زد إي :** `{jmthonversion}`\n"
    jmthon_caption += f"**{EMOJI} اصدار البايثون :** `{python_version()}\n`"
    jmthon_caption += f"**{EMOJI} المالك:** {mention}\n"
    return jmthon_caption


@ZE.ar_cmd(pattern="السورس$")
async def repo(event):
    RR7PP = Config.TG_BOT_USERNAME
    if event.reply_to_msg_id:
        await event.get_reply_message()
    response = await ZE.inline_query(RR7PP, "السورس")
    await response[0].click(event.chat_id)
    await event.delete()


ROZ_PIC = "https://telegra.ph/file/39ef559d36cdb76d47b6e.jpg"
RAZAN = Config.TG_BOT_USERNAME
ROZ_T = (
    f"**⌯︙بوت زد إي يعمل بنجاح 🤍،**\n"
    f"**   - اصدار التليثون :** `1.23.0\n`"
    f"**   - اصدار زد إي :** `4.0.0`\n"
    f"**   - البوت المستخدم :** `{RAZAN}`\n"
    f"**   - اصدار البايثون :** `3.9.6\n`"
    f"**   - المستخدم :** {mention}\n"
)

if Config.TG_BOT_USERNAME is not None and tgbot is not None:

    @tgbot.on(events.InlineQuery)
    async def inline_handler(event):
        builder = event.builder
        result = None
        query = event.text
        await ZE.get_me()
        if query.startswith("السورس") and event.query.user_id == ZE.uid:
            buttons = [
                [
                    Button.url("قنـاة السـورس ⚙️", "https://t.me/UI_XB"),
                    Button.url("مطور السورس 👨🏼‍💻", "https://t.me/UP_UO"),
                ]
            ]
            if ROZ_PIC and ROZ_PIC.endswith((".jpg", ".png", "gif", "mp4")):
                result = builder.photo(
                    ROZ_PIC, text=ROZ_T, buttons=buttons, link_preview=False
                )
            elif ROZ_PIC:
                result = builder.document(
                    ROZ_PIC,
                    title="ZE - USERBOT",
                    text=ROZ_T,
                    buttons=buttons,
                    link_preview=False,
                )
            else:
                result = builder.article(
                    title="ZE - USERBOT",
                    text=ROZ_T,
                    buttons=buttons,
                    link_preview=False,
                )
            await event.answer([result] if result else None)


# edit by ~ @UP_UO
