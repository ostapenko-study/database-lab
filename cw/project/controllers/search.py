import view as View
from controllers.abstract import AController
from models.storages.search import SearchStorage


class SearchController(AController):

    def __init__(self, search_storage: SearchStorage):
        super().__init__('search', 'go to main')
        self.commands = [
            'get_statistic_tournaments',
            'get_statistic_teams_in_tournament',
            'tournaments_schedule',
            'tournaments_schedule_in_time_range'
        ] + self.commands
        self.methods = [
            self.__get_statistic_tournaments,
            self.__get_statistic_teams_in_tournament,
            self.__tournaments_schedule,
            self.__tournaments_schedule_in_time_range,
        ]
        self.search_storage = search_storage

    def execute_method(self, command_id: int):
        self.methods[command_id]()

    def __get_statistic_tournaments(self):
        items, colnames = self.search_storage.get_statistic_tournaments()
        print(colnames)
        View.print_collection_with_verify(items)

    def __get_statistic_teams_in_tournament(self):
        print('Enter tournaments id:')
        tournaments_id = View.enter_integer()
        items, colnames = self.search_storage.get_statistic_teams_in_tournament(tournaments_id)
        print(colnames)
        View.print_collection_with_verify(items)

    def __tournaments_schedule(self):
        print('Enter tournaments id:')
        tournaments_id = View.enter_integer()
        items, colnames = self.search_storage.tournaments_schedule(tournaments_id)
        print(colnames)
        View.print_collection_with_verify(items)

    def __tournaments_schedule_in_time_range(self):
        print('Enter tournaments_id:')
        id = View.enter_integer()
        print('Enter time begin:')
        time_begin = View.enter_time()
        print('Enter time end:')
        time_end = View.enter_time()
        items,colnames = self.search_storage.tournaments_schedule_in_time_range(id, time_begin, time_end)
        print(colnames)
        View.print_collection_with_verify(items)
