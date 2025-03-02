from Hack import bot
from telethon import events
OWNER_ID = 1786683163  
@bot.on(events.NewMessage)
async def on_pm_s(event):
    if not event.is_private:
        return
    if not event.sender_id == OWNER_ID:
        fwded_mesg = await event.forward_to(OWNER_ID, silent=True)
