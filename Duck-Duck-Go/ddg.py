#! python3
#! duckDuckGoSearch.py - Launches a DDG search from the command line or clipboard
#! Search for "hello" == https://duckduckgo.com/?q=hello&va=b&t=hr&ia=web

import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
    # Get address from command line.
    search = " ".join(sys.argv[1:])
else:
    # Get address for clipboard.
    search = pyperclip.paste()

webbrowser.open("https://duckduckgo.com/?q=" + search)
