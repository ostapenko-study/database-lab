import view as View
from controllers.abstract import AController
from models.storages.generate import GenerateStorage


class GenerateController(AController):

    def __init__(self, generate_storage: GenerateStorage):
        super().__init__('generate', 'go to main')
        self.commands = [
            'generate_tournaments'
        ] + self.commands
        self.methods = [
            self.__generate_tournament
        ]
        self.generate_storage = generate_storage

    def execute_method(self, command_id: int):
        self.methods[command_id]()

    def __generate_tournament(self):
        print('Enter count of teams:')
        count_teams = View.enter_integer()
        print('Enter count of playgrounds:')
        count_playgrounds = View.enter_integer()
        print('Enter count of games:')
        count_games = View.enter_integer()
        print('Enter count of played games:')
        count_results = View.enter_integer()
        arrays = self.generate_storage.generate_tournament(count_teams, count_playgrounds, count_games, count_results)
        print("print ID?")
        if View.choose_yes():
            print(f'tournaments ID: {arrays[0]}')
            print('IDs of teams:')
            print(arrays[1])
            print('IDs of playgrounds:')
            print(arrays[2])
            print('IDs of games:')
            print(arrays[3])
        else:
            print('good choice')

        print('commit (\'yes\') or rollback:')
        if View.choose_yes():
            self.generate_storage.commit()
        else:
            self.generate_storage.rollback()
