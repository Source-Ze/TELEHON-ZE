import random

from ZE import ZE
from ZE.core.managers import edit_or_reply
from ZE.helpers import get_user_from_event
from razan.strings.fun import *

from . import *


@ZE.ar_cmd(pattern="رفع بقلبي(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        return await edit_or_reply(mention, f"[{custom}](tg://user?id={user.id})")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention, f"- المستخدم [{tag}](tg://user?id={user.id}) \n- تـم رفعـه بڪلبك 🖤 "
    )


@ZE.ar_cmd(pattern="رفع زوجي(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        return await edit_or_reply(mention, f"[{custom}](tg://user?id={user.id})")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention,
        f"⎊ المستخدم [{tag}](tg://user?id={user.id}) \n⎊ تـم رفعه زوجج روحوا خلفوا 😂",
    )


@ZE.ar_cmd(pattern="رفع مطي(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 5650717789:
        return await edit_or_reply(mention, f"**⎊ لا يمكنك استخدام الامر على مطور السورس**")
    if user.id == 169561:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    if user.id == 203585:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention, f"⎊ المستخدم [{tag}](tg://user?id={user.id}) \n⎊ تـم رفـعه مطي هـنا "
    )


@ZE.ar_cmd(pattern="رفع حمار(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        return await edit_or_reply(mention, f"[{custom}](tg://user?id={user.id})")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention, f"⎊ المستخدم [{tag}](tg://user?id={user.id}) \n⎊ تـم رفـعـة حـمـار 🦓 "
    )


@ZE.ar_cmd(pattern="رفع مرتي(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 5650717789:
        return await edit_or_reply(mention, f"**⎊ لا يمكنك استخدام الامر على مطور السورس**")
    if user.id == 2033585:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    if user.id == 676943:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور **")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention,
        f"⎊ المستخدم [{tag}](tg://user?id={user.id}) \n⎊ تـم رفعـه مـࢪتك مـشي نخـلف 😹🤤",
    )


@ZE.ar_cmd(pattern="رفع كلب(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 5650717789:
        return await edit_or_reply(mention, f"**⎊ لا يمكنك استخدام الامر على مطور السورس**")
    if user.id == 169561:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    if user.id == 203485:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention,
        f"⎊ المستخدم [{tag}](tg://user?id={user.id}) \n⎊ تـم رفعـه جلب خليه خله ينبح 😂🐶",
    )


@ZE.ar_cmd(pattern="كت(?: |$)(.*)")
async def mention(mention):
    reza = random.choice(kttwerz)
    await edit_or_reply(mention, f"**- {reza}**")


@ZE.ar_cmd(pattern="هينه(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 5650717789:
        return await edit_or_reply(mention, f"**⎊ لا يمكنك استخدام الامر على مطور السورس**")
    if user.id == 169561:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور **")
    if user.id == 203585:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    muh = user.first_name.replace("\u2060", "") if user.first_name else user.username
    sos = random.choice(hena)
    await edit_or_reply(mention, f"{sos} .")


@ZE.ar_cmd(pattern="نسبة الحب(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    muh = user.first_name.replace("\u2060", "") if user.first_name else user.username
    rza = random.choice(roz)
    await edit_or_reply(
        mention, f"نـسـبتكم انـت و [{muh}](tg://user?id={user.id}) هـي {rza} 😔🖤"
    )


@ZE.ar_cmd(pattern="نسبة الانوثة(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 5650717789:
        return await edit_or_reply(mention, f"**⎊ لا يمكنك استخدام الامر على مطور السورس**")
    if user.id == 169561:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور زلمة وعلى راسك**")
    if user.id == 203585:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور زلمة وعلى راسك**")
    muh = user.first_name.replace("\u2060", "") if user.first_name else user.username
    sos = random.choice(rr7)
    await edit_or_reply(
        mention, f"- نسبة الانوثة لـ [{muh}](tg://user?id={user.id}) هـي {sos} 🥵🖤"
    )


@ZE.ar_cmd(pattern="نسبة الغباء(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    muh = user.first_name.replace("\u2060", "") if user.first_name else user.username
    rzona = random.choice(rr7)
    await edit_or_reply(
        mention, f"نسبة الغباء لـ [{muh}](tg://user?id={user.id}) هـي {rzona} 😂💔"
    )


@ZE.ar_cmd(pattern="نسبة الجمال(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    muh = user.first_name.replace("\u2060", "") if user.first_name else user.username
    rzona = random.choice(rr7)
    await edit_or_reply(
        mention, f"نسبة الجمال لـ [{muh}](tg://user?id={user.id}) هـي {rzona} 🌝"
    )


@ZE.ar_cmd(pattern="رفع تاج(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        return await edit_or_reply(mention, f"[{custom}](tg://user?id={user.id})")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention, f"⎊ المستخدم [{tag}](tg://user?id={user.id}) \n⎊ تـم رفعـه تاج 👑🔥"
    )


@ZE.ar_cmd(pattern="رفع قرد(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 5650717789:
        return await edit_or_reply(mention, f"**⎊ لا يمكنك استخدام الامر على مطور السورس**")
    if user.id == 166561:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    if user.id == 203445:
        return await edit_or_reply(mention, f"**- لكك دي هذا المطور**")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention,
        f"⎊ المستخدم [{tag}](tg://user?id={user.id}) \n⎊ تـم رفعـه قرد واعطائه موزة 🐒🍌",
    )


@ZE.ar_cmd(pattern="اوصف(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    muh = user.first_name.replace("\u2060", "") if user.first_name else user.username
    rzona = random.choice(osfroz)
    await edit_or_reply(mention, f"{rzona}")


@ZE.ar_cmd(pattern="شغله(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    muh = user.first_name.replace("\u2060", "") if user.first_name else user.username
    rezw = random.choice(rzwhat)
    await edit_or_reply(
        mention, f"- المستخدم [{muh}](tg://user?id={user.id}) شغله هو {rezw}"
    )


@ZE.ar_cmd(pattern="نسبة الرجولة(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 5650717789:
        return await edit_or_reply(mention, f"**100%**")
    if user.id == 169561:
        return await edit_or_reply(mention, f"**100%**")
    if user.id == 203485:
        return await edit_or_reply(mention, f"**100%**")
    muh = user.first_name.replace("\u2060", "") if user.first_name else user.username
    sos = random.choice(kz)
    await edit_or_reply(
        mention, f"- نسبة الرجولة لـ [{muh}](tg://user?id={user.id}) هـي {sos} 🥵🖤"
    )


@ZE.ar_cmd(pattern="رفع حيوان(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        return await edit_or_reply(mention, f"[{custom}](tg://user?id={user.id})")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention, f"⎊ المستخدم [{tag}](tg://user?id={user.id}) \n⎊ تـم رفعـه حيوان 🐏"
    )


@ZE.ar_cmd(pattern="رفع بزون(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        return await edit_or_reply(mention, f"[{custom}](tg://user?id={user.id})")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention, f"⎊ المستخدم [{tag}](tg://user?id={user.id}) \n⎊ تـم رفعـه بزون 🐈"
    )


@ZE.ar_cmd(pattern="رفع زاحف(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        return await edit_or_reply(mention, f"[{custom}](tg://user?id={user.id})")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention, f"⎊ المستخدم [{tag}](tg://user?id={user.id}) \n⎊ تـم رفعـه زاحف 🐍💞"
    )


@ZE.on(admin_cmd(pattern="نزوج(?:\s|$)([\s\S]*)"))
async def rzfun(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 5650717789:
        return await edit_or_reply(mention, f"**⌔∮ عذرا هذا مطور السورس**")
    await edit_or_reply(mention, f"**نزوج وماتباوع على غيري 🥺💞 ܰ**")


@ZE.on(admin_cmd(pattern="طلاك(?:\s|$)([\s\S]*)"))
async def mention(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if user.id == 5650717789:
        return await edit_or_reply(mention, f"**⌔∮ عذرا هذا مطور السورس**")
    await edit_or_reply(mention, f"**طالق طالق بالعشرة 😹😭💕 ܰ**")
