#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import subprocess


def update_check():
    update = subprocess.Popen(["apt-get --just-print upgrade"], shell=True, stdout=subprocess.PIPE)
    out = "%s" % (update.stdout.read())
    format_output(out)


def format_output(out):
    a = out.find("und")
    out_number = a +4
    count = out[out_number]
    print(count)


def send_message(out):
    mTitle = "New updates are available"
    mText = "Following updates are available:\n {updates}".format(updates=out)
    os.system('notify-send "' + mTitle + '" "' + mText + '"')
    print("\n\n", out)


update_check()
