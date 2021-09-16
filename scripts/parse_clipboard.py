import json
import traceback
import sys
import pyperclip

try:

    lines = pyperclip.paste().split("\n")
    lines = [l.strip().strip(',"') for l in lines]

    obj = {
        "id": sys.argv[1],
        "title": sys.argv[2],
        "roll": lines
    }
    content = json.dumps(obj, indent=4)
    pyperclip.copy(content)

except Exception as e:
    print(traceback.format_exc())
    print(f'python parse_clipboard.py id(swn_rewards) title(Rewards)')
