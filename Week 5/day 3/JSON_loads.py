# __Author__: Han
# __Date__: 2019/1/17

import json

with open('JSON_text', 'r') as f:
    data = f.read()
    data = json.loads(data)

print(data['name'])











