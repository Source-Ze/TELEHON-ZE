import html
import os
import base64

from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from telethon.tl.types import MessageEntityMentionName

from requests import get
from telethon.tl.functions.photos import GetUserPhotosRequest
from telethon.tl.functions.users import GetFullUserRequest

from ZE import ZE
from ZE.core.logger import logging

from ZE.Config import Config
from ZE.core.managers import edit_or_reply, edit_delete
from ZE.helpers import reply_id
from ZE.sql_helper.globals import gvarstatus
from ZE.plugins import spamwatch

LOGS = logging.getLogger(__name__)

async def get_user_from_event(event):
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        user_object = await event.client.get_entity(previous_message.sender_id)
    else:
        user = event.pattern_match.group(1)
        if user.isnumeric():
            user = int(user)
        if not user:
            self_user = await event.client.get_me()
            user = self_user.id
        if event.message.entities:
            probable_user_mention_entity = event.message.entities[0]
            if isinstance(probable_user_mention_entity, MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                user_obj = await event.client.get_entity(user_id)
                return user_obj
        if isinstance(user, int) or user.startswith("@"):
            user_obj = await event.client.get_entity(user)
            return user_obj
        try:
            user_object = await event.client.get_entity(user)
        except (TypeError, ValueError) as err:
            await event.edit(str(err))
            return None
    return user_object


async def fetch_info(replied_user, event):
    
    FullUser = (await event.client(GetFullUserRequest(replied_user.id))).full_user
    replied_user_profile_photos = await event.client(
        GetUserPhotosRequest(user_id=replied_user.id, offset=42, max_id=0, limit=80)
    )
    replied_user_profile_photos_count = "⌔∮ هذا المستخدم لم يضع اي صورة"
    dc_id = "Can't get dc id"
    try:
        replied_user_profile_photos_count = replied_user_profile_photos.count
        dc_id = replied_user.photo.dc_id
    except AttributeError:
        pass
    user_id = replied_user.id
    first_name = replied_user.first_name
    full_name = FullUser.private_forward_name
    common_chat = FullUser.common_chats_count
    username = replied_user.username
    user_bio = FullUser.about
    is_bot = replied_user.bot
    restricted = replied_user.restricted
    verified = replied_user.verified
    photo = await event.client.download_profile_photo(
        user_id,
        Config.TMP_DOWNLOAD_DIRECTORY + str(user_id) + ".jpg",
        download_big=True,
    )
    first_name = (
        first_name.replace("\u2060", "")
        if first_name
        else ("هذا المستخدم ليس لديه اسم اول")
    )
    full_name = full_name or first_name
    username = "@{}".format(username) if username else ("⌔∮ هذا المستخدم ليس لديه معرف")
    user_bio = "⌔∮ هذا المستخدم ليس لديه اي نبذة" if not user_bio else user_bio
    rozrtba = (
        ".「  مـطـور آلُِسورس 𓄂𓆃 」."
        if user_id == 5650717789 or user_id == 574568 or user_id == 568865 or user_id == 550880 or user_id == 525601 or user_id == 183303
        else (".「  العضـو 𓅫 」.")
    )
    rozrtba = (
        ".「 مـالك الحساب  」."
        if user_id == (await event.client.get_me()).id
        and user_id != 5650717789
        and user_id != 574528
        and user_id != 591695
        and user_id != 525601
        and user_id != 568865
        and user_id != 550850
        else rozrtba
    )     
    caption = " ╮•⎚ مـعلومات الـشخص مـن بـوت سبايدر\n"
    caption += f"✛┈┉━｢ 𝑺𝑶𝑼𝑹𝑪𝑬 𝒁𝑬 . 🔱 ｣━┅┈✛\n"
    caption += f"╽<b>- ❃الاسـم ⇜ </b> {full_name}\n"
    caption += f"╽<b>- ❃المـعـرف ⇜ </b> {username}\n"
    caption += f"╽<b>- ❃الايـدي  ⇜</b> <code>{user_id}</code>\n"
    caption += f"╽<b>- ❃الـمجموعات المشتـركة ⇜</b> {common_chat}\n"
    caption += f"╽<b>- عـدد ❃الصـورة ⇜</b> {replied_user_profile_photos_count}\n"
    caption += f"╽<b>- ❃الرتبـة ⇜</b>{rozrtba}\n"
    caption += f"╽<b>-️ ❃الـنبـذه ⇜</b> \n<code>{user_bio}</code>\n"
    caption += f"╽<b>- رابط حسـابه ⇜</b> "
    caption += f'<a href="tg://user?id={user_id}">{first_name}</a>\n'
    caption += f"✛┈┉━｢ 𝑺𝑶𝑼𝑹𝑪𝑬 𝒁𝑬 . 🔱 ｣━┅┈✛\n"
    caption += f"♤ @UI_XB ♤"
    return photo, caption

@ZE.ar_cmd(pattern="ايدي(?: |$)(.*)")
async def who(event):
    roz = await edit_or_reply(event, "⇆")
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    replied_user = await get_user_from_event(event)
    try:
        photo, caption = await fetch_info(replied_user, event)
    except AttributeError:
        return await edit_or_reply(roz,  "**⌔∮ لم يتم العثور على معلومات لهذا المستخدم **")
    message_id_to_reply = event.message.reply_to_msg_id
    if not message_id_to_reply:
        message_id_to_reply = None
    try:
        await event.client.send_file(
            event.chat_id,
            photo,
            caption=caption,
            link_preview=False,
            force_document=False,
            reply_to=message_id_to_reply,
            parse_mode="html",
        )
        if not photo.startswith("http"):
            os.remove(photo)
        await roz.delete()
    except TypeError:
        await roz.edit(caption, parse_mode="html")


@ZE.ar_cmd(pattern="رابط الحساب(?:\s|$)([\s\S]*)")
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        return await edit_or_reply(mention, f"[{custom}](tg://user?id={user.id})")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(mention, f"⪼  [{tag}](tg://user?id={user.id})  𓆰. ")
