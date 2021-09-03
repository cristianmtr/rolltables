import json
import traceback
import sys

try:

    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()
        lines = [l.strip() for l in lines]

    obj = {
        "id": sys.argv[2],
        "title": sys.argv[3],
        "roll": lines
    }

    with open("out.js", "w") as f:
        f.write(json.dumps(obj))

except Exception as e:
    print(traceback.format_exc())
    print(f'python parse_file.py file_location id(swn_rewards) title(Rewards)')
