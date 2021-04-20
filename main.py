#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import subprocess


def update_check():
    update = subprocess.Popen(["apt-get --just-print upgrade"], shell=True, stdout=subprocess.PIPE)
    out = "%s" % (update.stdout.read())
    format_output(out)


def format_output(out):
    # restricted count
    restricted_locator = out.find("und") + 4
    i = 0
    restricted_count = ""
    while not out[restricted_locator + i].isspace():
        restricted_digit = out[restricted_locator + i]
        restricted_count = restricted_count + restricted_digit
        i = i + 1

    # update count
    update_locator = out.find("neu") - 18
    # update_count = out[update_locator]
    j = 0
    stop = "n"
    update_count = ""
    while not stop in out[update_locator + j]:
        update_digit = out[update_locator + j]
        update_count = update_count + update_digit
        j = j - 1

    print(restricted_count, update_count)


def send_message(out):
    mTitle = "New updates are available"
    mText = "Following updates are available:\n {updates}".format(updates=out)
    os.system('notify-send "' + mTitle + '" "' + mText + '"')
    print("\n\n", out)


update_check()
