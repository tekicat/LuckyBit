import secrets, os
import bit
from telegram import Bot
import datetime
now = datetime.datetime.now()
bot = Bot(os.getenv('TG_TOKEN'))
chat_id = os.getenv('CHAT_ID')

if (now.hour == 9) or (os.getenv('USER','') == "me") :
    bot.send_message(chat_id=chat_id, text="Running Fine for {}".format(now.date()))

k = 1
while k<20000:
    pk = bit.Key.from_int(secrets.randbits(256))
    # print(pk.address + ' - ' + pk.get_balance('usd') + ' - usd ')
    try:
        if not pk.get_balance('usd') != 0 :
            msg = "{} - {} USD\nPrivateKey (hex): {}\nPrivateKey (wif): {}".format(pk.address,pk.get_balance('usd'),pk.to_hex(),pk.to_wif())
            bot.send_message(chat_id=chat_id, text=msg)
    except e:
        print("Ooops! Seems like issue")
    k += 1