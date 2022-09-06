import json
import datetime
shop = json.loads(input())
params = []
for i in range(5):
	params.append(input().split(' '))
params_dict = dict()
for param in params:
    name, attrib = param
    if name in ('PRICE_LESS_THAN', 'PRICE_GREATER_THAN'):
        params_dict.setdefault(name, int(attrib))
    if name in ('DATE_AFTER', 'DATE_BEFORE'):
        params_dict.setdefault(name, datetime.datetime.strptime(attrib, '%d.%m.%Y').date())
    if name == 'NAME_CONTAINS':
        params_dict.setdefault(name, attrib.lower())

result = []

for article in shop:
    id_of_a = article['id']
    name = article['name']
    price = article['price']
    date = article['date']
    if params_dict['PRICE_LESS_THAN'] >= price >= params_dict['PRICE_GREATER_THAN'] \
            and name.lower().find(params_dict['NAME_CONTAINS']) >= 0 \
            and params_dict['DATE_BEFORE'] >= datetime.datetime.strptime(date, '%d.%m.%Y').date() >= params_dict['DATE_AFTER']:
        result.append({'id':id_of_a, 'name': name, 'price': price, 'date': date})

result.sort(key=lambda x: x['id'])
json_res = json.dumps(result)
print(json_res)
