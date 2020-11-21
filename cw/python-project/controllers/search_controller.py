import view as View
from models.searches import SearchesModel
from controllers.abstract_controller import AController


class SearchController(AController):

    def __init__(self, searches: SearchesModel):
        super().__init__('searches', 'go to main')
        self.searches = searches
        self.commands = [
            'tournaments_schedule',
            'tournaments_schedule_in_time_range',
            'tournaments_like'
        ] + self.commands
        self.methods = [
            self.__tournaments_schedule,
            self.__tournaments_schedule_in_time_range,
            self.__tournaments_like
        ]

    def execute_method(self, command_id: int):
        self.methods[command_id]()

    def __tournaments_schedule(self):
        print('Enter tournaments_id:')
        id = View.enter_integer()
        items = self.searches.tournaments_schedule(id)
        View.print_collection_with_verify(items)

    def __tournaments_schedule_in_time_range(self):
        print('Enter tournaments_id:')
        id = View.enter_integer()
        print('Enter time begin:')
        time_begin = View.enter_time()
        print('Enter time end:')
        time_end = View.enter_time()
        items = self.searches.tournaments_schedule_in_time_range(id, time_begin, time_end)
        View.print_collection_with_verify(items)

    def __tournaments_like(self):
        print('Enter pattern:')
        pattern = input()
        items = self.searches.tournaments_like(pattern)
        View.print_collection_with_verify(items)
