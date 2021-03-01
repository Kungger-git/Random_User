import json
import dl_api
import time


def get_user(json_user):
    for info in json_user:
        name = '{} {} {}'.format(info['name']['title'],
                                 info['name']['first'],
                                 info['name']['last'])
        age = info['dob']['age']
        country = info['location']['country']

    print(f"Hello, I'm {name}, and I'm {age} years old. I live in {country}")


if __name__ == '__main__':
    while True:
        dl_api.random_user_api()
        with open('random_user.json') as f:
            data = json.load(f)
            get_user(data)
        time.sleep(3)