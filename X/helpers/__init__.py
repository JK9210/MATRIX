from .adminHelpers import *
from .basic import *
from .constants import *
from .expand import *
#from .misc import *
from .interval import *
from .msg_types import *
from .parser import *
from .PyroHelpers import *
from .tools import *
from .utility import *


import os
import sys
from pyrogram import Client


def restart():
    os.execvp(sys.executable, [sys.executable, "-m", "X"])

async def join(client):
    try:
        await client.join_chat("STORM_TECHH")
        await client.join_chat("STORM_CHATZ")
        await client.join_chat("TORNADO_TRIBE")
        await client.join_chat("BOT_DEVEPOLING")
        await client.join_chat("Japanese_Userbot")
        await client.join_chat("Japanese_Userbot_Channel")
    except BaseException:
        pass
