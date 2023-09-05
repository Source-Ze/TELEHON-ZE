import random

from ZE import ZE

from ..core.managers import edit_or_reply
from . import fonts

plugin_category = "extra"


@ZE.ar_cmd(
    pattern="زخرفة1(?:\s|$)([\s\S]*)",
    command=("زخرفة1", plugin_category),)
async def stylish_generator(event):
    "Changes font style of the given text"
    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await edit_or_reply(event, "**اعـطنـي نـص اولا 🧸🖤**")
        return
    string = "  ".join(args).lower()
    for normalfontcharacter in string:
        if normalfontcharacter in fonts.normalfont:
            musicalcharacter = fonts.musicalfont[
                fonts.normalfont.index(normalfontcharacter)
            ]
            string = string.replace(normalfontcharacter, musicalcharacter)
    await edit_or_reply(event, string)


@ZE.ar_cmd(
    pattern="زخرفة2(?:\s|$)([\s\S]*)",
    command=("زخرفة2", plugin_category),)
async def stylish_generator(event):
    "Changes font style of the given text"
    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await edit_or_reply(event, "**اعـطنـي نـص اولا 🌺😗🗿**")
        return
    string = "  ".join(args).lower()
    for normalfontcharacter in string:
        if normalfontcharacter in fonts.normalfont:
            ancientcharacter = fonts.ancientfont[
                fonts.normalfont.index(normalfontcharacter)
            ]
            string = string.replace(normalfontcharacter, ancientcharacter)
    await edit_or_reply(event, string)


@ZE.ar_cmd(
    pattern="زخرفة3(?:\s|$)([\s\S]*)",
    command=("زخرفة3", plugin_category),)
async def vapor(event):
    "Changes font style of the given text"
    reply_text = []
    textx = await event.get_reply_message()
    message = event.pattern_match.group(1)
    if message:
        pass
    elif textx:
        message = textx.text
    else:
        await edit_or_reply(event, "اعـطنـي نـص اولا 🧸♥")
        return

    for charac in message:
        if 0x21 <= ord(charac) <= 0x7F:
            reply_text.append(chr(ord(charac) + 0xFEE0))
        elif ord(charac) == 0x20:
            reply_text.append(chr(0x3000))
        else:
            reply_text.append(charac)

    await edit_or_reply(event, "".join(reply_text))


@ZE.ar_cmd(
    pattern="زخرفة4(?:\s|$)([\s\S]*)",
    command=("زخرفة4", plugin_category),
)
async def stylish_generator(event):
    "Changes font style of the given text"
    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await edit_or_reply(event, "**اعـطنـي نـص اولا 🧸🖤**")
        return
    string = "  ".join(args).lower()
    for normaltextcharacter in string:
        if normaltextcharacter in fonts.normaltext:
            smallcapscharacter = fonts.smallcapsfont[
                fonts.normaltext.index(normaltextcharacter)
            ]
            string = string.replace(normaltextcharacter, smallcapscharacter)
    await edit_or_reply(event, string)


@ZE.ar_cmd(
    pattern="زخرفة5(?:\s|$)([\s\S]*)",
    command=("زخرفة5", plugin_category),
)
async def stylish_generator(event):
    "Changes font style of the given text"
    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await edit_or_reply(event, "**اعـطنـي نـص اولا 🧸🖤**")
        return
    string = "  ".join(args).lower()
    for normaltextcharacter in string:
        if normaltextcharacter in fonts.normaltext:
            bubblesblackcharacter = fonts.bubblesblackfont[
                fonts.normaltext.index(normaltextcharacter)
            ]
            string = string.replace(normaltextcharacter, bubblesblackcharacter)
    await edit_or_reply(event, string)


@ZE.ar_cmd(
    pattern="زخرفة6(?:\s|$)([\s\S]*)",
    command=("زخرفة6", plugin_category),
)
async def stylish_generator(event):
    "Changes font style of the given text"
    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await edit_or_reply(event, "**اعـطنـي نـص اولا 🧸🖤**")
        return
    string = "  ".join(args).lower()
    for normaltextcharacter in string:
        if normaltextcharacter in fonts.normaltext:
            bubblescharacter = fonts.bubblesfont[
                fonts.normaltext.index(normaltextcharacter)
            ]
            string = string.replace(normaltextcharacter, bubblescharacter)
    await edit_or_reply(event, string)


@ZE.ar_cmd(
    pattern="زخرفة7(?:\s|$)([\s\S]*)",
    command=("زخرفة7", plugin_category),
)
async def stylish_generator(event):
    "Changes font style of the given text"
    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await edit_or_reply(event, "**اعـطنـي نـص اولا 🧸🖤**")
        return
    string = "  ".join(args).lower()
    for normaltextcharacter in string:
        if normaltextcharacter in fonts.normaltext:
            tantextcharacter = fonts.tantextfont[
                fonts.normaltext.index(normaltextcharacter)
            ]
            string = string.replace(normaltextcharacter, tantextcharacter)
    await edit_or_reply(event, string)


@ZE.ar_cmd(
    pattern="زخرفة8(?:\s|$)([\s\S]*)",
    command=("زخرفة8", plugin_category),
)
async def stylish_generator(event):
    "Changes font style of the given text"
    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await edit_or_reply(event, "**اعـطنـي نـص اولا 🧸🖤**")
        return
    string = "  ".join(args).lower()
    for normaltextcharacter in string:
        if normaltextcharacter in fonts.normaltext:
            littleboxtextcharacter = fonts.littleboxtextfont[
                fonts.normaltext.index(normaltextcharacter)
            ]
            string = string.replace(normaltextcharacter, littleboxtextcharacter)
    await edit_or_reply(event, string)


@ZE.ar_cmd(
    pattern="زخرفة9(?:\s|$)([\s\S]*)",
    command=("زخرفة9", plugin_category),
)
async def stylish_generator(event):
    "Changes font style of the given text"
    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await edit_or_reply(event, "**اعـطنـي نـص اولا 🧸🖤**")
        return
    string = "  ".join(args).lower()
    for normaltextcharacter in string:
        if normaltextcharacter in fonts.normaltext:
            hwcapitalcharacter = fonts.hwcapitalfont[
                fonts.normaltext.index(normaltextcharacter)
            ]
            string = string.replace(normaltextcharacter, hwcapitalcharacter)
    await edit_or_reply(event, string)


@ZE.ar_cmd(
    pattern="زخرفة10(?:\s|$)([\s\S]*)",
    command=("زخرفة10", plugin_category),
)
async def stylish_generator(event):
    "Changes font style of the given text"
    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await edit_or_reply(event, "**اعـطنـي نـص اولا 🧸🖤**")
        return
    string = "  ".join(args).lower()
    for normaltextcharacter in string:
        if normaltextcharacter in fonts.normaltext:
            doubletextcharacter = fonts.doubletextfont[
                fonts.normaltext.index(normaltextcharacter)
            ]
            string = string.replace(normaltextcharacter, doubletextcharacter)
    await edit_or_reply(event, string)


@ZE.ar_cmd(
    pattern="زخرفة0(?:\s|$)([\s\S]*)",
    command=("زخرفة0", plugin_category),
)
async def spongemocktext(mock):
    "Changes font style of the given text"
    reply_text = []
    textx = await mock.get_reply_message()
    message = mock.pattern_match.group(1)
    if message:
        pass
    elif textx:
        message = textx.text
    else:
        await edit_or_reply(mock, "اعـطنـي نـص اولا")
        return

    for charac in message:
        if charac.isalpha() and random.randint(0, 1):
            to_app = charac.upper() if charac.islower() else charac.lower()
            reply_text.append(to_app)
        else:
            reply_text.append(charac)

    await edit_or_reply(mock, "".join(reply_text))
