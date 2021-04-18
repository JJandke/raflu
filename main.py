#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import subprocess


def update_check():
    update = subprocess.Popen(["apt-get --just-print upgrade"], shell=True, stdout=subprocess.PIPE)
    out = "%s" % (update.stdout.read())
    format_output(out)


def format_output(out):
    locator = out.find("und") +4
    i = 0
    update_count = ""
    while not out[locator + i].isspace():
        digit = out[locator + i]
        update_count = update_count + digit
        i = i + 1

    print(update_count)


def send_message(out):
    mTitle = "New updates are available"
    mText = "Following updates are available:\n {updates}".format(updates=out)
    os.system('notify-send "' + mTitle + '" "' + mText + '"')
    print("\n\n", out)


update_check()
