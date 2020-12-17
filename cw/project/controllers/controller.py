from database import Database
from controllers.storage import StorageController
from models.entities.tournament import Tournament
from models.entities.team import Team
from controllers.abstract import AController
from controllers.search import SearchController
from controllers.generate import GenerateController


class Controller(AController):

    def __init__(self, database: Database):
        super().__init__('main', 'exit, have a nice day!')
        self.commands = ['tournament', 'team', 'search', 'generate'] + self.commands
        self.controllers = [
            StorageController(database.tournaments, lambda: Tournament.input_from_console(), 'tournaments'),
            StorageController(database.teams, lambda: Team.input_from_console(), 'teams'),
            SearchController(database.searches),
            GenerateController(database.generate),
        ]

    def execute_method(self, command_id: int):
        self.controllers[command_id].loop()
