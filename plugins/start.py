from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("š CHANNEL š", url="https://t.me/BeKing_Bots")],
        [InlineKeyboardButton(
            "š©āš» DEVELOPER", url="https://t.me/zxyune")]
    ])
    welcomed = f"š¤ Halo <b>{message.from_user.first_name}</b> selamat datang di youtube downloader bot.\n\nš Aku adalah bot yang dibuat untuk mengunduh video dari youtube.\n\nš Ketik /help untuk membaca panduan bot ini yah."
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
