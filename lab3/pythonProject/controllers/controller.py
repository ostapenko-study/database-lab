import view as View
from database import Database
from controllers.storage_controller import StorageController
from models.entities.tournament import Tournament
from models.entities.team import Team
from models.entities.game import Game
from controllers.abstract_controller import AController
from controllers.search_controller import SearchController
from controllers.generate_controller import GenerateController


class Controller(AController):

    def __init__(self, database: Database):
        super().__init__('main', 'exit, have a nice day!')
        self.commands = ['tournament', 'team', 'game', 'searches', 'generate'] + self.commands
        self.controllers = [
            StorageController(database.tournaments, lambda: Tournament.input_from_console(), 'tournaments'),
            StorageController(database.teams, lambda: Team.input_from_console(), 'teams'),
            StorageController(database.games, lambda: Game.input_from_console(), 'games'),
            SearchController(database.searches),
            GenerateController(database)
        ]

    def execute_method(self, command_id: int):
        self.controllers[command_id].loop()
