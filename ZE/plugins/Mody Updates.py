import asyncio
import os
from secrets import choice
import random
from urllib.parse import quote_plus
from collections import deque
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.types import InputMessagesFilterVoice

from ZE import ZE

from ZE.core.logger import logging
from ..Config import Config
from ..core.managers import edit_delete, edit_or_reply
from . import ALIVE_NAME, mention
from ..helpers import get_user_from_event
from ..helpers.utils import _format

from . import reply_id


@ZE.on(admin_cmd(outgoing=True, pattern="Mody Updates$"))
async def jepvois(Voice):
  url = f"https://t.me/UI_XB"
  await Voice.client.send_file(Voice.chat_id,url,caption="⎊︙ اخر تحديثات سورس زد إي \n⎊︙ BY : @UI_XB 👑",parse_mode="html")
  await Voice.delete()
