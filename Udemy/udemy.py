#! python3
#! udemySearch.py - Searches udemy.com based on args provided or clipboard.
#! https://www.udemy.com/courses/search/?src=ukw&q=

import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
    # Get address from command line.
    search = ' '.join(sys.argv[1:])
else:
    # Get address for clipboard.
    search = pyperclip.paste()

webbrowser.open('https://www.udemy.com/courses/search/?src=ukw&q=' + search)