#! python3
# mcb.pyw - Save and loads pieces of tet to the clipboards
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword
#        py.exe mcb.pyw <keyword> - Loads keyword to clipboard
#        py.exe mcb.pyw list - loads all keywords to clipboard
#        py.exe mcb.pyw delete <keyword> - Deletes keyword from shelf
#        py.exe mcb.pyw deleteall - Deletes all keywords from shelve

import shelve, pyperclip, sys   # save clipboard text, copy/paste, read cmd line args

mcb_shelf = shelve.open('mcb')

# Save clipboard content
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcb_shelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    # List keywords and load content
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcb_Shelf.keys())))
    # To delete all arguments, run through the list of keys
    elif sys.argv[1].lower() =='deleteall':
        for keyword in list(mcb_shelf.keys()):
            del mcb_shelf[keyword]
    elif sys.argv[1] in mcb_shelf:
        pyperclip.copy(mcb_shelf[sys.argv[1]])
mcb_shelf.close()