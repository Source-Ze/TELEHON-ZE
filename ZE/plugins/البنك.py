# ======================================================================================================================================
# ping -> edited ping with pic by  @UP_UO 
# كتابة الملف لسورس زد إي فقط ممنوع نسبه لنفسك
# تخمط دليل فشلك تخمط و قول انك مطور 😂😂

import os
from datetime import datetime

from ZE import ZE

#
from . import hmention, reply_id

PING_PIC = os.environ.get("PING_PIC") or (
    "https://telegra.ph/file/22bec9ffa06519aba18c8.jpg"
)

JM_TXT = os.environ.get("PING_TEXT") or "مـن لا يتعلم من الماضي لا يرحمه المستقبل  . 🖤"


@ZE.ar_cmd(pattern="بنك$")
async def _(event):
    reply_to_id = await reply_id(event)
    start = datetime.now()
    roz = await edit_or_reply(
        event, "<b><i>  ❤️⃝⃝⃝⃝⃝⃝⃝⃝⃝⃝⃝⃝⃝⃝⃟✨ البــــنك... 🍀⃝⃝⃟🍂 </b></i>", "html"
    )
    end = datetime.now()
    await roz.delete()
    ms = (end - start).microseconds / 1000
    if PING_PIC:
        caption = f"<b><i>{JM_TXT}<i><b>\n<code>┏━━━━━━━┓\n┃ ✦ {ms}\n┃ ✦ <b>{hmention}</b>\n┗━━━━━━━┛"
        await event.client.send_file(
            event.chat_id,
            PING_PIC,
            caption=caption,
            parse_mode="html",
            reply_to=reply_to_id,
            link_preview=False,
            allow_cache=True,
        )
    else:
        await event.edit_or_reply(
            event, "<code>يجـب اضـافة متـغير `PING_PIC`  اولا  f<code>", "html"
        )


# ======================================================================================================================================
