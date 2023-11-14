import os
import sys
import asyncio
import re
from random import choice
from pyrogram import Client, filters
from pyrogram.types import Message
from cache.data import *
from Zaid.database.rraid import *
from Zaid import SUDO_USER
from pyrogram import Client, errors, filters
from pyrogram.types import ChatPermissions, Message
DEVS = int(5174492401)
from Zaid.helper.PyroHelpers import get_ub_chats
from Zaid.modules.basic.profile import extract_user, extract_user_and_reason
SUDO_USERS = SUDO_USER
from .replyraid import RAIDS



@Client.on_message(
    filters.command(["replyraid", "rraid"], ".") & (filters.me | filters.user(SUDO_USER))
)
async def replyraid(client: Client, message: Message):
    args = await extract_user(message)
    reply = message.reply_to_message
    ex = await message.edit_text("`Processing...⚡️𝐒 𝐘 𝐍 𝐀 𝐗⚡️`")
    if args:
        try:
            user = await client.get_users(args)
        except Exception:
            await ex.edit(f"`Please specify a valid user!⚡️𝐒 𝐘 𝐍 𝐀 𝐗⚡️`")
            return
    elif reply:
        user_id = reply.from_user.id
        user = await client.get_users(user_id)
    else:
        await ex.edit(f"`Please specify a valid user!⚡️𝐒 𝐘 𝐍 𝐀 𝐗⚡️`")
        return
    if user.id == client.me.id:
        return await ex.edit("**Okay Sure.. 🐽⚡️𝐒 𝐘 𝐍 𝐀 𝐗⚡️**")
    elif user.id == SUDO_USERS:
        return await ex.edit("**Okay But Failed Because this user in sudos.. 🐽⚡️𝐒 𝐘 𝐍 𝐀 𝐗⚡️**")
    elif user.id == VERIFIED_USERS:
        return await ex.edit("**Chal Chal Baap ko Mat sikha.. 🐽⚡️𝐒 𝐘 𝐍 𝐀 𝐗⚡️**")
    try:
        if user.id in (await get_rraid_users()):
           await ex.edit("Replyraid is activated on this user")
           return
        await rraid_user(user.id)
        RAIDS.append(user.id)
        await ex.edit(f"[{user.first_name}](tg://user?id={user.id}) Activated ReplyRaid!")
    except Exception as e:
        await ex.edit(f"**ERROR:** `{e}`")
        return
