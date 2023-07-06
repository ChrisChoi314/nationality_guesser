import json

with open('data/database_surnames.json', 'r') as f:
    data = json.load(f)

no_dups = {'country': [], 'country_name': [], 'rank_in_country': [],
           'surname': [], 'incidence': [], 'frequency_denom': []}

for i in range(len(data['surname'])):
    item = {k: data[k][i] for k in data}

    country, country_name, rank, surname, incidence, frequency_denom = item['country'], item[
        'country_name'], item['rank_in_country'], item['surname'], item['incidence'], item['frequency_denom']

    if surname not in no_dups['surname']:
        no_dups['country'].append(country)
        no_dups['country_name'].append(country_name)
        no_dups['rank_in_country'].append(rank)
        no_dups['surname'].append(surname)
        no_dups['incidence'].append(incidence)
        no_dups['frequency_denom'].append(frequency_denom)
    else:
        idx = no_dups['surname'].index(surname)
        if no_dups['incidence'][idx] <= incidence:
            del no_dups['country'][idx]
            del no_dups['country_name'][idx]
            del no_dups['rank_in_country'][idx]
            del no_dups['surname'][idx]
            del no_dups['incidence'][idx]
            del no_dups['frequency_denom'][idx]

            no_dups['country'].append(country)
            no_dups['country_name'].append(country_name)
            no_dups['rank_in_country'].append(rank)
            no_dups['surname'].append(surname)
            no_dups['incidence'].append(incidence)
            no_dups['frequency_denom'].append(frequency_denom)

with open('data/database_surnames_no_duplicates.json', 'w') as f:
    f.write(json.dumps(no_dups))
    f.write('\n')
