import json
import random
import datetime


def get_collection():
    collection = open('csis3300_test.json')
    documents = json.load(collection)
    return documents


def random_drop_attribute(documents):
    for document in documents:
        # Randomly drop attributes
        for i in range(0, len(document['player'])):
            random_drop_gender = random.randint(0, 7)
            random_drop_nation = random.randint(0, 7)
            random_drop_birthday = random.randint(0, 7)
            if random_drop_gender <= 1:
                del document['player'][i]['gender']
                print("Player " + str(i + 1) + " gender dropped")
            if random_drop_nation <= 1:
                del document['player'][i]['nation']
                print("Player " + str(i + 1) + " nation dropped")
            if random_drop_birthday <= 1:
                del document['player'][i]['date_of_birth']
                print("Player " + str(i + 1) + " birthday dropped")


def datetime_converter(documents):
    for document in documents:
        document['date'] = datetime.datetime.strptime(document['date'], "%m/%d/%Y").date().isoformat()
        document['time_start'] = datetime.datetime.strptime(document['time_start'], "%H:%M").time().isoformat()
        document['time_end'] = datetime.datetime.strptime(document['time_end'], "%H:%M:%S").time().isoformat()
        for i in range(0, len(document['player'])):
            document['player'][i]['date_of_birth'] = datetime.datetime.strptime(
                document['player'][i]['date_of_birth'],
                "%Y-%m-%d"
            ).date().isoformat()


def winning_settings(documents):
    for document in documents:
        winner_index = random.randint(0, 1)
        if len(document['player']) > 1:
            document['winner'] = document['player'][winner_index]['id']
        else:
            if winner_index == 0:
                document['winner'] = document['player'][winner_index]['id']
            else:
                document['winner'] = "AI"
        for i in range(0, len(document['player'])):
            winning_rate = random.uniform(0.1, 0.99)
            winning_rate = round(winning_rate, 4)
            document['player'][i]['winning_rate'] = winning_rate


def print_collection(documents):
    for document in documents:
        print(document)

if __name__ == '__main__':
    records = get_collection()
    datetime_converter(records)
    random_drop_attribute(records)
    winning_settings(records)
    print_collection(records)
    with open('csis3300_test_update.json', 'w') as collection_update:
        json.dump(records, collection_update)
