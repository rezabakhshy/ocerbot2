from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Hey {}

Welcome to {}

I can extract text from images using OCR technology.

By REZA BAKHSH ZAII
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("CREATOR BOT ", url="https://t.me/REZABZ2")],
    ]
    # Rest Buttons
    buttons = [
        [
            InlineKeyboardButton("about", url="https://t.me/REZABZ2")
        ],
    ]

    # Help Message
    HELP = """
    SEND IMAGE 
    """

    # About Message
    ABOUT = """
    @REZABZ2
    """
