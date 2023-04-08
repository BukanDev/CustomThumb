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

async def main():
    await bot.start()
    print(f"{bot.me.first_name} | @{bot.me.username}Telah aktif")
    await idle()

if __name__ == "__main__" :
    get_event_loop_policy().get_event_loop().run_until_complete(main())
    
    