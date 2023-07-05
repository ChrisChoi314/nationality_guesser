import html
import json

with open('data/database.json', 'r') as f:
    data = json.load(f)

no_dups = {}
for i in range(len(data['surname'])):
    item = {k: data[k][i] for k in data}
    if item['country'] not in by_country:
        by_country[item['country']] = []
    by_country[item['country']].append(item)
