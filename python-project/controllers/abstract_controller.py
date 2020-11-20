from abc import ABC, abstractmethod
import view as View


class AController(ABC):

    def __init__(self, title: str, title_go_to_prev_menu: str):
        self.commands = ['exit']
        self.methods = []
        self.title = title
        self.title_go_to_prev_menu = title_go_to_prev_menu

    def loop(self):
        count_commands = len(self.commands) - 1
        while True:
            View.print_help(self.commands, self.title)
            command_id = View.enter_integer(0, count_commands)
            if command_id == count_commands:
                print(self.title_go_to_prev_menu)
                break
            print(f'{self.title} command: {self.commands[command_id]} is selected')
            self.execute_method(command_id)

    @abstractmethod
    def execute_method(self, command_id: int):
        pass
