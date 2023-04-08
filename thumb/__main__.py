# Credits: @pySmartDL
# Copyright (C) 2023 CustomThumb
#
# This file is a part of < https://github.com/BukanDev/CustomThumb/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/BukanDev/CustomThumb/blob/main/LICENSE/>.
#

from thumb import bot
from asyncio import get_event_loop_policy
from pyrogram.methods.utilities.idle import idle
from thumb.plugins import ALL_MODULES

async def main():
    await bot.start()
    for all_module in ALL_MODULES:
        importlib.import_module(f"thumb.plugins.{all_module}")
    print(f"{bot.me.first_name} | @{bot.me.username}Telah aktif")
    await idle()

if __name__ == "__main__" :
    get_event_loop_policy().get_event_loop().run_until_complete(main())
    
    