import json
import random
import datetime
from pymongo import MongoClient


def get_collection():
    client = MongoClient('ds153677.mlab.com', 53677)
    db = client.game_history
    db.authenticate("Vincent Shen", "kuroKi_87B", mechanism='SCRAM-SHA-1')
    collection = db.records_20161127
    return collection


def get_local_collection():
    local_collection = open('csis3300_test.json')
    documents = json.load(local_collection)
    return documents


def random_drop_attribute(documents):
    for document in documents:
        # Randomly drop attributes
        for i in range(0, len(document['player'])):
            random_drop_gender = random.randint(0, 7)
            random_drop_nation = random.randint(0, 7)
            if random_drop_gender <= 1:
                del document['player'][i]['gender']
                print("Player " + str(i + 1) + " gender dropped")
            if random_drop_nation <= 1:
                del document['player'][i]['nation']
                print("Player " + str(i + 1) + " nation dropped")


def datetime_converter(documents):
    for document in documents:
        document['time_start'] = document['date'] + " " + document['time_start']
        document['time_end'] = document['date'] + " " + document['time_end']
        document['time_start'] = datetime.datetime.strptime(
            document['time_start'], "%m/%d/%Y %H:%M"
        )
        document['time_end'] = datetime.datetime.strptime(
            document['time_end'], "%m/%d/%Y %H:%M:%S"
        )
        del document['date']


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


def dump_to_update(documents):
    with open('csis3300_test_update.json', 'w') as collection_update:
        json.dump(records, collection_update)


def insert_to_remote(documents):
    remote_reocrds = get_collection()
    results = remote_reocrds.insert_many(documents)
    for obj_id in results.inserted_ids:
        print(obj_id)


if __name__ == '__main__':
    records = get_local_collection()
    datetime_converter(records)
    random_drop_attribute(records)
    winning_settings(records)
    print_collection(records)
    insert_to_remote(records)
