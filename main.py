import json
import random


def random_drop_attribute(documents):
    for document in documents:
        # Randomly drop attributes
        for i in range(0, len(document['player'])):
            random_drop_gender = random.randrange(7)
            random_drop_nation = random.randrange(7)
            random_drop_birthday = random.randrange(7)
            if random_drop_gender <= 1:
                del document['player'][i]['gender']
                print("Player " + str(i + 1) + " gender dropped")
            if random_drop_nation <= 1:
                del document['player'][i]['nation']
                print("Player " + str(i + 1) + " nation dropped")
            if random_drop_birthday <= 1:
                del document['player'][i]['date_of_birth']
                print("Player " + str(i + 1) + " birthday dropped")


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


def player_2_data(documents):
    # Check the results
    for document in documents:
        if len(document['player']) > 1:
            document['player'][1]['game_played'] = document['player'][0]['game_played']
            document['player'][1]['wins'] = document['player'][0]['loses']
            document['player'][1]['loses'] = document['player'][0]['wins']
            print("player 1: ")
            print(document['player'][0])
            print("player 2: ")
            print(document['player'][1])
        else:
            print("player 1: ")
            print(document['player'][0])


def print_collection(documents):
    for document in documents:
        print(document)

if __name__ == '__main__':
    with open('csis3300_test.json') as collection:
        records = json.load(collection)
        winning_settings(records)
        print_collection(records)
