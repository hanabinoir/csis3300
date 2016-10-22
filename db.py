import pymysql


class DB(object):
    def __init__(self):
        pass

    def getCursor(self):
        db_config = {
            'host': 'localhost',
            'port': 3306,
            'user': 'root',
            'passwd': '',
            'db': 'csis3300'
        }

        conn = pymysql.connect(
            host=db_config['host'],
            port=3306,
            user=db_config['user'],
            passwd=db_config['passwd'],
            db=db_config['db'],
            charset='utf8',
            autocommit=True
        )

        cursor = conn.cursor()
        return cursor
