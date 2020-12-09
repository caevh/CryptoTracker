import requests
import json
from datetime import datetime

parameters = {
    "lat": 51.4545,
    'lon': -2.5879
}
response = requests.get('http://api.open-notify.org/iss-pass.json?', params=parameters)
response2 = requests.get('http://api.open-notify.org/astros.json')
astronaught = response2.json()
pass_time = response.json()['response']

risetimes = []
for d in pass_time:
    time = d['risetime']
    risetimes.append(time)

times = []
for rt in risetimes:
    time = datetime.fromtimestamp(rt)
    times.append(time)
    print(time)


def jprint(obj):
    risetimes = []
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

jprint(as)