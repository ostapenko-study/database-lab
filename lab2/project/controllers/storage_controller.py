from models.storages.abstract_storage import AStorage
from controllers.abstract_controller import AController
import view as View


class StorageController(AController):

    def __init__(self, storage: AStorage, func_input_entity, entity_name: str):
        super().__init__(entity_name, 'go to main')
        self.storage = storage
        self.func_input_entity = func_input_entity
        self.commands = [
            'get_all',
            'get_by_id',
            'insert',
            'update',
            'delete'
        ] + self.commands
        self.methods = [
            self.__get_all,
            self.__get_by_id,
            self.__insert,
            self.__update,
            self.__delete
        ]

    # def loop(self): from AController
    def execute_method(self, command_id: int):
        self.methods[command_id]()

    def __get_all(self):
        items = self.storage.get_all()
        View.print_collection_with_verify(items)

    def __get_by_id(self):
        id = View.enter_integer()
        item = self.storage.get_by_id(id)
        if item is not None:
            print(item)
        else:
            print('no find')

    def __insert(self):
        entity = self.func_input_entity()
        status = self.storage.insert(entity)
        print('status of insert - {}'.format(status))

    def __update(self):
        entity = self.func_input_entity()
        counts = self.storage.update(entity)
        print('updated {} record(s)'.format(counts))

    def __delete(self):
        id = View.enter_integer()
        counts = self.storage.delete(id)
        print('deleted {} record(s)'.format(counts, ))
