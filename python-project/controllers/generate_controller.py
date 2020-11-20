import view as View
from controllers.abstract_controller import AController
from database import Database


class GenerateController(AController):

    def __init__(self, database: Database):
        super().__init__('generate', 'go to main')
        self.commands = [
            'generate_tournaments'
        ] + self.commands
        self.methods = [
            self.__generate_tournament
        ]
        self.db = database

    def execute_method(self, command_id: int):
        self.methods[command_id]()

    def __generate_tournament(self):
        print('Enter count of teams:')
        count_teams = View.enter_integer()
        print('Enter count of games:')
        count_games = View.enter_integer()
        arrays = self.db.generate_tournament(count_teams, count_games)
        print('IDs of teams:')
        print(arrays[0])
        print('IDs of games:')
        print(arrays[1])
