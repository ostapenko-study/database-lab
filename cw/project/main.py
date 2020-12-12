from db import session
from db import create_database
from models.entities.tournament import Tournament
from models.entities.team import Team
from models.entities.match_results import MatchResults
from models.entities.match_schedule import MatchSchedule
from models.entities.playground import Playground
import psycopg2
from config import Config
from controllers.generate import GenerateController
from models.storages.generate import GenerateStorage
from controllers.search import SearchController
from models.storages.search import SearchStorage

if __name__ == '__main__':
    conn = psycopg2.connect(dbname=Config.db_name, user=Config.user,
                            password=Config.passwd, host='localhost')

    cursor = conn.cursor()
    storage = SearchStorage(cursor)
    controller = SearchController(storage)

    controller.loop()

    cursor.close()
    conn.commit()
    conn.close()
