#الملف بحقوق سورس سبايدر @UI_XB
import asyncio
import random
from asyncio.exceptions import TimeoutError

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from ZE import ZE
from ..helpers.utils import reply_id


@ZE.on(admin_cmd(outgoing=True, pattern="ريمكس$"))
async def jepvois(vois):
  rl = random.randint(3,267)
  url = f"https://t.me/REMIXv1/{rl}"
  await vois.client.send_file(vois.chat_id,url,caption="⎊︙ BY : @UI_XB 🎧",parse_mode="html")
  await vois.delete()
