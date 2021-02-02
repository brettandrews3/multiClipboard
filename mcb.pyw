#! python3
# This is a multi-clipboard program I'm making with Automate the Boring Stuff
# The .pyw file extension => no terminal window pops when running program
# Usage: py.exe mcb.pyw save <keyword> - Saves clips to keyword
# py.exe mcb.pyw list - Loads all keywords to clipboard

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

#TODO: save clipboard content

#TODO: list keywords and load content

mcbShelf.close()