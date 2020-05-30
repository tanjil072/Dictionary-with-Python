import json
import re

with open('my_dictionary_database.json') as f:
    x = json.load(f)

data = {}
pattern = r'[\.]*'

new = {}
for word, mean in x.items():
    lis = []
    for s in mean:
        s = re.sub(pattern, '', s)
        lis.append(s)
    new[word] = lis

with open('my_dictionary_database.json', 'w') as f:
    json.dump(new, f, indent=2, sort_keys=True)
