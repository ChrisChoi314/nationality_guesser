import json
import re
import requests

def repeat_get(url):
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1788.0'}
    r = None
    while r is None or r.status_code != 200:
        print(f'Getting {url}')
        r = requests.get(url, headers=headers)
    return r.text

text = repeat_get('https://forebears.io/countries')
countries = re.findall('\\<a href\\=\\"([A-Za-z\\-\\_ ]+)\\"\\>\\<svg class\\=\\"flag-icon\\"\\>', text)
# print(countries)

data = {'country': [], 'rank_in_country': [], 'surname': [], 'incidence': [], 'frequency_denom': []}

for country in countries:
    text = repeat_get(f'https://forebears.io/{country}/surnames')
    items = re.findall('\\<td\\>([0-9\\,]+)\\<\\/td\\>\\<td class\\=\\"sur\\"\\>\\<a href\\=\\"surnames/[A-Za-z\\-\\_]+">([A-Za-z\\-\\_ ]+)\\<\\/a\\>\\<\\/td\\>\\<td\\>([0-9\\,]+)\\<\\/td\\>\\<td\\>\\<span data\\-tooltip\\=\\"[0-9\\,\\.]+\\%\\"\\>[0-9\\,]+\\:([0-9\\,]+)\\<\\/span\\>\\<\\/td\\>', text)

    for item in items:
        rank = int(item[0].replace(',', ''))
        surname = item[1]
        incidence = int(item[2].replace(',', ''))
        frequency_denom = int(item[3].replace(',', ''))
        data['country'].append(country)
        data['rank_in_country'].append(rank)
        data['surname'].append(surname)
        data['incidence'].append(incidence)
        data['frequency_denom'].append(frequency_denom)

with open('data/database.json', 'w') as f:
    f.write(json.dumps(data))
    f.write('\n')
