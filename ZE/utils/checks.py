from telethon.tl.types import ChannelParticipantAdmin, ChannelParticipantCreator

from ..core.logger import logging

LOGS = logging.getLogger(__name__)


# للتأكد من الادمن
async def is_admin(ZE, chat_id, userid):
    if not str(chat_id).startswith("-100"):
        return False
    try:
        req_jo = await ZE.get_permissions(chat_id, userid)
        chat_participant = req_jo.participant
        if isinstance(
            chat_participant, (ChannelParticipantCreator, ChannelParticipantAdmin)
        ):
            return True
    except Exception as e:
        LOGS.info(str(e))
        return False
    else:
        return False
