# Credits: @pySmartDL
# Copyright (C) 2023 CustomThumb
#
# This file is a part of < https://github.com/BukanDev/CustomThumb/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/BukanDev/CustomThumb/blob/main/LICENSE/>.
#

import os
import time
import math
from pyrogram import Client, filters
from dotenv import load_dotenv

load_dotenv(".env")

BOT_TOKEN = os.environ.get("BOT_TOKEN")
API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")


bot = Client(
    name="RenameBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    
    )
bot.run()
print("The bot is on")


async def progress_dl(current, total, ud_type, message, start):
    now = time.time()
    diff = now - start
    if round(diff % 10.00) == 0 or current == total:
        # if round(current / total * 100, 0) % 5 == 0:
        percentage = current * 100 / total
        speed = current / diff
        elapsed_time = round(diff) * 1000
        time_to_completion = round((total - current) / speed) * 1000
        estimated_total_time = elapsed_time + time_to_completion

        elapsed_time = TimeFormatter(milliseconds=elapsed_time)
        estimated_total_time = TimeFormatter(milliseconds=estimated_total_time)

        progress = "[{0}{1}] \n**Progress**: {2}%\n".format(
            "".join(["⬛" for i in range(math.floor(percentage / 5))]),
            "".join(["⬜" for i in range(20 - math.floor(percentage / 5))]),
            round(percentage, 2),
        )

        tmp = progress + "{0} of {1}\n**Speed**: {2}/s\n**ETA**: {3}\n".format(
            humanbytes(current),
            humanbytes(total),
            humanbytes(speed),
            # elapsed_time if elapsed_time != '' else "0 s",
            estimated_total_time if estimated_total_time != "" else "0 s",
        )
        try:
            await message.edit(text="{}\n {}".format(ud_type, tmp))
        except:
            pass


def humanbytes(size):
    # https://stackoverflow.com/a/49361727/4723940
    # 2**10 = 1024
    if not size:
        return ""
    power = 2**10
    n = 0
    Dic_powerN = {0: " ", 1: "Ki", 2: "Mi", 3: "Gi", 4: "Ti"}
    while size > power:
        size /= power
        n += 1
    return str(round(size, 2)) + " " + Dic_powerN[n] + "B"


def TimeFormatter(milliseconds: int) -> str:
    seconds, milliseconds = divmod(int(milliseconds), 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    tmp = (
        ((str(days) + "d, ") if days else "")
        + ((str(hours) + "h, ") if hours else "")
        + ((str(minutes) + "m, ") if minutes else "")
        + ((str(seconds) + "s, ") if seconds else "")
        + ((str(milliseconds) + "ms, ") if milliseconds else "")
    )
    return tmp[:-2]
    
    
@bot.on_message(filters.command("start") & filters.private)
async def start_bot(c, m):
    await m.reply("This bot is a bot for changing video thumbnails with your custom photos")

@bot.on_message(filters.command("help") & filters.private)
async def help_bot(c, m):
    await m.reply("/start - for start bot\n/help - for help bot\n/thumb - for custom thumb\n/rthumb - for remove custom thumb\n/cekthumb - for cek custom thumb\n/rename - for rename video")
    
@bot.on_message(filters.command("thumb") & filters.private)
async def set_thumb(c, m):
    rep = m.reply_to_message
    if not rep:
        return await m.reply("Please reply to photo")
    if rep.photo:
        anu = await c.download_media(rep, f"thumb/{m.from_user.id}.jpg")
        await m.reply("thumb successfully set")
    else:
        return await m.reply("Sorry wrong")
        
@bot.on_message(filters.command("rthumb") & filters.private)
async def remove_thumb(c, m):
    if os.path.isfile(f"thumb/{m.from_user.id}.jpg"):
        os.remove(f"thumb/{m.from_user.id}.jpg")
        await m.reply("thumb successfully removed")
    else:
        return await m.reply("Sorry, thumbs not set")
        
@bot.on_message(filters.command("cekthumb") & filters.private)
async def cek_thumb(c, m):
    if not os.path.isfile(f"thumb/{m.from_user.id}.jpg"):
        return await m.reply("Sorry, thumbs not set")
    elif os.path.isfile(f"thumb/{m.from_user.id}.jpg"):
        iya = f"thumb/{m.from_user.id}.jpg"
        await c.send_photo(m.chat.id, iya)
    
@bot.on_message(filters.command("rename") & filters.private)
async def rename_file(c, m):
    rep = m.reply_to_message
    if not rep:
        return await m.reply("Please reply to video")
    if rep.video.file_size < 10000000:
        return await m.reply("Sorry, the file size is less than 10MB")
    if rep.video:
        if not os.path.isfile(f"thumb/{m.from_user.id}.jpg"):
            return await m.reply("Sorry, thumbs not set")
        elif os.path.isfile(f"thumb/{m.from_user.id}.jpg"):
            iya = f"thumb/{m.from_user.id}.jpg"
            hems = await m.reply("Start renaming the video...")
            tm = time.time()
            anu = await c.download_media(rep, progress=progress_dl,
                        progress_args=("**Start Downloading...**", hems, tm),
            )
            await c.send_video(
                m.chat.id,
                anu,
                caption=rep.caption,
                caption_entities=rep.caption_entities,
                duration=rep.video.duration,
                width=rep.video.width,
                height=rep.video.height,
                thumb=iya,
                progress=progress_dl,
                progress_args=("**Start Uploading**", hems, tm),
            )
            await hems.delete()
            os.remove(anu)
        
    else:
        return await m.reply("Sorry wrong")
        
