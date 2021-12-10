# Search-Tools

Uses Python 3 and bat files to search various websites directly from the start menu or run dialogue. 

Installation:

1: Install newest version of python from https://www.python.org/. Make sure to check the box to add Python to the PATH variable.

2: Download this repository and unpack it to the root of your C:\ drive.

3: Open powershell and run the following command:

    pip install -r C:\Search-Tools\packages.md

4: Run setup.py.

5: Reboot.

Usage:

Enter one of the commands into the Start Menu or Run dialogue (Win + r) to search the associated webpage. Arguments provided will be used as the search term. 

If no args are provided, the program will use whatever is copied to your clipboard as the search term.

"google hello" will open a new browser tab and search "hello" on google.com

"google" will open a new browser tab and search whatever you have stored in your clipboard on google.com

Commands:

ddb - Searches DNDBEYOND

ddg - Searches DuckDuckGo

google - Searches Google

lucky - Searches Google and opens the first 5 results in new tabs.

mapIt - Searches Google Maps

snow - Searches Service Now

udemy - Searches Udemy

Known issue:

Sometimes Windows will not detect the bat file via the Start Menu. Use the Run dialogue (Win + r) to run searches instead.
