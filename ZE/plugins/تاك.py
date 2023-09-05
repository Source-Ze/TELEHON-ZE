from telethon import functions
from telethon.tl import functions
from telethon.tl.functions.channels import InviteToChannelRequest

from ZE import ZE

from ..core.managers import edit_delete, edit_or_reply

@ZE.on(admin_cmd(pattern="تاك(?: |$)(.*)"))
async def iq(ZE):
    mentions = ZE.text[8:]
    chat = await ZE.get_input_chat()
    async for x in ZE.client.iter_participants(chat, 200):
        mentions += f" \n🝳 ⦙ ⵧ〈[{x.first_name}](tg://user?id={x.id})〉"
    await ZE.client.send_message(ZE.chat_id, mentions)
    await ZE.delete()
@ZE.on(admin_cmd(pattern="تاك 150(?: |$)(.*)"))
async def iq(ZE):
    mentions = ZE.text[8:]
    chat = await ZE.get_input_chat()
    async for x in ZE.client.iter_participants(chat, 150):
        mentions += f" \n🝳 ⦙ ⵧ〈[{x.first_name}](tg://user?id={x.id})〉 \n"
    await ZE.client.send_message(ZE.chat_id, mentions)
    await ZE.delete()
@ZE.on(admin_cmd(pattern="تاك 100(?: |$)(.*)"))
async def iq(ZE):
    mentions = ZE.text[8:]
    chat = await ZE.get_input_chat()
    async for x in ZE.client.iter_participants(chat, 100):
        mentions += f" \n🝳 ⦙ ⵧ〈[{x.first_name}](tg://user?id={x.id})〉 \n"
    await ZE.client.send_message(ZE.chat_id, mentions)
    await ZE.delete()
@ZE.on(admin_cmd(pattern="تاك 50(?: |$)(.*)"))
async def iq(ZE):
    mentions = ZE.text[8:]
    chat = await ZE.get_input_chat()
    async for x in ZE.client.iter_participants(chat, 50):
        mentions += f" \n🝳 ⦙ ⵧ〈[{x.first_name}](tg://user?id={x.id})〉 \n"
    await ZE.client.send_message(ZE.chat_id, mentions)
    await ZE.delete()
@ZE.on(admin_cmd(pattern="تاك 10(?: |$)(.*)"))
async def iq(ZE):
    mentions = ZE.text[8:]
    chat = await ZE.get_input_chat()
    async for x in ZE.client.iter_participants(chat, 10):
        mentions += f" \n 🝳 ⦙ ⵧ〈[{x.first_name}](tg://user?id={x.id})〉 \n"
    await ZE.client.send_message(ZE.chat_id, mentions)
    await ZE.delete()
