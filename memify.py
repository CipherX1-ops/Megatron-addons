# Ported Nd Modified For Ultroid
# Ported From DarkCobra (Modified by @ProgrammingError)
#
# Ultroid - UserBot
# Copyright (C) 2020 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.

"""
✘ Commands Available -

• `{i}mmf <upper text> ; <lower text> <reply to media>`
    To create memes as sticker,
    for tyring different fonts use (.mmf <text>_1)(u can use 0 to 10).

• `{i}mms <upper text> ; <lower text> <reply to media>`
    To create memes as pic,
    for tyring different fonts use (.mms <text>_1)(u can use 0 to 10).

"""

import cv2
import os, io, re ,textwrap
from PIL import Image, ImageDraw, ImageEnhance, ImageFont, ImageOps
from . import *


@ultroid_cmd(pattern="mmf ?(.*)")
async def ultd(event):
    ureply = await event.get_reply_message()
    msg = event.pattern_match.group(1)
    if not (ureply and (ureply.media)):
        xx = await eor(event, "`Reply to any media`")
        return
    if not msg:
        xx = await eor(event, "`Give me something text to write 😑`")
        return
    ultt = await ureply.download_media()
    if ultt.endswith((".tgs")):
        xx = await eor(event, "`Ooo Animated Sticker 👀...`")
        cmd = ["lottie_convert.py", ultt, "ult.png"]
        file = "ult.png"
        process = await asyncio.create_subprocess_exec(
           *cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
        )
        stdout, stderr = await process.communicate()
        stderr.decode().strip()
        stdout.decode().strip()
    elif ultt.endswith((".webp",".png")):
        xx = await eor(event, "`Processing`")
        im = Image.open(ultt)
        im.save("ult.png", format="PNG", optimize=True)
        file = "ult.png"
    else:
        xx = await eor(event, "`Processing`")
        img = cv2.VideoCapture(ultt)
        heh,lol = img.read()
        cv2.imwrite("ult.png",lol)
        file = "ult.png"
    stick = await draw_meme_text(file, msg)
    send = await event.client.send_file(
        event.chat_id, stick, force_document=False, reply_to=event.reply_to_msg_id
    )
    await xx.delete()
    try: 
        os.remove(ultt)
        os.remove(file)
        os.remove(stick)
    except BaseException:
        pass
    


async def draw_meme_text(image_path, msg):
    img = Image.open(image_path)
    os.remove(image_path)
    i_width, i_height = img.size
    if "_" in msg:
        text, font = msg.split("_")
    else:
        text = msg
        font = "default"
    if ";" in text:
        upper_text, lower_text = text.split(";")
    else:
        upper_text = text
        lower_text = ""
    draw = ImageDraw.Draw(img)
    m_font = ImageFont.truetype(
    f"resources/fonts/{font}.ttf", int((70 / 640) * i_width)
    )
    current_h, pad = 10, 5
    if upper_text:
        for u_text in textwrap.wrap(upper_text, width=15):
            u_width, u_height = draw.textsize(u_text, font=m_font)
            draw.text(
                xy=(((i_width - u_width) / 2) - 1, int((current_h / 640) * i_width)),
                text=u_text,
                font=m_font,
                fill=(0, 0, 0),
            )
            draw.text(
                xy=(((i_width - u_width) / 2) + 1, int((current_h / 640) * i_width)),
                text=u_text,
                font=m_font,
                fill=(0, 0, 0),
            )
            draw.text(
                xy=((i_width - u_width) / 2, int(((current_h / 640) * i_width)) - 1),
                text=u_text,
                font=m_font,
                fill=(0, 0, 0),
            )
            draw.text(
                xy=(((i_width - u_width) / 2), int(((current_h / 640) * i_width)) + 1),
                text=u_text,
                font=m_font,
                fill=(0, 0, 0),
            )
            draw.text(
                xy=((i_width - u_width) / 2, int((current_h / 640) * i_width)),
                text=u_text,
                font=m_font,
                fill=(255, 255, 255),
            )
            current_h += u_height + pad
    if lower_text:
        for l_text in textwrap.wrap(lower_text, width=15):
            u_width, u_height = draw.textsize(l_text, font=m_font)
            draw.text(
                xy=(
                    ((i_width - u_width) / 2) - 1,
                    i_height - u_height - int((80 / 640) * i_width),
                ),
                text=l_text,
                font=m_font,
                fill=(0, 0, 0),
            )
            draw.text(
                xy=(
                    ((i_width - u_width) / 2) + 1,
                    i_height - u_height - int((80 / 640) * i_width),
                ),
                text=l_text,
                font=m_font,
                fill=(0, 0, 0),
            )
            draw.text(
                xy=(
                    (i_width - u_width) / 2,
                    (i_height - u_height - int((80 / 640) * i_width)) - 1,
                ),
                text=l_text,
                font=m_font,
                fill=(0, 0, 0),
            )
            draw.text(
                xy=(
                    (i_width - u_width) / 2,
                    (i_height - u_height - int((80 / 640) * i_width)) + 1,
                ),
                text=l_text,
                font=m_font,
                fill=(0, 0, 0),
            )
            draw.text(
                xy=(
                    (i_width - u_width) / 2,
                    i_height - u_height - int((80 / 640) * i_width),
                ),
                text=l_text,
                font=m_font,
                fill=(255, 255, 255),
            )
            current_h += u_height + pad
    imag = "ultt.webp"
    img.save(imag, "WebP")
    return imag


@ultroid_cmd(pattern="mms ?(.*)")
async def ultd(event):
    ureply = await event.get_reply_message()
    msg = event.pattern_match.group(1)
    if not (ureply and (ureply.media)):
        xx = await eor(event, "`Reply to any media`")
        return
    if not msg:
        xx = await eor(event, "`Give me something text to write 😑`")
        return
    ultt = await ureply.download_media()
    if ultt.endswith((".tgs")):
        xx = await eor(event, "`Ooo Animated Sticker 👀...`")
        cmd = ["lottie_convert.py", ultt, "ult.png"]
        file = "ult.png"
        process = await asyncio.create_subprocess_exec(
           *cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
        )
        stdout, stderr = await process.communicate()
        stderr.decode().strip()
        stdout.decode().strip()
    elif ultt.endswith((".webp",".png")):
        xx = await eor(event, "`Processing`")
        im = Image.open(ultt)
        im.save("ult.png", format="PNG", optimize=True)
        file = "ult.png"
    else:
        xx = await eor(event, "`Processing`")
        img = cv2.VideoCapture(ultt)
        heh,lol = img.read()
        cv2.imwrite("ult.png",lol)
        file = "ult.png"
    pic = await draw_meme(file, msg)
    send = await event.client.send_file(
        event.chat_id, pic, force_document=False, reply_to=event.reply_to_msg_id
        )
    await xx.delete()
    try: 
        os.remove(ultt)
        os.remove(file)
    except BaseException:
        pass
    os.remove(pic)


async def draw_meme(image_path, msg):
    img = Image.open(image_path)
    os.remove(image_path)
    i_width, i_height = img.size
    if "_" in msg:
        text, font = msg.split("_")
    else:
        text = msg
        font = "default"
    if ";" in text:
        upper_text, lower_text = text.split(";")
    else:
        upper_text = text
        lower_text = ""
    draw = ImageDraw.Draw(img)
    m_font = ImageFont.truetype(
        f"resources/fonts/{font}.ttf", int((70 / 640) * i_width)
    )
    current_h, pad = 10, 5
    if upper_text:
        for u_text in textwrap.wrap(upper_text, width=15):
            u_width, u_height = draw.textsize(u_text, font=m_font)
            draw.text(
                xy=(((i_width - u_width) / 2) - 1, int((current_h / 640) * i_width)),
                text=u_text,
                font=m_font,
                fill=(0, 0, 0),
            )
            draw.text(
                xy=(((i_width - u_width) / 2) + 1, int((current_h / 640) * i_width)),
                text=u_text,
                font=m_font,
                fill=(0, 0, 0),
            )
            draw.text(
                xy=((i_width - u_width) / 2, int(((current_h / 640) * i_width)) - 1),
                text=u_text,
                font=m_font,
                fill=(0, 0, 0),
            )
            draw.text(
                xy=(((i_width - u_width) / 2), int(((current_h / 640) * i_width)) + 1),
                text=u_text,
                font=m_font,
                fill=(0, 0, 0),
            )
            draw.text(
                xy=((i_width - u_width) / 2, int((current_h / 640) * i_width)),
                text=u_text,
                font=m_font,
                fill=(255, 255, 255),
            )
            current_h += u_height + pad
    if lower_text:
        for l_text in textwrap.wrap(lower_text, width=15):
            u_width, u_height = draw.textsize(l_text, font=m_font)
            draw.text(
                xy=(
                    ((i_width - u_width) / 2) - 1,
                    i_height - u_height - int((20 / 640) * i_width),
                ),
                text=l_text,
                font=m_font,
                fill=(0, 0, 0),
            )
            draw.text(
                xy=(
                    ((i_width - u_width) / 2) + 1,
                    i_height - u_height - int((20 / 640) * i_width),
                ),
                text=l_text,
                font=m_font,
                fill=(0, 0, 0),
            )
            draw.text(
                xy=(
                    (i_width - u_width) / 2,
                    (i_height - u_height - int((20 / 640) * i_width)) - 1,
                ),
                text=l_text,
                font=m_font,
                fill=(0, 0, 0),
            )
            draw.text(
                xy=(
                    (i_width - u_width) / 2,
                    (i_height - u_height - int((20 / 640) * i_width)) + 1,
                ),
                text=l_text,
                font=m_font,
                fill=(0, 0, 0),
            )
            draw.text(
                xy=(
                    (i_width - u_width) / 2,
                    i_height - u_height - int((20 / 640) * i_width),
                ),
                text=l_text,
                font=m_font,
                fill=(255, 255, 255),
            )
            current_h += u_height + pad
    pics = "ultt.png"
    img.save(pics, "png")
    return pics

HELP.update({f"{__name__.split('.')[1]}": f"{__doc__.format(i=HNDLR)}"})
