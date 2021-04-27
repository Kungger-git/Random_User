import pandas as pd
import os
import json


def view(filename='users.csv'):
    if os.path.exists(filename):
        source = read_json()

        df = pd.read_csv(os.path.join(os.getcwd(), filename), encoding='utf-8')
        pd.set_option('display.max_rows', None)

        headers = []
        for element in source['view']:
            for key in element:
                if not element[key]:
                    headers.append(key)

        print(df.drop(headers, axis=1))


def read_json(filename='jView.json'):
    with open(filename, 'r', encoding='utf-8') as j_source:
        user_source = json.load(j_source)
    return user_source


if __name__ == '__main__':
    view()
