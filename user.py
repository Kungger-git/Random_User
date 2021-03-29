import requests
import json
import csv
import random
import argparse
import pandas as pd


class Preview_User:

    def __init__(self, json_user):
        self.json_user = json_user

    def print_user(self):
        for info in self.json_user:
            name = []
            for element in info['name']:
                name.append(info['name'][element])

            print(f"Hello, I'm {' '.join(name)}")
        return Record_User_Data(self.json_user, ' '.join(name[1:])).write_user()


class Record_User_Data:

    def __init__(self, source, username):
        self.source = source
        self.username = username

    def write_user(self):
        with open('user.csv', 'a', encoding='utf-8') as f:
            writer = csv.writer(f, dialect='excel')

            for dict in self.source:
                df = pd.read_csv('user.csv', encoding='utf-8', delimiter=',')
                data = [len([list(row) for row in df.values]),
                        random.randint(10000, 99999), self.username]
                data.extend((dict['dob']['age'], dict['gender'].capitalize()))

                location = ['city', 'state', 'country']
                for element in dict['location']:
                    if element in location:
                        data.append(dict['location'][element])

                data.extend((dict['email'], dict['phone']))

                login = ['username', 'password']
                for info in dict['login']:
                    if info in login:
                        data.append(dict['login'][info])

                writer.writerows([data])


class Get_Users:

    def __init__(self, user_range):
        for num in user_range:
            self.user_range = num

    def random_user_api(self):
        try:
            with open('user.csv', 'w', encoding='utf-8') as f:
                headers = ['#', 'ID', 'Name', 'Age', 'Gender', 'City',
                           'State', 'Country', 'Email', 'Phone', 'Username', 'Password']
                wr = csv.writer(f, dialect='excel')
                wr.writerow(headers)

            while self.user_range > 0:
                with requests.get('https://randomuser.me/api') as response:
                    source = json.loads(response.text)

                self.user_range -= 1
                Get_Users([self.user_range]).user_json(source['results'])
        except requests.HTTPError as err:
            print('Something went wrong! {}'.format(err))

    def user_json(self, j_source):
        with open('random_user.json', 'w', encoding='utf-8') as f_source:
            json.dump(j_source, f_source, indent=2)

        return Preview_User(j_source).print_user()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
                                     description='Writes Random User Data.')

    parser.add_argument('range',
                        nargs=1, metavar='RANGE',
                        type=int, action='store',
                        help='Enter range of how many users to write.')

    args = parser.parse_args()

    if args.range:
        Get_Users([x for x in args.range]).random_user_api()
