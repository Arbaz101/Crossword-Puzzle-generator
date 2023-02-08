import json

f = open('Crossword JSON generator\data.json')

data = json.load(f)

print(len(data))

