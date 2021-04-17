#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import subprocess


def update_check():
    update = subprocess.Popen(["apt-get --just-print upgrade"], shell=True, stdout=subprocess.PIPE)
    out = update.stdout.read()
    send_message(out)


def send_message(out):
    mTitle = "New updates are available"
    mText = "Following updates are available:\n {updates}".format(updates = out)
    os.system('notify-send "' + mTitle + '" "' + mText + '"')
    print("\n\n", out)


update_check()
