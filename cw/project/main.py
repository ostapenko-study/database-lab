from database import Database
from controllers.controller import Controller

database = Database()

controller = Controller(database)

controller.loop()

# for i in range(1, 5):
#     database.generate.generate_tournament(i*1000, i*100, i*2000, i*1000)