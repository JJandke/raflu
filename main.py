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
    j = 0
    stop = "n"
    update_count_rev = ""
    while stop not in out[update_locator + j]:
        update_digit = out[update_locator + j]
        update_count_rev = update_count_rev + update_digit
        j = j - 1

    update_count = update_count_rev[::-1]
    send_message(update_count, restricted_count)


def send_message(update_count, restricted_count):
    duration = "50000"
    m_title = "Updates are available"
    m_text = "There are {0} updates aviable\n{1} more are retained".format(update_count, restricted_count)
    os.system('notify-send "' + m_title + '" "' + m_text + '" "-t" "' + duration + '" ')


update_check()
