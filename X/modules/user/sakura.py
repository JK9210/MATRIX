#MIT License

#Copyright (c) 2024 Japanese-X-Userbot

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.

import random
from pyrogram import Client, filters
from config import SUDO_USERS
from .help import * 

hl = "."

@Client.on_message(
    filters.command(["sakura"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def castle(client, message):
    args = message.text.split(" ")[1:]
    castledata = [
  "https://graph.org/file/78acb6560a402baa9d812.jpg",
  "https://graph.org/file/058adc2304eaf04b38792.jpg",
  "https://graph.org/file/de6f3f853b158a61d19dc.jpg",
  "https://graph.org/file/82b863bab4ba088f3ff60.jpg",
  "https://graph.org/file/b2e19298b4c6b3ae8703e.jpg",
  "https://graph.org/file/08c352184ceba84f21561.jpg",
  "https://graph.org/file/de6f3f853b158a61d19dc.jpg",
  "https://graph.org/file/058adc2304eaf04b38792.jpg",
    ]
    castle_url = random.choice(castledata)
    await message.reply_photo(castle_url)

add_command_help(
    "•─╼⃝𖠁 Sᴀᴋᴜʀᴀ",
    [
       ["sakura", "Gɪᴠᴇ random Sᴀᴋᴜʀᴀ pic."],
        ],
)
