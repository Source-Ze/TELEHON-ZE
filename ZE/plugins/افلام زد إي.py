#الملف بحقوق سورس زد إي @UI_XB
#تم انشاء الملف بواسطة @UP_UO 
import asyncio
import os
from secrets import choice
import random
from urllib.parse import quote_plus
from collections import deque
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.types import InputMessagesFilterVideo

from ZE import ZE

from ZE.core.logger import logging
from ..Config import Config
from ..core.managers import edit_delete, edit_or_reply
from . import ALIVE_NAME, mention
from ..helpers import get_user_from_event
from ..helpers.utils import _format

from . import reply_id

@ZE.on(admin_cmd(outgoing=True, pattern="بيت الروبي$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/61"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙ فيلم بيت الروبي 2023\n⎊︙ BY : @UI_XB 🎬",parse_mode="html")
  await Video.delete()


@ZE.on(admin_cmd(outgoing=True, pattern="تاج$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/62"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙ فيلم تاج 2023\n⎊︙ BY : @UI_XB 🎬",parse_mode="html")
  await Video.delete()


@ZE.on(admin_cmd(outgoing=True, pattern="مستر اكس$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/63"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙ فيلم مستر اكس 2023\n⎊︙ BY : @UI_XB 🎬",parse_mode="html")
  await Video.delete()


@ZE.on(admin_cmd(outgoing=True, pattern="البعبع$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/64"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙ فيلم البعبع 2023\n⎊︙ BY : @UI_XB 🎬",parse_mode="html")
  await Video.delete()


@ZE.on(admin_cmd(outgoing=True, pattern="يوم 13$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/65"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙ فيلم يوم 13\n⎊︙ BY : @UI_XB 🎬",parse_mode="html")
  await Video.delete()


@ZE.on(admin_cmd(outgoing=True, pattern="شوجر دادي$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/66"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙ فيلم شوجر دادي\n⎊︙ BY : @UI_XB 🎬",parse_mode="html")
  await Video.delete()


@ZE.on(admin_cmd(outgoing=True, pattern="هارلي$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/3"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙ فيلم هارلي 2023 بجودة 360p \n⎊︙ BY : @UI_XB 🎬",parse_mode="html")
  await Video.delete()


@ZE.on(admin_cmd(outgoing=True, pattern="تحت تهديد السلاح$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/4"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙فيلم تحت تهديد السلاح 2023_ #360p \n⎊︙ BY : @UI_XB 🎬",parse_mode="html")
  await Video.delete()


@ZE.on(admin_cmd(outgoing=True, pattern="ولا غلطة$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/5"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙فيلم ولا غلطة 2023- #360p \n⎊︙ BY : @UI_XB 🎬",parse_mode="html")
  await Video.delete()


@ZE.on(admin_cmd(outgoing=True, pattern="خطة مازنجر$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/6"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙ فيلم خطة مازنجر hd ️: #360p 2023  \n⎊︙ BY : @UI_XB 🎬",parse_mode="html")
  await Video.delete()


@ZE.on(admin_cmd(outgoing=True, pattern="هاشتاج جوزني$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/7"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙فيلم #هاشتاج جوزني 2023- #360p \n⎊︙ BY : @UI_XB 🎬",parse_mode="html")
  await Video.delete()


@ZE.on(admin_cmd(outgoing=True, pattern="بعد الشر$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/8"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙فيلم بعد الشر 2023 | #360p \n⎊︙ BY : @UI_XB 🎬",parse_mode="html")
  await Video.delete()


@ZE.on(admin_cmd(outgoing=True, pattern="أبن الحج احمد$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/9"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙فيلم أبن الحج احمد نسخه اوضح 2023 \n⎊︙ BY : @UI_XB 🎬",parse_mode="html")
  await Video.delete()


@ZE.on(admin_cmd(outgoing=True, pattern="رمسيس باريس$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/10"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙فيلم رمسيس باريس 2023 جودة عالية \n⎊︙ BY : @UI_XB 🎬",parse_mode="html")
  await Video.delete()


@ZE.on(admin_cmd(outgoing=True, pattern="جروب الماميز$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/11"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙ 📽| جروب الماميز (2023)  360p \n⎊︙ BY : @UI_XB 🎬",parse_mode="html")
  await Video.delete()


@ZE.on(admin_cmd(outgoing=True, pattern="العنكبوت$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/12"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙العنكبوت 2022 بجودة # #FHD \n⎊︙ BY : @UI_XB 🎬",parse_mode="html")
  await Video.delete()


@ZE.on(admin_cmd(outgoing=True, pattern="اشباح اوروبا$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/13"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙فيلم اشباح اوروبا 2022 (360p) \n⎊︙ BY : @UI_XB 🎬",parse_mode="html")
  await Video.delete()


@ZE.on(admin_cmd(outgoing=True, pattern="كيرة و الجن$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/14"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙فلم كيرة و الجن 2022 جوده #360p \n⎊︙ BY : @UI_XB 🎬",parse_mode="html")
  await Video.delete()


@ZE.on(admin_cmd(outgoing=True, pattern="بحبك$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/15"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙فيلم : بحبك 2022  بجودة : #360p  \n⎊︙ BY : @UI_XB 🎬",parse_mode="html")
  await Video.delete()


@ZE.on(admin_cmd(outgoing=True, pattern="موسى$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/16"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙ فيلم موسى بجودة #1080HD #شاشةكاملة  \n⎊︙ BY : @UI_XB 🎬",parse_mode="html")
  await Video.delete()


@ZE.on(admin_cmd(outgoing=True, pattern="عمهم$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/17"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙فيلم #عمهم 2022  #360p  \n⎊︙ BY : @UI_XB 🎬",parse_mode="html")
  await Video.delete()


@ZE.on(admin_cmd(outgoing=True, pattern="الجريمة$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/18"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙فيلم : الجريمة 2022 بجودة : #360p  \n⎊︙ BY : @UI_XB 🎬",parse_mode="html")
  await Video.delete()


@ZE.on(admin_cmd(outgoing=True, pattern="العارف$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/19"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙فيلم العارف (2021) #360p بجودة  \n⎊︙ BY : @UI_XB 🎬",parse_mode="html")
  await Video.delete()


@ZE.on(admin_cmd(outgoing=True, pattern="نبيل الجميل اخصائى تجميل$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/20"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙ فيلم نبيل الجميل اخصائى تجميل [2023] \n⎊︙ BY : @UI_XB 🎬",parse_mode="html")
  await Video.delete()


@ZE.on(admin_cmd(outgoing=True, pattern="الفيل الازرق1$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/21"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙الفيلم الرائع الفيل الازرق 1 كامل الجودة HD \n⎊︙ BY : @UI_XB 🎬",parse_mode="html")
  await Video.delete()


@ZE.on(admin_cmd(outgoing=True, pattern="اخي فوق الشجرة$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/22"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙ فلم أخي فوق الشجرة | 2023 \n⎊︙ BY : @UI_XB 🎬",parse_mode="html")
  await Video.delete()


@ZE.on(admin_cmd(outgoing=True, pattern="احمد نوتردام$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/23"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙ فيلم احمد نوتردام نسخة (FHD) جودة #480p \n⎊︙ BY : @UI_XB 🎬",parse_mode="html")
  await Video.delete()


@ZE.on(admin_cmd(outgoing=True, pattern="محمد حسين$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/24"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙ فيلم محمد حسين - HD \n⎊︙ BY : @UI_XB 🎬",parse_mode="html")
  await Video.delete()


@ZE.on(admin_cmd(outgoing=True, pattern="مسرح مصر1$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/25"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙ مسرح مصر - الحلقة الاولي- موسم 3 ( كواليس الكواليس ) \n⎊︙ BY : @UI_XB 🎬",parse_mode="html")
  await Video.delete()


@ZE.on(admin_cmd(outgoing=True, pattern="مسرح مصر2$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/26"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙مسرح مصر - الحلقة الثانية - موسم 3 ( شوكت وشاطوفني )  \n⎊︙ BY : @UI_XB 🎬",parse_mode="html")
  await Video.delete()


@ZE.on(admin_cmd(outgoing=True, pattern="مسرح مصر3$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/27"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙مسرح مصر - الحلقة الثالثة - موسم 3 ( فرحة )  \n⎊︙ BY : @UI_XB 🎬",parse_mode="html")
  await Video.delete()


@ZE.on(admin_cmd(outgoing=True, pattern="مسرح مصر4$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/28"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙مسرح مصر - الحلقة الرابعة - موسم 3 ( عودة ضرغام )  \n⎊︙ BY : @UI_XB 🎬",parse_mode="html")
  await Video.delete()


@ZE.on(admin_cmd(outgoing=True, pattern="مسرح مصر5$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/29"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙مسرح مصر - الحلقة الخامسة - موسم 3 ( زي كل مرة )  \n⎊︙ BY : @UI_XB 🎬",parse_mode="html")
  await Video.delete()


@ZE.on(admin_cmd(outgoing=True, pattern="مسرح مصر6$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/30"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙مسرح مصر - الحلقة السادسة - موسم 3 ( المؤلف )  \n⎊︙ BY : @UI_XB 🎬",parse_mode="html")
  await Video.delete()


@ZE.on(admin_cmd(outgoing=True, pattern="مسرح مصر7$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/31"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙مسرح مصر - الحلقة السابعة - موسم 3 ( عملية تجميل )  \n⎊︙ BY : @UI_XB 🎬",parse_mode="html")
  await Video.delete()


@ZE.on(admin_cmd(outgoing=True, pattern="مسرح مصر8$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/32"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙مسرح مصر - الحلقة الثامنة - موسم 3 ( زي الفل )  \n⎊︙ BY : @UI_XB 🎬",parse_mode="html")
  await Video.delete()


@ZE.on(admin_cmd(outgoing=True, pattern="مسرح مصر9$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/33"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙مسرح مصر - الحلقة التاسعة - موسم 3 ( ورينا القوة ) \n⎊︙ BY : @UI_XB 🎬",parse_mode="html")
  await Video.delete()


@ZE.on(admin_cmd(outgoing=True, pattern="مسرح مصر10$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/34"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙مسرح مصر - الحلقة العاشرة - موسم 3 ( المتحولون ) \n⎊︙ BY : @UI_XB 🎬",parse_mode="html")
  await Video.delete()


@ZE.on(admin_cmd(outgoing=True, pattern="مسرح مصر11$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/35"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙مسرح مصر - الحلقة الحادية عشر - موسم 3 ( ال كابوني \n⎊︙ BY : @UI_XB 🎬",parse_mode="html")
  await Video.delete()


@ZE.on(admin_cmd(outgoing=True, pattern="مسرح مصر12$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/36"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙مسرح مصر - الحلقة الثانية عشر - موسم 3 ( من عشرين سنة ) \n⎊︙ BY : @UI_XB 🎬",parse_mode="html")
  await Video.delete()


@ZE.on(admin_cmd(outgoing=True, pattern="مسرح مصر13$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/37"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙مسرح مصر - الحلقة الثالثة عشر - موسم 3 ( قرب قرب ) \n⎊︙ BY : @UI_XB 🎬",parse_mode="html")
  await Video.delete()


@ZE.on(admin_cmd(outgoing=True, pattern="مسرح مصر14$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/38"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙مسرح مصر - الحلقة الرابعة عشر - موسم 3 ( حاجة مهمة جدا ) \n⎊︙ BY : @UI_XB 🎬",parse_mode="html")
  await Video.delete()


@ZE.on(admin_cmd(outgoing=True, pattern="مسرح مصر15$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/39"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙مسرح مصر - الحلقة الخامسة عشر - موسم 3 ( اوبرا فايزة ) \n⎊︙ BY : @UI_XB 🎬",parse_mode="html")
  await Video.delete()


@ZE.on(admin_cmd(outgoing=True, pattern="مسرح مصر16$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/40"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙مسرح مصر - الحلقة السادسة عشر - موسم 3 ( عصابة في المول ) \n⎊︙ BY : @UI_XB 🎬",parse_mode="html")
  await Video.delete()


@ZE.on(admin_cmd(outgoing=True, pattern="مسرح مصر17$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/41"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙مسرح مصر - الحلقة السابعة عشر - موسم 3 ( كلام كبار ) \n⎊︙ BY : @UI_XB 🎬",parse_mode="html")
  await Video.delete()


@ZE.on(admin_cmd(outgoing=True, pattern="مسرح مصر18$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/42"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙مسرح مصر - الحلقة الثامنة عشر - موسم 3 ( ضربة جزاء ) \n⎊︙ BY : @UI_XB 🎬",parse_mode="html")
  await Video.delete()


@ZE.on(admin_cmd(outgoing=True, pattern="مسرح مصر19$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/43"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙مسرح مصر - الحلقة التاسعة عشر - موسم 3 ( راس السنة \n⎊︙ BY : @UI_XB 🎬",parse_mode="html")
  await Video.delete()


@ZE.on(admin_cmd(outgoing=True, pattern="مسرح مصر20$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/44"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙مسرح مصر - الحلقة العشرون - موسم 3 ( رجالة بلدنا ) \n⎊︙ BY : @UI_XB 🎬",parse_mode="html")
  await Video.delete()


@ZE.on(admin_cmd(outgoing=True, pattern="مسرح مصر21$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/45"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙مسرح مصر - الحلقة الواحدة والعشرون - موسم 3 ( الخاتم ) \n⎊︙ BY : @UI_XB 🎬",parse_mode="html")
  await Video.delete()


@ZE.on(admin_cmd(outgoing=True, pattern="مسرح مصر22$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/46"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙مسرح مصر - الحلقة الثانية والعشرون - موسم 3 ( رايح جاي ) \n⎊︙ BY : @UI_XB 🎬",parse_mode="html")
  await Video.delete()


@ZE.on(admin_cmd(outgoing=True, pattern="الواد سيد الشغال$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/47"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙مسرحية الواد سيد الشغال كاملة اونلاين🎭 \n⎊︙ BY : @UI_XB 🎬",parse_mode="html")
  await Video.delete()


@ZE.on(admin_cmd(outgoing=True, pattern="اخويا هايص وانا لايص$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/48"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙مسرحية اخويا هايص وانا لايص كاملة \n⎊︙ BY : @UI_XB 🎬",parse_mode="html")
  await Video.delete()


@ZE.on(admin_cmd(outgoing=True, pattern="سك على بناتك$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/49"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙ مسرحيه سك على بناتك كاملة اون لاين 🎭\n⎊︙ BY : @UI_XB 🎬",parse_mode="html")
  await Video.delete()


@ZE.on(admin_cmd(outgoing=True, pattern="المتزوجون$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/50"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙ مسرحيه المتزوجون كاملة اون لاين 🎭\n⎊︙ BY : @UI_XB 🎬",parse_mode="html")
  await Video.delete()


@ZE.on(admin_cmd(outgoing=True, pattern="العيال كبرت$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/51"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙ مسرحية العيال كبرت كاملة اون لاين HD\n⎊︙ BY : @UI_XB 🎬",parse_mode="html")
  await Video.delete()


@ZE.on(admin_cmd(outgoing=True, pattern="مدرسة المشاغبين$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/52"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙ مسرحية مدرسة المشاغبين كاملة اون لاين HD\n⎊︙ BY : @UI_XB 🎬",parse_mode="html")
  await Video.delete()


@ZE.on(admin_cmd(outgoing=True, pattern="وجهة نظر$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/53"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙ مسرحية وجهة نظر كاملة اونلاين HD\n⎊︙ BY : @UI_XB 🎬",parse_mode="html")
  await Video.delete()


@ZE.on(admin_cmd(outgoing=True, pattern="حزمنى يا$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/54"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙ مسرحية حزمنى يا كاملة اون لاين HD\n⎊︙ BY : @UI_XB 🎬",parse_mode="html")
  await Video.delete()


@ZE.on(admin_cmd(outgoing=True, pattern="المرجيحة$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/55"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙ مسرح امين وشركاه مسرحيه المرجيحة\n⎊︙ BY : @UI_XB 🎬",parse_mode="html")
  await Video.delete()


@ZE.on(admin_cmd(outgoing=True, pattern="مدرسة المشاغبين بالالوان$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/57"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙ مدرسة المشاغبين بالألوان بجودة #360p\n⎊︙ BY : @UI_XB 🎬",parse_mode="html")
  await Video.delete()


@ZE.on(admin_cmd(outgoing=True, pattern="بودي جارد$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/60"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙ مسرحية بودي جارد (1999) | بجودة #480p\n⎊︙ BY : @UI_XB 🎬",parse_mode="html")
  await Video.delete()


@ZE.on(admin_cmd(outgoing=True, pattern="Avatar The Way of Water$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/101"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙ Avatar: The Way of Water 2022\n⎊︙ BY : @UI_XB 🎬",parse_mode="html")
  await Video.delete()


@ZE.on(admin_cmd(outgoing=True, pattern="Dinosaur world$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/102"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙ Dinosaur world\n⎊︙ BY : @UI_XB 🎬",parse_mode="html")
  await Video.delete()


@ZE.on(admin_cmd(outgoing=True, pattern="The Tomorrow Job$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/103"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙ The.Tomorrow.Job.2023.360p\n⎊︙ BY : @UI_XB 🎬",parse_mode="html")
  await Video.delete()


@ZE.on(admin_cmd(outgoing=True, pattern="Pillow Party Massacre$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/104"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙ Pillow.Party.Massacre.2023.360p\n⎊︙ BY : @UI_XB 🎬",parse_mode="html")
  await Video.delete()


@ZE.on(admin_cmd(outgoing=True, pattern="From Black$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/105"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙ From.Black.2023.360p\n⎊︙ BY : @UI_XB 🎬",parse_mode="html")
  await Video.delete()


@ZE.on(admin_cmd(outgoing=True, pattern="Clock$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/106"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙ Clock.2023.360p\n⎊︙ BY : @UI_XB 🎬",parse_mode="html")
  await Video.delete()


@ZE.on(admin_cmd(outgoing=True, pattern="Aka$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/107"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙ Aka.2023.360p\n⎊︙ BY : @UI_XB 🎬",parse_mode="html")
  await Video.delete()


@ZE.on(admin_cmd(outgoing=True, pattern="The Fearway$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/108"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙ The.Fearway.2023.360p.BluRay\n⎊︙ BY : @UI_XB 🎬",parse_mode="html")
  await Video.delete()


@ZE.on(admin_cmd(outgoing=True, pattern="Breakout$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/109"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙ Breakout [2023]\n⎊︙ BY : @UI_XB 🎬",parse_mode="html")
  await Video.delete()


@ZE.on(admin_cmd(outgoing=True, pattern="Jesus Revolution$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/110"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙ Jesus Revolution [2023]\n⎊︙ BY : @UI_XB 🎬",parse_mode="html")
  await Video.delete()


@ZE.on(admin_cmd(outgoing=True, pattern="Dungeons Dragons$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/111"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙ Dungeons & Dragons: Honor Among Thieves [2023]\n⎊︙ BY : @UI_XB 🎬",parse_mode="html")
  await Video.delete()


@ZE.on(admin_cmd(outgoing=True, pattern="The Best Man$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/112"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙ The.Best.Man.2023\n⎊︙ BY : @UI_XB 🎬",parse_mode="html")
  await Video.delete()


@ZE.on(admin_cmd(outgoing=True, pattern="The Irish Mob$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/113"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙ The.Irish.Mob.2023\n⎊︙ BY : @UI_XB 🎬",parse_mode="html")
  await Video.delete()


@ZE.on(admin_cmd(outgoing=True, pattern="Sisu$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/114"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙ Sisu.2022\n⎊︙ BY : @UI_XB 🎬",parse_mode="html")
  await Video.delete()


@ZE.on(admin_cmd(outgoing=True, pattern="Maid For Revenge$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/115"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙ Maid.For.Revenge.2023\n⎊︙ BY : @UI_XB 🎬",parse_mode="html")
  await Video.delete()


@ZE.on(admin_cmd(outgoing=True, pattern="Polite Society$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/116"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙ Polite.Society.2023\n⎊︙ BY : @UI_XB 🎬",parse_mode="html")
  await Video.delete()


@ZE.on(admin_cmd(outgoing=True, pattern="Homestead$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/117"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙ Homestead.2023\n⎊︙ BY : @UI_XB 🎬",parse_mode="html")
  await Video.delete()


@ZE.on(admin_cmd(outgoing=True, pattern="bull shark$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/118"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙ bull.shark.2022\n⎊︙ BY : @UI_XB 🎬",parse_mode="html")
  await Video.delete()


@ZE.on(admin_cmd(outgoing=True, pattern="Tin and Tina$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/119"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙ Tin and Tina 2023\n⎊︙ BY : @UI_XB 🎬",parse_mode="html")
  await Video.delete()


@ZE.on(admin_cmd(outgoing=True, pattern="Evil dead risev$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/120"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙ Evil dead rise 2023\n⎊︙ BY : @UI_XB 🎬",parse_mode="html")
  await Video.delete()


@ZE.on(admin_cmd(outgoing=True, pattern="Iron Man1$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/68"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙ Iron.Man.2008.BluRay.720p\n⎊︙ BY : @UI_XB 🎬",parse_mode="html")
  await Video.delete()


@ZE.on(admin_cmd(outgoing=True, pattern="Iron Man2$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/69"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙ .Iron.Man.2.2010.BluRay.720p \n⎊︙ BY : @UI_XB 🎬",parse_mode="html")
  await Video.delete()


@ZE.on(admin_cmd(outgoing=True, pattern="Iron Man3$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/70"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙ Iron Man Three (2013)\n⎊︙ BY : @UI_XB 🎬",parse_mode="html")
  await Video.delete()


@ZE.on(admin_cmd(outgoing=True, pattern="Spider man1$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/71"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙ Spider-man [2002] الجزء الأول\n⎊︙ BY : @UI_XB 🎬",parse_mode="html")
  await Video.delete()


@ZE.on(admin_cmd(outgoing=True, pattern="Spider man2$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/72"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙ Spider-Man 2 [2004] الجزء الثانى\n⎊︙ BY : @UI_XB 🎬",parse_mode="html")
  await Video.delete()


@ZE.on(admin_cmd(outgoing=True, pattern="Spider man3$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/73"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙ Spider-Man 3 [2007] الجزء الثالث\n⎊︙ BY : @UI_XB 🎬",parse_mode="html")
  await Video.delete()


@ZE.on(admin_cmd(outgoing=True, pattern="The Amazing Spider Man1$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/74"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙ The Amazing Spider-Man [2012]الجزء الاول\n⎊︙ BY : @UI_XB 🎬",parse_mode="html")
  await Video.delete()


@ZE.on(admin_cmd(outgoing=True, pattern="The Amazing Spider Man2$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/75"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙ The Amazing Spider-Man 2 [2014] الجزء الثانى\n⎊︙ BY : @UI_XB 🎬",parse_mode="html")
  await Video.delete()


@ZE.on(admin_cmd(outgoing=True, pattern="Venom1$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/76"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙ Venom [2018] الجزء الاول\n⎊︙ BY : @UI_XB 🎬",parse_mode="html")
  await Video.delete()


@ZE.on(admin_cmd(outgoing=True, pattern="Venom2$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/77"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙ Venom: Let There Be Carnage [2021] الجزء الثانى\n⎊︙ BY : @UI_XB 🎬",parse_mode="html")
  await Video.delete()


@ZE.on(admin_cmd(outgoing=True, pattern="Thor1$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/78"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙ Thor 2011\n⎊︙ BY : @UI_XB 🎬",parse_mode="html")
  await Video.delete()


@ZE.on(admin_cmd(outgoing=True, pattern="Thor2$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/79"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙ Thor: The Dark World (2013)\n⎊︙ BY : @UI_XB 🎬",parse_mode="html")
  await Video.delete()


@ZE.on(admin_cmd(outgoing=True, pattern="Deadpool1$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/80"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙ Deadpool [2016] الجزء الاول\n⎊︙ BY : @UI_XB 🎬",parse_mode="html")
  await Video.delete()

@ZE.on(admin_cmd(outgoing=True, pattern="Deadpool2$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/81"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙ Deadpool 2 [2018] الجزء الثانى\n⎊︙ BY : @UI_XB 🎬",parse_mode="html")
  await Video.delete()


@ZE.on(admin_cmd(outgoing=True, pattern="Captain America1$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/82"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙ Captain America The First Avenger 2011\n⎊︙ BY : @UI_XB 🎬",parse_mode="html")
  await Video.delete()


@ZE.on(admin_cmd(outgoing=True, pattern="Captain America2$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/83"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙ Captain America: The Winter Soldier 2014\n⎊︙ BY : @UI_XB 🎬",parse_mode="html")
  await Video.delete()


@ZE.on(admin_cmd(outgoing=True, pattern="Captain America3$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/84"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙ Captain America Civil War 2016\n⎊︙ BY : @UI_XB 🎬",parse_mode="html")
  await Video.delete()


@ZE.on(admin_cmd(outgoing=True, pattern="Doctor Strange1$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/85"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙ Doctor Strange 2016\n⎊︙ BY : @UI_XB 🎬",parse_mode="html")
  await Video.delete()


@ZE.on(admin_cmd(outgoing=True, pattern="Doctor Strange2$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/86"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙ Doctor Strange in the Multiverse of Madness [2022]\n⎊︙ BY : @UI_XB 🎬",parse_mode="html")
  await Video.delete()


@ZE.on(admin_cmd(outgoing=True, pattern="Spider Man Homecoming$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/87"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙ Spider-Man: Homecoming 2017\n⎊︙ BY : @UI_XB 🎬",parse_mode="html")
  await Video.delete()


@ZE.on(admin_cmd(outgoing=True, pattern="Spider Man Far From Home$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/88"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙ Spider-Man: Far From Home 2019\n⎊︙ BY : @UI_XB 🎬",parse_mode="html")
  await Video.delete()


@ZE.on(admin_cmd(outgoing=True, pattern="Spider Man No Way Home$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/89"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙ Spider-Man: No Way Home [2022]\n⎊︙ BY : @UI_XB 🎬",parse_mode="html")
  await Video.delete()


@ZE.on(admin_cmd(outgoing=True, pattern="Black panther1$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/90"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙ Black panther 2018\n⎊︙ BY : @UI_XB 🎬",parse_mode="html")
  await Video.delete()


@ZE.on(admin_cmd(outgoing=True, pattern="Black panther2$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/91"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙ Black Panther: Wakanda Forever [2022]\n⎊︙ BY : @UI_XB 🎬",parse_mode="html")
  await Video.delete()


@ZE.on(admin_cmd(outgoing=True, pattern="Avengers Infinity War$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/93"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙ Avengers Infinity War 2018\n⎊︙ BY : @UI_XB 🎬",parse_mode="html")
  await Video.delete()


@ZE.on(admin_cmd(outgoing=True, pattern="Avengers Endgame$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/94"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙ Avengers: Endgame 2019\n⎊︙ BY : @UI_XB 🎬",parse_mode="html")
  await Video.delete()


@ZE.on(admin_cmd(outgoing=True, pattern="Ant Man1$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/95"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙ Ant-Man 2015\n⎊︙ BY : @UI_XB 🎬",parse_mode="html")
  await Video.delete()


@ZE.on(admin_cmd(outgoing=True, pattern="Ant Man2$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/96"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙ Ant-Man and the Wasp 2018\n⎊︙ BY : @UI_XB 🎬",parse_mode="html")
  await Video.delete()


@ZE.on(admin_cmd(outgoing=True, pattern="Ant Man3$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/97"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙ Ant-Man and the Wasp: Quantumani [2023]\n⎊︙ BY : @UI_XB 🎬",parse_mode="html")
  await Video.delete()


@ZE.on(admin_cmd(outgoing=True, pattern="Black Widow$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/98"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙ Black Widow [2021]\n⎊︙ BY : @UI_XB 🎬",parse_mode="html")
  await Video.delete()


@ZE.on(admin_cmd(outgoing=True, pattern="Shang Chi$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/99"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙ Shang-Chi and the Legend of the Ten Rings [2021]\n⎊︙ BY : @UI_XB 🎬",parse_mode="html")
  await Video.delete()


@ZE.on(admin_cmd(outgoing=True, pattern="The Avengers$"))
async def jepvois(Video):
  url = f"https://t.me/EE_SPI/100"
  await Video.client.send_file(Video.chat_id,url,caption="⎊︙ The Avengers 2012\n⎊︙ BY : @UI_XB 🎬",parse_mode="html")
  await Video.delete()
