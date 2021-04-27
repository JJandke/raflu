#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Note that this version only works for systems with English language!

import os
import subprocess


# Check if updates are available and format the output as string.
def update_check():
    update = subprocess.Popen(["apt-get --just-print upgrade"], shell=True, stdout=subprocess.PIPE)
    out = "%s" % (update.stdout.read())
    format_output(out)


def format_output(out):
    # restricted count
    # Search for "and" in the string passed by update_check() to go from there to the number of packages held back.
    restricted_locator = out.find("and") + 4
    i = 0
    restricted_count = ""
    while not out[restricted_locator + i].isspace():
        restricted_digit = out[restricted_locator + i]
        restricted_count = restricted_count + restricted_digit
        i = i + 1

    # update count
    # Search for "newly" to get the number of packages to install.
    # update_count_rev must be mirrored after that, otherwise the number of packages to install will be the wrong way around.
    update_locator = out.find("newly") - 18
    j = 0
    # Use the "n" of "\n" to recognize that the beginning of the line has been reached, since the formatting in update_check() outputs all lines as one.
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
    m_text = "There are {0} updates available\n{1} more are retained".format(update_count, restricted_count)
    os.system('notify-send "' + m_title + '" "' + m_text + '" "-t" "' + duration + '" ')


update_check()
