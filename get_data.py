import requests, json
from datetime import datetime
import time

now = datetime.now()
current_time = now.strftime("%d/%m/%Y %H:%M:%S")
print(current_time, ": Running owntracks data fetching script")

server = 'http://152.67.97.63:8083/api/0/'
path = '../librephotos-frontend/src/owntracks-data/'
res = requests.get(server+'list/')

data = res.json()
with open(path+'users_list.json', 'w', encoding='utf-8') as list_file:
    json.dump(data, list_file, ensure_ascii=False, indent=4)

for results in data:
    for user in data[results]:
        params = {
            'user' : user,
            'device': user+'phone',
            'from': '2015-09-01'
        }
        l = requests.get(server+'locations', params=params)
        locations = l.json()

        with open(path+'%s_data.json' % user, 'w', encoding='utf-8') as f:
            json.dump(locations, f, ensure_ascii=False, indent=4)

res_last = requests.get(server+'last/')
last = res_last.json()
with open(path+'last.json', 'w', encoding='utf-8') as last_file:
    json.dump(last, last_file, ensure_ascii=False, indent=4)

time.sleep(8640)
