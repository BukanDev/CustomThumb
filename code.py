# Credits: @pySmartDL
# Copyright (C) 2023 CustomThumb
#
# This file is a part of < https://github.com/BukanDev/CustomThumb/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/BukanDev/CustomThumb/blob/main/LICENSE/>.
#

from pyrogram import Client as c

API_ID = input("\nEnter Your API_ID:\n > ")
API_HASH = input("\nEnter Your API_HASH:\n > ")

print("\n\n Enter Phone number when asked.\n\n")

i = c(name="gen", in_memory=True, api_id=API_ID, api_hash=API_HASH)

with i:
    ss = i.export_session_string()
    print("\nHERE IS YOUR STRING SESSION, COPY IT, DON'T SHARE!!\n")
    print(f"\n{ss}\n")
