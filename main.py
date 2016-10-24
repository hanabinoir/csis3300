import urllib.request as request
from lxml import html as html
import pymongo
import logging
import os
# import db

# database = db.DB()
# cursor = db.DB.getCursor(database)


def get_local_profile():
    client_local = pymongo.MongoClient('localhost', 27017)
    db_local = client_local['local']
    collection_profile = db_local['Profile']
    return collection_profile


def get_csis3300_db():
    try:
        client_csis3300 = pymongo.MongoClient('ds023098.mlab.com', 23098)
        db_csis3300 = client_csis3300['csis3300']
        db_csis3300.authenticate('csis3300', 'dkt75gT', mechanism='SCRAM-SHA-1')
        return db_csis3300
    except Exception as e:
        logging.warning(str(e))


def get_csis3300_users(db):
    collection_users = db['users']
    return collection_users


def find_users(collection):
    result_found = collection.find({"user_num": {"$lte": 10}})
    for document in result_found:
        print(document['first_name'])


def get_root():
    html_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'stats.htm')
    response = request.urlopen("file://" + html_file)
    html_text = response.read().decode('utf-8')
    root = html.fromstring(html_text)
    return root


def get_stats(root):
    stats = root.xpath("//table[contains(@class, 'sortable')]/tbody//tr")
    return stats


def retrieve_and_insert_stats(stats):
    for record in stats:
        team_name = record[0].find('a').attrib['title']
        player_nickname = record[1].find('a').attrib['title']
        games = record[2].find('b').text
        wins = record[3].text.strip()
        losses = record[4].text.strip()
        kills = record[6].text.strip()
        deaths = record[7].text.strip()
        assists = record[8].text.strip()
        cs = record[10].text.strip()  # creeps per game
        cspm = record[11].text.strip()  # creeps per minute
        gold = record[12].text.strip()
        gpm = record[13].text.strip()  # gold per minute
        kpar = record[14].text.strip()  # kill participation
        ks = record[15].text.strip()  # kill share
        gs = record[16].text.strip()  # gold share
        cp = record[17].find('b/span/a').text  # champions played
        champs = record[18]  # champions most played
        champ_names = []
        for tag in champs:
            champ_names.append(tag.attrib['title'])

if __name__ == '__main__':
    find_users(get_csis3300_users(get_csis3300_db()))
