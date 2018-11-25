#!/usr/bin/env python

# open_in_tabs.py

import webbrowser
import sys

google = webbrowser.get('google')

for url in sys.stdin.readlines():
    url = url.rstrip("\n")
    google.open_new_tab(url)
