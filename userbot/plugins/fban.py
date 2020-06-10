"""Globally Ban users from all the
Group Administrations bots where you are SUDO
Available Commands:
.fban REASON
.unfban REASON"""
from telethon import events
import asyncio
from uniborg.util import admin_cmd


@command(outgoing=True, pattern=r"^.fban ?(.*)", allow_sudo=True)
async def _(event):
    if Config.F_BAN_LOGGER_GROUP is None:
        await event.edit("ENV VAR is not set. This module will not work.")
        return
    if event.fwd_from:
        return
    reason = event.pattern_match.group(1)
    if event.reply_to_msg_id:
        r = await event.get_reply_message()
        if r.forward:
            r_from_id = r.forward.from_id or r.from_id
        else:
            r_from_id = r.from_id
        await borg.send_message(
            Config.F_BAN_LOGGER_GROUP,
            "!fban user {}".format(r_from_id, reason)
        )
    await event.delete()


@command(outgoing=True, pattern=r"^.unfban ?(.*)", allow_sudo=True)
async def _(event):
    if Config.F_BAN_LOGGER_GROUP is None:
        await event.edit("ENV VAR is not set. This module will not work.")
        return
    if event.fwd_from:
        return
    reason = event.pattern_match.group(1)
    if event.reply_to_msg_id:
        r = await event.get_reply_message()
        r_from_id = r.from_id
        await borg.send_message(
            Config.F_BAN_LOGGER_GROUP,
            "!unfban user {}".format(r_from_id, reason)
        )
    await event.delete()

    if event.fwd_from:
        return
    reason = event.pattern_match.group(1)
    if event.reply_to_msg_id:
        r = await event.get_reply_message()
        if r.forward:
            r_from_id = r.forward.from_id or r.from_id
        else:
            r_from_id = r.from_id
        await borg.send_message(
            Config.F_BAN_LOGGER_GROUP,
            "!fban user {}".format(r_from_id, reason)
        )
    await event.delete()


@command(outgoing=True, pattern=r"^.unfban ?(.*)", allow_sudo=True)
async def _(event):
    if Config.F_BAN_LOGGER_GROUP is None:
        await event.edit("ENV VAR is not set.")
