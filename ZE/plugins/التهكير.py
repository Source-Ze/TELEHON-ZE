import asyncio

from ZE import ZE

from ..core.managers import edit_or_reply
from ..helpers.utils import _format
from . import ALIVE_NAME


@ZE.ar_cmd(pattern="تهكير$")
async def _(event):
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        idd = reply_message.sender_id
        if idd == 5650717789:
            await edit_or_reply(event, "هذا مطوري\nلا يمكنني اختراق حساب مطوري")
        else:
            event = await edit_or_reply(event, "- يتم التهكير انتظر قليلا")
            animation_chars = [
                "يتم الربط بالسيرفرات الخاصة بالاختراق ",
                "تم تحديد الضحيه بنجاح",
                "جار الاختراق... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ ",
                "جار الاختراق... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ ",
                "جار الاختراق... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ ",
                "جار الاختراق... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ ",
                "جار الاختراق... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ ",
                "جار الاختراق... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ ",
                "جار الاختراق... 84%\n█████████████████████▒▒▒▒ ",
                "جار الاختراق... 100%\n████████████████████████ ",
                f"حساب الضحيه تم اختراقه بنجاح...\n\nادفع 69$ الى  {ALIVE_NAME} . لحذف هذا التهكير",
            ]
            animation_interval = 3
            animation_ttl = range(11)
            for i in animation_ttl:
                await asyncio.sleep(animation_interval)
                await event.edit(animation_chars[i % 11])
    else:
        await edit_or_reply(
            event,
            "لم يتم التعرف المستخدم \nلا يمكنني اختراق الحساب ",
            parse_mode=_format.parse_pre,
        )


@ZE.ar_cmd(pattern="تهكير2$")
async def _(event):
    animation_interval = 2
    animation_ttl = range(12)
    event = await edit_or_reply(event, "يتم التهكير النوع الثاني ")
    animation_chars = [
        "**يتم الربط بقاعده بيانات التلجرام**",
        f"تم تحديد الضحيه من قبل: {ALIVE_NAME}",
        "جار الاختراق... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ \n\n\n  الترمنال:\nيتم تحميل: \n  Bruteforce-Telegram-0.1.tar.gz (9.3 kB)",
        "جار الاختراق... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ \n\n\n  الترمنال:\nيتم تحميل: \n  Bruteforce-Telegram-0.1.tar.gz (9.3 kB)\nيتم تجميع حزمه البيانات ",
        "جار الاختراق... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ \n\n\n  الترمنال:\nيتم تحميل: \n  Bruteforce-Telegram-0.1.tar.gz (9.3 kB)\nيتم تجميع حزمه البيانات \n  يتم تحميل \n Telegram-Data-Sniffer-7.1.1-py2.py3-none-any.whl (82 kB)",
        "جار الاختراق... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ \n\n\n  الترمنال:\nيتم تحميل: \n  Bruteforce-Telegram-0.1.tar.gz (9.3 kB)\nيتم تجميع حزمه البيانات \n  يتم تحميل \n Telegram-Data-Sniffer-7.1.1-py2.py3-none-any.whl (82 kB)\n Tg-Bruteforcing (setup.py): تم الانتهاء مع عمليه 'النجاح' ",
        "جار الاختراق... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ \n\n\n  الترمنال:\nيتم تحميل: \n  Bruteforce-Telegram-0.1.tar.gz (9.3 kB)\nيتم تجميع حزمه البيانات \n  يتم تحميل \n Telegram-Data-Sniffer-7.1.1-py2.py3-none-any.whl (82 kB)\nيتم التصنيع لـ \n Tg-Bruteforcing (setup.py):\n تم الانتهاء مع عمليه 'النجاح'\nجار الانشاء للتلجرام ملف:\n filename=Telegram-Data-Sniffer-0.0.1-py3-none-any.whl size=1306 sha256=cb224caad7fe01a6649188c62303cd4697c1869fa12d280570bb6ac6a88e6b7e",
        "جار الاختراق... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ \n\n\n  الترمنال:\nيتم تحميل: \n  Bruteforce-Telegram-0.1.tar.gz (9.3 kB)\nيتم تجميع حزمه البيانات \n  يتم تحميل \n Telegram-Data-Sniffer-7.1.1-py2.py3-none-any.whl (82 kB)\nيتم التصنيع لـ Tg-Bruteforcing (setup.py):\n تم الانتهاء مع عمليه 'النجاح'\nجار الانشاء للتلجرام ملف:\n filename=Telegram-Data-Sniffer-0.0.1-py3-none-any.whl size=1306 sha256=cb224caad7fe01a6649188c62303cd4697c1869fa12d280570bb6ac6a88e6b7e\n  يتم الحفظ في الجهاز:\n /app/.cache/pip/wheels/a2/9f/b5/650dd4d533f0a17ca30cc11120b176643d27e0e1f5c9876b5b",
        "جار الاختراق... 84%\n█████████████████████▒▒▒▒ \n\n\n  الترمنال:\nيتم تحميل: \n  Bruteforce-Telegram-0.1.tar.gz (9.3 kB)\nيتم تجميع حزمه البيانات \n  يتم تحميل \n Telegram-Data-Sniffer-7.1.1-py2.py3-none-any.whl (82 kB)\nيتم التصنيع لـ\n Tg-Bruteforcing (setup.py):\n تم الانتهاء مع عمليه 'النجاح'\nجار الانشاء للتلجرام ملف:\n filename=Telegram-Data-Sniffer-0.0.1-py3-none-any.whl size=1306 sha256=cb224caad7fe01a6649188c62303cd4697c1869fa12d280570bb6ac6a88e6b7e\n  يتم الحفظ في الجهاز:\n /app/.cache/pip/wheels/a2/9f/b5/650dd4d533f0a17ca30cc11120b176643d27e0e1f5c9876b5b\n\n **تم بنجاح اختراق قاعده بيانات التلجرام**",
        "جار الاختراق... 100%\n█████████تم الاختراق ███████████ \n\n\n  الترمنال:\nيتم تحميل\n  Bruteforce-Telegram-0.1.tar.gz (9.3 kB)\nيتم تجميع حزمه البيانات \n  يتم تحميل \n Telegram-Data-Sniffer-7.1.1-py2.py3-none-any.whl (82 kB)\nيتم التصنيع لـ\n Tg-Bruteforcing (setup.py):\n تم الانتهاء مع عمليه 'النجاح'\nجار الانشاء للتلجرام ملف:\n filename=Telegram-Data-Sniffer-0.0.1-py3-none-any.whl size=1306 sha256=cb224caad7fe01a6649188c62303cd4697c1869fa12d280570bb6ac6a88e6b7e\n  يتم الحفظ في الجهاز:\n /app/.cache/pip/wheels/a2/9f/b5/650dd4d533f0a17ca30cc11120b176643d27e0e1f5c9876b5b\n\n **تم بنجاح اختراق قاعده بيانات التلجرام**\n\n\n🔹يتم جميع البيانات...",
        f"حساب الضحيه تم اختراقه...\n\nادفع 699$ الى {ALIVE_NAME} . لحذف هذا الاختراق \n\n\n  الترمنال:\nيتم تحميل:\n  Bruteforce-Telegram-0.1.tar.gz (9.3 kB)\nيتم تجميع حزمه البيانات \n  يتم تحميل  Telegram-Data-Sniffer-7.1.1-py2.py3-none-any.whl (82 kB)\nيتم التصنيع لـ \n Tg-Bruteforcing (setup.py):\n تم الانتهاء مع عمليه 'النجاح'\nجار الانشاء للتلجرام ملف:\n filename=Telegram-Data-Sniffer-0.0.1-py3-none-any.whl size=1306 sha256=cb224caad7fe01a6649188c62303cd4697c1869fa12d280570bb6ac6a88e6b7e\n  يتم الحفظ في الجهاز:\n /app/.cache/pip/wheels/a2/9f/b5/650dd4d533f0a17ca30cc11120b176643d27e0e1f5c9876b5b\n\n **تم بنجاح اختراق قاعده بيانات التلجرام**\n\n\n🔹**تم حفظ البيانات**",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 11])


@ZE.ar_cmd(pattern="تهكير3$")
async def _(event):
    animation_interval = 2
    animation_ttl = range(15)
    event = await edit_or_reply(event, "**- يتم التهكير انتظر**")
    animation_chars = [
        "- يتم البحث على قاعده بيانات المستخدم ...",
        "حاله المستخدم: متصل\nصلاحيات التلجرام: موجوده\nخصوصيه التخزين: موجوده ",
        "جار الاختراق... 0%\n[░░░░░░░░░░░░░░░░░░░░]\nيتم البحث عن المعلومات...\nETA: 0m, 30s",
        "جار الاختراق... 11.07%\n[██░░░░░░░░░░░░░░░░░░]\nيتم البحث عن المعلومات...\nETA: 0m, 27s",
        "جار الاختراق... 20.63%\n[███░░░░░░░░░░░░░░░░░]\nتم ايجاد الملف  \nC:/WhatsApp\nETA: 0m, 24s",
        "جار الاختراق... 34.42%\n[█████░░░░░░░░░░░░░░░]\nتم ايجاد الملف  \nC:/WhatsApp\nETA: 0m, 21s",
        "جار الاختراق... 42.17%\n[███████░░░░░░░░░░░░░]\nيتم البحث في قاعده البيانات \nETA: 0m, 18s",
        "جار الاختراق... 55.30%\n[█████████░░░░░░░░░░░]\nmsgstore.db.crypt12\nETA: 0m, 15s",
        "جار الاختراق... 64.86%\n[███████████░░░░░░░░░]\nmsgstore.db.crypt12\nETA: 0m, 12s",
        "جار الاختراق... 74.02%\n[█████████████░░░░░░░]\nيتم فك التشفير...\nETA: 0m, 09s",
        "جار الاختراق... 86.21%\n[███████████████░░░░░]\nيتم فك التشفير...\nETA: 0m, 06s",
        "جار الاختراق... 93.50%\n[█████████████████░░░]\nتم فك التشفير بنجاح!\nETA: 0m, 03s",
        "جار الاختراق... 100%\n[████████████████████]\nيتم البحث عن الملف...\nETA: 0m, 00s",
        "تم انتهاء الاختراق بنجاح !\nيتم رفع المعلومات...",
        "- حساب الضحيه تم اختراقه بنجاح ...!\n\n ✅ جميع بياناته تم رفعها الى السيرفر .\nحاله قاعده البيانات:\n./DOWNLOADS/msgstore.db.crypt12",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 15])
