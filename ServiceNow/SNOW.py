#! python3
#! SNOW.py - Searches Service Now based on args provided or clipboard.
#! https://servicenow.adventhealth.com/nav_to.do?uri=%2F$sn_global_search_results.do%3Fsysparm_search%3D

import sys, webbrowser, pyperclip

if len(sys.argv) > 1:
    # Get search from args.
    search = " ".join(sys.argv[1:])
else:
    # Get search from clipboard.
    search = pyperclip.paste()

webbrowser.open(
    f"https://servicenow.adventhealth.com/now/nav/ui/classic/params/target/incident_list.do%3Fsysparm_query%3DGOTO123TEXTQUERY321%253D{search}%255Eactive%253Dtrue%26sysparm_first_row%3D1%26sysparm_view%3D"
)
