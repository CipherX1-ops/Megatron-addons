
"""
✘ Commands Available -

• `{i}quotly | {i}qbot <replying a message>`
    send stickers to current chat with @QuotlyBot.
    
"""

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from . import *


@ultroid_cmd(pattern="(quotly|qbot)$")
async def _(event):
    if not event.reply_to_msg_id:
        return await eor(event, "```Reply to any user message.```")
    reply_message = await event.get_reply_message()
    chat = "@QuotLyBot"
    reply_message.sender
    ac = await eor(event, "```Making a Quote```")
    async with ultroid_bot.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1031952739)
            )
            await ultroid_bot.forward_messages(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            return await event.reply("```Please unblock @QuotLyBot and try again```")
        if response.text.startswith("Hi!"):
            await eor(
                event,
                "```Can you kindly disable your forward privacy settings for good?```",
            )
        else:
            await ac.delete()
            await ultroid_bot.send_message(event.chat_id, response.message)


HELP.update({f"{__name__.split('.')[1]}": f"{__doc__.format(i=Var.HNDLR)}"})
