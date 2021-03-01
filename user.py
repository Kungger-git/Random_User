import json
import mk_json
import time


class my_json:

    def __init__(self, json_user):
        self.json_user = json_user


    def get_user(self):
        for info in self.json_user:
            name = '{} {} {}'.format(info['name']['title'],
                                    info['name']['first'],
                                    info['name']['last'])
            age = info['dob']['age']
            country = info['location']['country']

        print(f"Hello, I'm {name}, and I'm {age} years old. I live in {country}")


if __name__ == '__main__':
    while True:
        mk_json.random_user_api()
        with open('random_user.json') as f:
            data = json.load(f)
            my_json(data).get_user()
        time.sleep(1.5)