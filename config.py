#!/usr/bin/env python3

# BOT_TOKEN contains the token that BotFather gave to you
BOT_TOKEN = "0123456789:mY-C00L-t0K3n-w1ll-83-plac3d-h3re"

# ADMINS_ID is a list of User ID that can use privileged commands.
# Put admins id between brakets separated by a comma
ADMINS_ID = [123456789, 987654321]

# This message will popup when someone type /start
START_MSG = """A Python 3 version of @JimmySanBot, but written in Python 3 by @a_lombax.
This bot replies with 'X merda' where X is a trigger listed in a file.
Try it by writing 'I Love JS'.
Send /list to get a list of the current triggers."""

# The filename where are stored the triggers, separated by a newline
FILENAME = "merde.txt"

# The unicode emoji of the poop
POOP = b"\\U0001F4A9".decode('unicode-escape')

# The string conatins the sentence that the bot will send if he find one trigger.
# The first "%s" will be replaced with the found trigger
# The second "%s" will be replaced with the emoji
SINGLE_TRIGGER_PHRASE = "%s merda %s"
MORE_TRIGGERS_PHRASE = "%s merde %s"
