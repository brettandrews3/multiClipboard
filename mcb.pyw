#! python3
# This is a multi-clipboard program I'm making with Automate the Boring Stuff
# The .pyw file extension => no terminal window pops when running program
# Usage: py.exe mcb.pyw save <keyword> - Saves clips to keyword
# py.exe mcb.pyw list - Loads all keywords to clipboard

import shelve, pyperclip, sys   # save clipboard text, copy/paste, read cmd line args

mcbShelf = shelve.open('mcb')

# Save clipboard content
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    # List keywords and load content
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()