import json

with open('data/database.json', 'r') as f:
    data = json.load(f)

print(f'Total: {len(data["surname"])}')

by_country = {}
for i in range(len(data['surname'])):
    item = {k: data[k][i] for k in data}
    if item['country'] not in by_country:
        by_country[item['country']] = []
    by_country[item['country']].append(item)

print(f'Total per country:')
name = input('Enter country you want to see last names of: \n') 
for country, items in by_country.items():
    if country == name:
       print([x['surname'] for x in items])
    #print(f'{country}: {len(items)}')
