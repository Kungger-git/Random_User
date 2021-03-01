import json
import requests


def random_user_api():
    with requests.get('https://randomuser.me/api') as response:
        source = response.text
        response.raise_for_status()

    data = json.loads(source)

    with open('random_user.json', 'w') as f:
        f.write(json.dumps(data['results'], indent=2))
