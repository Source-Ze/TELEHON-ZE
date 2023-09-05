from telethon import events

from ZE import ZE

from ..sql_helper.globals import addgvar, delgvar, gvarstatus


@ZE.ar_cmd(pattern="تفعيل الزخرفة الانجليزية")
async def zakrafaon(event):
    if not gvarstatus("enzakrafa"):
        addgvar("enzakrafa", "on")
        await edit_delete(event, "⎊ **تم تفعيل الزخرفة الانجليزية بنجاح ✅**")
        return
    if gvarstatus("enzakrafa"):
        await edit_delete(event, "⎊ **الزخرفة الانجليزية مفعلة بالفعل ✅**")
        return


@ZE.ar_cmd(pattern="تعطيل الزخرفة الانجليزية")
async def zakrafaoff(event):
    if not gvarstatus("enzakrafa"):
        await edit_delete(event, "⎊ **الزخرفة الانجليزية غير مفعلة بالفعل ❌**")
        return
    if gvarstatus("enzakrafa"):
        delgvar("enzakrafa")
        await edit_delete(event, "⎊ **تم تعطيل الزخرفة الانجليزية بنجاح ❌**")
        return


@ZE.on(events.NewMessage(outgoing=True))
async def zakrafarun(event):
    if gvarstatus("enzakrafa"):
        text = event.message.message
        uppercase_text = (
            text.replace("a", "𝔸", "𝐀")
            .replace("b", "𝔹", "𝐁")
            .replace("c", "ℂ", "𝐂")
            .replace("d", "𝔻", "𝐃")
            .replace("e", "𝔼", "𝐄")
            .replace("f", "𝔽", "𝐅")
            .replace("g", "𝔾", "𝐆")
            .replace("h", "ℍ", "𝐇")
            .replace("i", "𝕀", "𝐈")
            .replace("j", "𝕁", "𝐉")
            .replace("k", "𝕂", "𝐊")
            .replace("l", "𝕃", "𝐋")
            .replace("m", "𝕄", "𝐌")
            .replace("n", "ℕ", "𝐍")
            .replace("o", "𝕆", "𝐎")
            .replace("p", "ℙ", "𝐏")
            .replace("q", "ℚ", "𝐐")
            .replace("r", "ℝ", "𝐑")
            .replace("s", "𝕊", "𝐒")
            .replace("t", "𝕋", "𝐓")
            .replace("u", "𝕌", "𝐔")
            .replace("v", "𝕍", "𝐕")
            .replace("w", "𝕎", "𝐖")
            .replace("x", "𝕏", "𝐗")
            .replace("y", "𝕐", "𝐘")
            .replace("z", "ℤ", "𝐙")
        )
        await event.edit(uppercase_text)
