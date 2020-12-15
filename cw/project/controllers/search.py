import view as View
from controllers.abstract import AController
from models.storages.search import SearchStorage
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np


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
        if View.choose_output():
            index_of_name = colnames.index('name')
            count_of_info_field = colnames.index('teams_count')
            colnames = colnames[count_of_info_field:]
            field = View.choose_command(colnames)
            sizes = [row[field + count_of_info_field] for row in items]
            labels = [row[index_of_name] for row in items]
            index_empty_fields = []
            for i in range(0, len(sizes)):
                if sizes[i] is None:
                    index_empty_fields.append(i)

            count = 0
            for i in index_empty_fields:
                sizes.pop(i - count)
                labels.pop(i - count)
                count += 1

            explode = [0.1 for row in labels]

            fig, ax = plt.subplots()
            fig.set_size_inches(18.5, 10.5, forward=True)
            ax.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                    shadow=True, startangle=90)
            ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

            temp_str = f'statistic_tournaments_{colnames[field]}_{datetime.now().strftime("%Y-%m-%d_%H:%M:%S")}'
            plt.title(temp_str)
            plt.savefig(temp_str)
            print(f'file \'{temp_str}\' created')
        else:
            print(colnames)
            View.print_collection_with_verify(items)

    def __get_statistic_teams_in_tournament(self):
        print('Enter tournaments id:')
        tournaments_id = View.enter_integer()
        items, colnames = self.search_storage.get_statistic_teams_in_tournament(tournaments_id)
        if View.choose_output():
            index_of_name = colnames.index('name')
            labels = [row[index_of_name] for row in items]
            for i in range(0, len(labels)):
                if len(labels[i]) > 3:
                    labels[i] = labels[i][:3] + '..'
            commands = ['matches info', 'results info']
            commands_id = View.choose_command(commands)
            if commands_id == 0:
                played_matches = [row[colnames.index('played_match')] for row in items]
                matches_count = [row[colnames.index('match_count')] for row in items]
                for i in range(0, len(matches_count)):  # len(matches_count) == len(played_matches)
                    if played_matches[i] is None:
                        played_matches[i] = 0
                    if matches_count[i] is None:
                        matches_count[i] = 0
                fig, ax = plt.subplots()
                fig.set_size_inches(18.5, 10.5, forward=True)
                ax.bar(labels, matches_count)
                ax.bar(labels, played_matches)
                ax.set_facecolor('seashell')
                fig.set_facecolor('floralwhite')

                plt.xlabel('orange - played_matches; blue - unplayed_matches;')
                temp_str = f'statistic_teams_in_tournament_{tournaments_id}_{commands[commands_id]}_{datetime.now().strftime("%Y-%m-%d_%H:%M:%S")}'
                plt.title(temp_str)
                plt.savefig(temp_str)
            if commands_id == 1:
                wins = [row[colnames.index('win_count')] for row in items]
                self.____null_to_0(wins)
                draws = [row[colnames.index('draw_count')] for row in items]
                self.____null_to_0(draws)
                loses = [row[colnames.index('lose_count')] for row in items]
                self.____null_to_0(loses)

                fig, ax = plt.subplots()

                ax.bar(labels, wins, width=0.4)
                ax.bar(labels, draws, width=0.4, bottom=wins)
                ax.bar(labels, loses, width=0.4, bottom=np.add(wins, draws))

                plt.xlabel('green - lose; orange - draw; blue - win;')
                temp_str = f'statistic_teams_in_tournament_{tournaments_id}_{commands[commands_id]}_{datetime.now().strftime("%Y-%m-%d_%H:%M:%S")}'
                plt.title(temp_str)
                plt.savefig(temp_str)

                print(f'file \'{temp_str}\' created')
        else:
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
        items, colnames = self.search_storage.tournaments_schedule_in_time_range(id, time_begin, time_end)
        print(colnames)
        View.print_collection_with_verify(items)

    def ____null_to_0(self, array):
        for i in range(0, len(array)):
            if array[i] is None:
                array[i] = 0
