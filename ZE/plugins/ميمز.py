import asyncio
import random
from asyncio.exceptions import TimeoutError

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from ZE import ZE
from ..helpers.utils import reply_id

# الي يخمط ويكول من كتابتي 
@ZE.on(admin_cmd(pattern="حالتي ?(.*)"))
async def _(event):
    await event.edit("**⎊ يتم التاكد من حالتك اذا كنت محظور او لا**")
    async with bot.conversation("@SpamBot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=178220800)
            )
            await conv.send_message("/start")
            response = await response
            await bot.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await event.edit("** اولا الغي حظر @SpamBot وحاول مجددا**")
            return
        await event.edit(f"- {response.message.message}\n @jepthon")


@ZE.on(admin_cmd(pattern="الاغنية ?(.*)"))
async def _(event):
    "To reverse search music by bot."
    if not event.reply_to_msg_id:
        return await event.edit("**▾∮ يجب الرد على الاغنيه اولا**")
    reply_message = await event.get_reply_message()
    chat = "@auddbot"
    try:
        async with event.client.conversation(chat) as conv:
            try:
                await event.edit("**▾∮ يتم التعرف على الاغنية انتظر**")
                start_msg = await conv.send_message("/start")
                response = await conv.get_response()
                send_audio = await conv.send_message(reply_message)
                check = await conv.get_response()
                if not check.text.startswith("Audio received"):
                    return await event.edit(
                        "**▾∮ يجب ان يكون حجم الاغنيه من 5 الى 10 ثواني **."
                    )
                await event.edit("⎊ انتظر قليلا")
                result = await conv.get_response()
                await event.client.send_read_acknowledge(conv.chat_id)
            except YouBlockedUserError:
                await event.edit("```Mohon buka blokir (@auddbot) dan coba lagi```")
                return
            namem = f"**الأغنية : **{result.text.splitlines()[0]}\
        \n\n**التفاصيـل : **{result.text.splitlines()[2]}"
            await event.edit(namem)
            await event.client.delete_messages(
                conv.chat_id,
                [start_msg.id, send_audio.id, check.id, result.id, response.id],
            )
    except TimeoutError:
        return await event.edit("***حدث خطا ما حاول مجددا**")


@ZE.on(admin_cmd(pattern="ايميل وهمي(?: |$)(.*)"))
async def _(event):
    chat = "@TempMailBot"
    geez = await event.edit("**جاري انشاء بريد ...**")
    async with bot.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=220112646)
            )
            await conv.send_message("/start")
            await asyncio.sleep(1)
            await conv.send_message("/create")
            response = await response
            ZEmail = (response).reply_markup.rows[2].buttons[0].url
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await geez.edit("**الغي حظر @TempMailBot  و حاول مجددا**")
            return
        await event.edit(
            f"الايميل الخاص هو `{response.message.message}`\n[ اضغط هنا لرؤية من رسائل الايميل الواردة]({ZEmail})"
        )
@ZE.on(admin_cmd(outgoing=True, pattern="غنيلي$"))
async def jepvois(vois):
  rl = random.randint(3,267)
  url = f"https://t.me/DwDi1/{rl}"
  await vois.client.send_file(vois.chat_id,url,caption="⎊︙ BY : @UI_XB 🎀",parse_mode="html")
  await vois.delete()

@ZE.on(admin_cmd(outgoing=True, pattern="شعر$"))
async def jepvois(vois):
  rl = random.randint(2,101)
  url = f"https://t.me/L1BBBL/{rl}"
  await vois.client.send_file(vois.chat_id,url,caption="⎊︙ BY : @UI_XB 🎀",parse_mode="html")
  await vois.delete()
@ZE.on(admin_cmd(outgoing=True, pattern="قران$"))
async def jepvois(vois):
  rl = random.randint(2,101)
  url = f"https://t.me/QuraanJep/{rl}"
  await vois.client.send_file(vois.chat_id,url,caption="⎊︙ BY : @UI_XB 🤲🏻☪️",parse_mode="html")
  await vois.delete()
@ZE.on(admin_cmd(outgoing=True, pattern="ثيم$"))
async def jepThe(theme):
  rl = random.randint(2,510)
  url = f"https://t.me/GSSSD/{rl}"
  await theme.client.send_file(theme.chat_id,url,caption="⎊︙ THEME BY : @UI_XB 🎊",parse_mode="html")
  await theme.delete()
@ZE.on(admin_cmd(outgoing=True, pattern="لاتغلط$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/MemeSoundJep/4"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ZE.on(admin_cmd(outgoing=True, pattern="بجيت$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/MemeSoundJep/5"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ZE.on(admin_cmd(outgoing=True, pattern="نشاقة$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/MemeSoundJep/3"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ZE.on(admin_cmd(outgoing=True, pattern="احب الله$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/MemeSoundJep/2"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ZE.on(admin_cmd(outgoing=True, pattern="روح$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/MemeSoundJep/6"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ZE.on(admin_cmd(outgoing=True, pattern="انمي1$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/MemeSoundJep/7"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ZE.on(admin_cmd(outgoing=True, pattern="انمي2$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/MemeSoundJep/9"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ZE.on(admin_cmd(outgoing=True, pattern="انمي3$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/MemeSoundJep/11"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ZE.on(admin_cmd(outgoing=True, pattern="انمي4$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/MemeSoundJep/12"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ZE.on(admin_cmd(outgoing=True, pattern="انمي5$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/MemeSoundJep/13"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ZE.on(admin_cmd(outgoing=True, pattern="انمي6$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/MemeSoundJep/14"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ZE.on(admin_cmd(outgoing=True, pattern="انمي7$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/MemeSoundJep/15"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ZE.on(admin_cmd(outgoing=True, pattern="انمي8$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/MemeSoundJep/16"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ZE.on(admin_cmd(outgoing=True, pattern="انمي9$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/MemeSoundJep/17"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ZE.on(admin_cmd(outgoing=True, pattern="انمي10$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/MemeSoundJep/18"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ZE.on(admin_cmd(outgoing=True, pattern="زيج2$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/MemeSoundJep/19"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ZE.on(admin_cmd(outgoing=True, pattern="زيج$"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/MemeSoundJep/20"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@ZE.on(admin_cmd(outgoing=True, pattern="(نكته|نكتة)"))
async def jepmeme(memejep):
  Jep = await reply_id(memejep)
  url = f"https://t.me/IEIEIElEI/94"
  await memejep.client.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
