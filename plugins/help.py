from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"📚 Panduan Bot.\n\n➠ Kirimkan link video yang ingin kamu download.\n\n➠ Tentukan resolusi video yang ingin kamu download.\n\n➠ Bot ini tidak dapat mendownload video dari link playlist youtube."
    await message.reply_text(helptxt)
