from pyrogram import Client

api_id = 2486084
api_hash = "493bc2bd-dd04-4d0b-b767-b30dbc2cff03"

with Client("my_account", api_id, api_hash) as app:
    app.send_message("me", "Greetings from **Pyrogram**!")
