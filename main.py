import json
import random

with open("csis3300_test.json") as collection:
    documents = json.load(collection)
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

        # Check the results
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
