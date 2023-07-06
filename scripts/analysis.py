import json

with open('data/database_surnames.json', 'r') as f:
    data = json.load(f)

with open('data/database_surnames_no_duplicates.json', 'r') as f:
    data_pruned = json.load(f)


by_country = {}

for i in range(len(data_pruned['surname'])):
    item = {k: data_pruned[k][i] for k in data_pruned}
    if item['country_name'] not in by_country:
        by_country[item['country_name']] = []
    by_country[item['country_name']].append(item)
alphabetical_countries = []
for country_name, items in by_country.items():
    alphabetical_countries += [country_name]
alphabetical_countries.sort()
'''
print('number of surnames in unpruned list: ', len(data['country']))
print('number of surnames in pruned list: ', len(data_pruned['country']))

print(f'Total per country, pruned:')
name = input('Enter country you want to see last names of: \n') 
for country, items in by_country.items():
    if country == name:
       print([x['surname'] for x in items])
    #print(f'{country}: {len(items)}')
'''

print('What would you like to do? \n1. If you would like to see all of the names from a particular country, enter \'country\', and then enter the country\'s name.\n2. If you would like to see what the countries are, enter \'list\'. The displayed countries are in the format that this program recieves them, so make sure you spell them right. (Note, Barbados and North Korea are notably missing, I sincerely apologize to all Barbadians and North Koreans)\n3. If you would like to search for a last name and see what country it is from, then enter \'name\' and then the surname you had in mind.\n4. Type \'help\' for help')
is_running = True
while is_running:
    inp = input()
    if inp == 'list':
        print(alphabetical_countries)
    if inp == 'country':
        inp = input(f'What country would you like to see the surnames of?')
        for country, items in by_country.items():
            if country == inp:
                print([x['surname'] for x in items])
    if inp == 'name':
        inp = input('Which last name would you like to find?')
        if inp not in data_pruned['surname']:
            print('Not in the database')
        else:
            idx = data_pruned['surname'].index(inp)
            print(
                f"Country: {data_pruned['country_name'][idx]}, Rank: {data_pruned['rank_in_country'][idx]}, Frequency: {data_pruned['incidence'][idx]}")
    if inp == 'help':
        print('\n1. If you would like to see all of the names from a particular country, enter \'country\', and then enter the country\'s name.\n2. If you would like to see what the countries are, enter \'list\'. The displayed countries are in the format that this program recieves them, so make sure you spell them right. (Note, Barbados and North Korea are notably missing, I sincerely apologize to all Barbadians and North Koreans)\n3. If you would like to search for a last name and see what country it is from, then enter \'name\' and then the surname you had in mind.')
