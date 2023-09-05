import contextlib
import sys

import ZE
from ZE import BOTLOG_CHATID, PM_LOGGER_GROUP_ID
from razan.strings import blacklisted_users

from .Config import Config
from .core.logger import logging
from .core.session import ZE
from .sql_helper.globals import gvarstatus
from .utils import (
    add_bot_to_logger_group,
    load_plugins,
    mybot,
    saves,
    setup_bot,
    startupmessage,
    verifyLoggerGroup,
)

LOGS = logging.getLogger("سورس زد إي")

cmdhr = Config.COMMAND_HAND_LER

try:
    LOGS.info("يتم بدء البوت المساعد")
    ZE.loop.run_until_complete(setup_bot())
    LOGS.info("اكتملت عمليه البوت المساعد")
except Exception as e:
    LOGS.error(f"{e}")
    sys.exit()

try:
    LOGS.info("يتم تفعيل وضع حمايه الحساب من الاختراق")
    ZE.loop.create_task(saves())
    LOGS.info("تم تفعيل وضع حمايه الحساب من الاختراق")
except Exception as bb:
    LOGS.error(f"- {bb}")
    sys.exit()


try:
    LOGS.info("يتم تفعيل وضع الانلاين")
    ZE.loop.run_until_complete(mybot())
    LOGS.info("تم تفعيل وضع الانلاين بنجاح ✓")
except Exception as meo:
    LOGS.error(f"- {meo}")
    sys.exit()


async def startup_process():
    if ZE.uid in blacklisted_users:
        LOGS.info("انت لا يمكنك تنصيب سورس زد إي عزيزي دي")
        return
    if not gvarstatus("TNSEEB"):
        try:
            await verifyLoggerGroup()
            await load_plugins("plugins")
            await load_plugins("assistant")
            LOGS.info("============================================================")
            LOGS.info("تم انتهاء عملية التنصيب بنجاح")
            LOGS.info(
                f"لمعرفة اوامر السورس ارسل {cmdhr}الاوامر\
                \nمجموعة قناة السورس  https://t.me/UI_XB"
            )
            LOGS.info("============================================================")
            await verifyLoggerGroup()
            await add_bot_to_logger_group(BOTLOG_CHATID)
            if PM_LOGGER_GROUP_ID != -100:
                await add_bot_to_logger_group(PM_LOGGER_GROUP_ID)
            await startupmessage()
            return
        except Exception as e:
            LOGS.info(str(e))
            return
    else:
        LOGS.info("انت لا يمكنك تنصيب سورس زد إي عزيزي دي")
        LOGS.info("انت لا يمكنك تنصيب سورس زد إي عزيزي دي")
        LOGS.info("انت لا يمكنك تنصيب سورس زد إي عزيزي دي")


ZE.loop.run_until_complete(startup_process())

if len(sys.argv) in {1, 3, 4}:
    with contextlib.suppress(ConnectionError):
        ZE.run_until_disconnected()
else:
    ZE.disconnect()
