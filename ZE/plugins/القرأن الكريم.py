import asyncio
import random
from asyncio.exceptions import TimeoutError

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from WWWL5 import WWWL5
from ..helpers.utils import reply_id


@WWWL5.on(admin_cmd(outgoing=True, pattern="سوره للقارئ الشيخ محمد صديق المنشاوي$"))
async def jepvois(vois):
  rl = random.randint(1022,1134)
  url = f"https://t.me/quran1tv/{rl}"
  await vois.client.send_file(vois.chat_id,url,caption="سوره للقارئ الشيخ محمد صديق المنشاوي\n⎊︙ BY : @UI_XB 🌺",parse_mode="html")
  await vois.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="سوره للقارئ الشيخ مشاري العفاسي$"))
async def jepvois(vois):
  rl = random.randint(1266,1380)
  url = f"https://t.me/quran1tv/{rl}"
  await vois.client.send_file(vois.chat_id,url,caption="سوره للقارئ الشيخ مشاري العفاسي\n⎊︙ BY : @UI_XB 🌺",parse_mode="html")
  await vois.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="سوره للقارئ الشيخ عبدالرحمن السديس$"))
async def jepvois(vois):
  rl = random.randint(9294,9407)
  url = f"https://t.me/quran1tv/{rl}"
  await vois.client.send_file(vois.chat_id,url,caption="سوره للقارئ الشيخ عبدالرحمن السديس\n⎊︙ BY : @UI_XB 🌺",parse_mode="html")
  await vois.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="سوره للقارئ الشيخ ناصر القطامي$"))
async def jepvois(vois):
  rl = random.randint(2025,2138)
  url = f"https://t.me/quran1tv/{rl}"
  await vois.client.send_file(vois.chat_id,url,caption="سوره للقارئ الشيخ ناصر القطامي\n⎊︙ BY : @UI_XB 🌺",parse_mode="html")
  await vois.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="سوره للقارئ الشيخ احمد العجمي$"))
async def jepvois(vois):
  rl = random.randint(2629,2743)
  url = f"https://t.me/quran1tv/{rl}"
  await vois.client.send_file(vois.chat_id,url,caption="سوره للقارئ الشيخ احمد العجمي\n⎊︙ BY : @UI_XB 🌺",parse_mode="html")
  await vois.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="سوره للقارئ الطبيب احمد نعينع$"))
async def jepvois(vois):
  rl = random.randint(3792,3904)
  url = f"https://t.me/quran1tv/{rl}"
  await vois.client.send_file(vois.chat_id,url,caption="سوره للقارئ الطبيب احمد نعينع\n⎊︙ BY : @UI_XB 🌺",parse_mode="html")
  await vois.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="سوره للقارئ الشيخ عبدالباسط عبدالصمد$"))
async def jepvois(vois):
  rl = random.randint(11636,11749)
  url = f"https://t.me/quran1tv/{rl}"
  await vois.client.send_file(vois.chat_id,url,caption="سوره للقارئ الشيخ عبدالباسط عبدالصمد\n⎊︙ BY : @UI_XB 🌺",parse_mode="html")
  await vois.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="سوره للقارئ الشيخ ياسر الدوسري$"))
async def jepvois(vois):
  rl = random.randint(3410,3523)
  url = f"https://t.me/quran1tv/{rl}"
  await vois.client.send_file(vois.chat_id,url,caption="سوره للقارئ الشيخ ياسر الدوسري\n⎊︙ BY : @UI_XB 🌺",parse_mode="html")
  await vois.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="سوره للقارئ الشيخ ابراهيم الاخضر$"))
async def jepvois(vois):
  rl = random.randint(5044,5157)
  url = f"https://t.me/quran1tv/{rl}"
  await vois.client.send_file(vois.chat_id,url,caption="سوره للقارئ الشيخ ابراهيم الاخضر\n⎊︙ BY : @UI_XB 🌺",parse_mode="html")
  await vois.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="سوره للقارئ الشيخ محمد جبريل$"))
async def jepvois(vois):
  rl = random.randint(6158,6271)
  url = f"https://t.me/quran1tv/{rl}"
  await vois.client.send_file(vois.chat_id,url,caption="سوره للقارئ الشيخ محمد جبريل \n⎊︙ BY : @UI_XB 🌺",parse_mode="html")
  await vois.delete()
