import html
import json
import re
import requests


def repeat_get(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1788.0'}
    r = None
    while r is None or r.status_code != 200:
        print(f'Getting {url}')
        r = requests.get(url, headers=headers)
    return r.text


text = repeat_get('https://forebears.io/countries')
countries = re.findall(
    '\\<a href\\=\\"(((?!\\").)+)\\"\\>\\<svg class\\=\\"flag-icon\\"\\>', text)
country_names = re.findall('\\</use\\>\\</svg\\>(((?!\\").)+)\\</a\\>', text)

countries = [x[0] for x in countries]
print(countries)

country_names = [x[0] for x in country_names]
print(country_names)

data = {'country': [], 'country_name': [], 'rank_in_country': [],
        'surname': [], 'incidence': [], 'frequency_denom': []}

i = 0
for country in countries:
    text = repeat_get(f'https://forebears.io/{country}/surnames')
    items = re.findall('\\<td\\>([0-9\\,]+)\\<\\/td\\>\\<td class\\=\\"sur\\"\\>\\<a href\\=\\"surnames/(((?!\\").)+)">(((?!\\<).)+)\\<\\/a\\>\\<\\/td\\>\\<td\\>([0-9\\,]+)\\<\\/td\\>\\<td\\>\\<span data\\-tooltip\\=\\"[0-9\\,\\.]+\\%\\"\\>[0-9\\,]+\\:([0-9\\,]+)\\<\\/span\\>\\<\\/td\\>', text)

    prev_rank = 0
    for item in items:
        rank = int(item[0].replace(',', ''))
        if rank < prev_rank and prev_rank != 0:
            break
        surname = item[3]
        surname = html.unescape(surname)
        incidence = int(item[5].replace(',', ''))
        frequency_denom = int(item[6].replace(',', ''))
        data['country'].append(country)
        data['country_name'].append(country_names[i])
        data['rank_in_country'].append(rank)
        data['surname'].append(surname)
        data['incidence'].append(incidence)
        data['frequency_denom'].append(frequency_denom)

        prev_rank = rank
    i+=1

with open('data/database_surnames.json', 'w') as f:
    f.write(json.dumps(data))
    f.write('\n')
