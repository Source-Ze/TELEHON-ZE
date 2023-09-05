from ZE import *
from ZE import ZE 
from ..sql_helper.globals import gvarstatus

@ZE.on(admin_cmd(pattern="(ذاتية|ذاتيه)"))
async def dato(event):
    if not event.is_reply:
        return await event.edit("..")
    ZE = await event.get_reply_message()
    pic = await ZE.download_media()
    await bot.send_file(
        "me",
        pic,
        caption=f"""
- تـم جـلب الصـورة بنجـاح ✓ 
- غير مبري الذمه اذا استخدمت الامر للابتزاز
- CH: @UI_XB 
- Dev: @UP_UO 
  """,
    )
    await event.edit(" 🙂❤️ ")
