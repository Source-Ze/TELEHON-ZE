import asyncio
import random

MALATH = [
    """
༆

𝙸ғ ᴜ ᴅᴏɴᴛ sᴀᴄʀɪғɪᴄᴇ FᴏR 𝚆𝚑𝚊𝚝 𝚄 𝚠𝙰𝚗𝚝,
"ᴡʜAᴛ U ᴡAɴᴛ" ʙᴇCᴏᴍᴇS ᴛʜE Sᴀᴄʀɪғɪᴄᴇ.
""",
    """
𓆩 ﭑجـعل مَن نفسك شيَ يَـصعب تقليدۿـہ 𓆪
""",
    """
𓆩𓆩'‏﮼انا ‏﮼جبل ‏﮼والجبال ‏﮼لا ‏﮼تسقط ‏﮼يا ‏﮼عزيزي ‏﮼𓆪𓆪
""",
    """
 - ثـق بـنفسڪ وﭑتـرڪ ﭑلـباقي عـلى ﭑلـلّه 
""",
    """
𓆩𓆩 قُربك من الله هو مفتاح لجميع الأبواب  𓆪𓆪
""",
    """
𓆩𓆩 ‎ڪُن أنتَ ، ولْيتقَبلك من يَتقبَلك 𓆪𓆪⠀
""",
    """
𓆩𓆩كُن قَويًّا حَتّى لا يُشفَق عليك أحد𓆪𓆪
""",
    """
𓆩𓆩 ڪَن شخصـاً نـادراً يستحـال تڪـراره 𓆪𓆪⠀
""",
    """
 ‏𓆪ڪـُن قَـليل الڪـلام وككثير آلـتجـّاهـل💛ء‏𓆩
""",
    """
 𓆩𓆩 طبعـي ذهب بس الناس موصيـاغ 𓆪𓆪 
""",
    """
 • إصنع حربًا من اجل سعـآدتك 🏹 .
""",
    """
 •  ڪ التاريخ انا لا اعود ولا انتهي 🖤🕊
""",
    """
 ‏- دع العالم يتحدث و افعل ما يحلو لك𓂅
""",
    """
﴿‏ لن تجـد #نسختي ، مهما بحثت ₎ꨄ
""",
    """
𓆩𓆩 قـوي نـفسِك بنفسِك..لاتنتّظر أحد 𓆪𓆪
""",
    """
𓆩𓆩 عيش عمركْ بس للعيون التفهمك 𓆪𓆪
""",
    """
𓆩𓆩 لا حـيـاة بـلا قـوه ولا قـوه بـلا ألــم 𓆪𓆪
""",
    """
𓆩𓆩 قـآتل مُـن ٱجل حلـمڪٰ دائما 𓆪𓆪
""",
    """
   انـا لا أخـسـر أبـداً أمـا اكـســب أو اتـعـلـم♥️
""",
    """
    (‌‏⚜عـينَ ثكَــيلهَ وعــقــلَ يــوزن بــلــدَ⚜)
""",
    """
𓆩𓆩 ﭑنا ﻼ أنڪـــســر بـــل أزداد قـــــوة 𓆪𓆪⠀
""",
    """
- هي لي حياة اكثر من كونها صديقتي
𝒔𝒉𝒆'𝒔 𝒎𝒐𝒓𝒆 𝒐𝒇 𝒂 𝒍𝒊𝒇𝒆 𝒕𝒐 𝒎𝒆 𝒕𝒉𝒂𝒏 𝒎𝒚 𝒇𝒓𝒊𝒆𝒏𝒅
""",
    """
- أبتليت بحب ضحكتك و عيونك الحلوة
𝒊 𝒇𝒆𝒍𝒍 𝒊𝒏 𝒍𝒐𝒗𝒆 𝒘𝒊𝒕𝒉 𝒚𝒐𝒖𝒓 𝒍𝒂𝒖𝒈𝒉𝒕𝒆𝒓 𝒂𝒏𝒅 𝒔𝒘𝒆𝒆𝒕 𝒆𝒚𝒆𝒔
""",
    """
- اي شيء يجعلك تبتسم احتفظ به سرآ
𝒂𝒏𝒚𝒕𝒉𝒊𝒏𝒈 𝒕𝒉𝒂𝒕 𝒎𝒂𝒌𝒆𝒔 𝒚𝒐𝒖 𝒔𝒎𝒊𝒍𝒆, 𝒌𝒆𝒆𝒑 𝒊𝒕 𝒂 𝒔𝒆𝒄𝒓𝒆𝒕
""",
    """
𓆩𓆩انا لـ نفسي السند والقوة ، والحب𓆪𓆪
""",
    """
𖤍  ﻣشغوله ﺑﻣﺳﺗﭱبلي ﻣاﻳﮫﻣني واقعڪمً❥)
""",
    """
""",
    """
( '‏﮼لاتحارب ‏﮼ولاتحاول ‏﮼ولاتعطي ‏﮼انهي ‏﮼فقط.. )
""",
    """
𓆩𓆩 إقتلهم بالنجاح، وإدفنهم بالابتسامة 𓆪𓆪⠀
""",
    """
 ️﴾♥˺توقفْ عن آلتمني آبدء بالعمل ،‏﴿
""",
    """
𓆩𓆩 أنا حلم صعب تكسبهۂ مرتين'💛ء 𓆪𓆪⠀
""",
    """
  هادئـۿ بـ؏ـزلتي وحيدۿ بـ؏ـالمي㋛
    𝒒𝒖𝒊𝒆𝒕 𝒊𝒏 𝒎𝒚 𝒑𝒓𝒂𝒚𝒆𝒓 𝒂𝒍𝒐𝒏𝒆 𝒊𝒏 𝒄𝒂𝒍𝒎𝒚㋛
""",
    """
• كِـثرة الإهتمام خـذلان 〰 .

• 𝙼𝙺𝚄𝙷 𝙸𝙽𝚃𝙴𝚁𝙴𝚂𝚃 𝙻𝙴𝚃 𝙳𝙾𝚆𝙽 .
""",
    """
• عيناها مِن الجمال قُدست 🌍💕 .

• 𝙴𝚈𝙴𝚂 𝚂𝙰𝙽𝙲𝚃𝙸𝙵𝙸𝙴𝙳 𝙱𝚈 𝙱𝙴𝙰𝚄𝚃𝚈 .
""",
    """
• إصنع حربًا من اجل سعـآدتك 🏹 .

• 𝙼𝙰𝙺𝙴 𝚆𝙰𝚁 𝙵𝙾𝚁 𝙷𝙰𝙿𝙿𝙸𝙽𝙴𝚂𝚂 .
""",
    """
• كُن صادِقًا او إصمِت 📮 .

• 𝙱𝙴 𝙷𝙾𝙽𝙴𝚂𝚃 𝙾𝚁 𝚂𝙷𝚄𝚃 𝚄𝙿 .
""",
    """
• لكُل حِــزن ؛ فـرح 👼🏻🤍 .

• 𝙵𝙾𝚁 𝙴𝚅𝙴𝚁𝚈 𝚂𝙰𝙳𝙽𝙴𝚂𝚂 ; 𝙹𝙾𝚈 .
""",
    """
• لاتــكُن لـطيفًا دائِـمًا 👼🏻🤍 .

• 𝙳𝙾 𝙽𝙾𝚃 𝙰𝙻𝚆𝙰𝚈𝚂 𝙱𝙴 𝙽𝙸𝙲𝙴 .
""",
    """
༆

Tʜᴇʀᴇ ɪS Nᴏ Dᴏᴜʙᴛ, 
EᴠᴇʀʏOɴᴇ ɪs Dᴇᴠɪʟ...


ᴀɴᴅ TʜᴇRᴇ  ɪS Nᴏ Dᴏᴜʙᴛ,
Wᴇ ᴀRᴇ Dᴇʟᴠɪʟ ᴏᴜʀSᴇʟᴠᴇS..𓁹𓁹
""",
    """
༒︎

𝐼 𝑆ℎ𝑜𝑢𝑙𝑑 𝐻𝑎𝑣𝑒...⌫
𝐼 𝐶𝑜𝑢𝑙𝑑 𝐻𝑎𝑣𝑒...⌫
𝐼 𝑊𝑖𝑠ℎ 𝐼 𝐻𝑎𝑑...⌫
𝐼𝑓 𝑂𝑛𝑙𝑦 𝐼 𝐻𝑎𝑑...⌫

߷𝔻𝕠𝕟𝕥 𝕋𝕙𝕚𝕟𝕜߷

❥︎𝙅𝙪𝙨𝙩 𝘿𝙤 𝙞𝙩 𝙉𝙤𝙬
""",
    """
༆

𝑻𝒉𝒆 𝒐𝒏𝒍𝒚 𝒕𝒉𝒊𝒏𝒈 𝒘𝒆 𝒂𝒓𝒆 𝒂𝒍𝒍𝒐𝒘𝒆𝒅 𝒕𝒐 𝒅𝒐 𝒊𝒔 𝒕𝒐 𝔹𝕖𝕝𝕚𝕖𝕧𝕖 𝒕𝒉𝒂𝒕 𝒘𝒆 𝒘𝒐𝒏'𝒕 𝙍𝙚𝙜𝙧𝙚𝙩 𝒕𝒉𝒆 𝒄𝒉𝒐𝒊𝒄𝒆𝒔 𝒘𝒆 𝒎𝒂𝒅𝒆.


❥︎ ʟᵉᵛⁱ ᴀᶜᵏᵉʳᵐᵃⁿ
""",
    """
༒︎

ℝ𝕖𝕘𝕣𝕖𝕥𝕤...

𝑾𝒆 𝒂𝒍𝒍 𝒂𝒓𝒆 𝒇𝒖𝒍𝒍 𝒐𝒇 𝒓𝒆𝒈𝒓𝒆𝒕𝒔,
𝑾𝒆 𝒄𝒂𝒏'𝒕 𝐶ℎ𝑎𝑛𝑔𝑒 𝒊𝒕.
𝑾𝒆 𝒄𝒂𝒏'𝒕 𝑆𝑢𝑝𝑝𝑟𝑒𝑠𝑠 𝒊𝒕.
𝑾𝒆 𝒄𝒂𝒏'𝒕 𝐸𝑥𝑝𝑟𝑒𝑠𝑠 𝒊𝒕.
𝑰𝒕 𝒑𝒊𝒏𝒄𝒉 𝒖𝒔 𝒂𝒍𝒍 𝒐𝒗𝒆𝒓 𝒐𝒖𝒓 ᒪIᖴᗴ,
𝚃𝚒𝚕𝚕 𝙳𝚎𝚊𝚝𝚑 .

𝔒ℜ

𝑨𝒇𝒕𝒆𝒓 𝑳𝒊𝒇𝒆 ??  𝑊ℎ𝑜 𝐾𝑛𝑜𝑤𝑠¯\_(ツ)_/¯
""",
    """
༒︎

ℕ𝕠𝕥𝕙𝕚𝕟𝕘 𝚒𝚗 𝚝𝚑𝚒𝚜 𝚏𝚞𝚔𝚒𝚗𝚐 𝚠𝚘𝚛𝚕𝚍 𝚒𝚜 𝐂𝐨𝐧𝐬𝐭𝐚𝐧𝐭...

𝑨𝒍𝒍 𝒂𝒓𝒆 𝐕𝐚𝐫𝐢𝐚𝐛𝐥𝐞 𝒘𝒊𝒕𝒉 𝒓𝒆𝒔𝒑𝒆𝒄𝒕 𝒕𝒐 𝑺𝒐𝒎𝒆𝒐𝒏𝒆 / 𝑺𝒐𝒎𝒆𝒕𝒉𝒊𝒏𝒈.""",
    """
༒︎

𝙷𝚊𝚟𝚎 𝚞 𝙴𝚟𝚎𝚛 𝕀𝕞𝕒𝕘𝕚𝕟𝕖....

This "𝕀𝕞𝕒𝕘𝕚𝕟𝕖" word Is itself a 𝐋𝐢𝐞

Which 𝒅𝒐𝒏'𝒕 𝑬𝒙𝒊𝒔𝒕.
""",
]

# SOURCE ZE @UI_XB 
# MODY @UP_UO 


@bot.on(admin_cmd(pattern="بايو"))
async def ics(zel):
    await zel.edit("**⌔∮ اهلا عزيزي يتم تجهيز بايو لاجلك.**")
    await asyncio.sleep(2)
    tosh = random.choice(MALATH)
    return await zel.edit(f"{tosh}")
