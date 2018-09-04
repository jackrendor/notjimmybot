#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from time import sleep
from config import *

# Global list that will contain the triggers
MERDE = []

def RED(text):
    return "\033[1;37;41m%s\033[0m" % str(text)

def GREEN(text):
    return "\033[1;37;41m%s\033[0m" % str(text)

def is_admin(user_id=None):
    return bool(user_id in ADMINS)

def del_char(text):
    """This function deletes all the special chars
    inside the string"""
    UNCHAR = "\"',.;:-_#*?!^&/\\$°"
    result = ""
    for char in text:
        if char not in UNCHAR:
            result+=char
    return result

def load_merde():
    global MERDE
    # Resetting the list to an empty one.
    MERDE = []
    try:
        with open(FILENAME, "r") as f:
            for line in f:
                # trim the last part (it's \n)
                item = line[:-1]
                # append the rest of the line
                MERDE.append(item)
    except FileNotFoundError:
        print(RED(" '%s' FILE DOES NOT EXIST!!!" % FILENAME))
        exit()
    except IsADirectoryError:
        print(RED("ARE YOU KIDDING ME?! '%s' IS A DIRECTORY!!" % FILENAME))
        exit()
    except PermissionError:
        print(RED("CANNOT READ '%s': PERMISSION DENIED" % FILENAME))

def handler_start(bot, update):
    sleep(1)
    send = update.message.reply_text
    send(START_MSG)

def handler_list(bot, update):
    send = update.message.reply_text
    send('\n'.join(MERDE))

def handler_reload(bot, update):
    """ reload the list """
    user_id = update.message.from_user.id
    send = update.message.reply_text

    if is_admin(user_id):
        load_merde()
        send("Reload completed")
    else:
        sleep(1)
        send("Nope.")

def normal_msg(bot, update):
    """Handler to check for every normal message"""
    msg = update.message.text
    msg = msg.lower()
    msg = del_char(msg).split(' ')
    send = update.message.reply_text
    
    triggers = []
    
    for item in MERDE:
        if item.lower() in msg:
            triggers.append(item)
    if len(triggers) == 1:
        send("%s merda %s" % (triggers[0], POOP))
    elif len(triggers) > 1:
        # s_triggers -> string_triggers
        s_triggers = ", ".join(triggers)
        send("%s merde %s" % (s_triggers, POOP))

def main():
    """Start the bot."""
    updater = Updater(BOT_TOKEN)
    
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", handler_start))
    dp.add_handler(CommandHandler("list", handler_list))
    dp.add_handler(CommandHandler("reload", handler_reload))
    dp.add_handler(MessageHandler(Filters.text, normal_msg))

    load_merde()

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
