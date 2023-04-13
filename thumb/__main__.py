# Credits: @pySmartDL
# Copyright (C) 2023 CustomThumb
#
# This file is a part of < https://github.com/BukanDev/CustomThumb/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/BukanDev/CustomThumb/blob/main/LICENSE/>.
#

import importlib
from asyncio import get_event_loop_policy

from pyrogram.methods.utilities.idle import idle
from pyrogram.types import BotCommand, BotCommandScopeAllPrivateChats

from thumb import bot
from thumb.plugins import ALL_MODULES


async def main():
    await bot.start()
    for all_module in ALL_MODULES:
        importlib.import_module(f"thumb.plugins.{all_module}")
    print(f"{bot.me.first_name} | @{bot.me.username} Has been active")
    await bot.set_bot_commands(
        [
            BotCommand("start", "start bot"),
            BotCommand("help", "helppers bot"),
            BotCommand("thumb", "change tumb video"),
            BotCommand("rthumb", "remove thumb video"),
            BotCommand("cekthumb", "cek custom thumb"),
            BotCommand("rename", "reply to video to modif thumb"),
        ],
        BotCommandScopeAllPrivateChats(),
    )
    await idle()


if __name__ == "__main__":
    get_event_loop_policy().get_event_loop().run_until_complete(main())
