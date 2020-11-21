from abc import ABC, abstractmethod
from benchmark import benchmark


class AStorage(ABC):

    def __init__(self, cursor, table_name):
        self.cursor = cursor
        self.__table_name = table_name

    @benchmark
    def get_by_id(self, id: int):
        self.cursor.execute("""
            SELECT * FROM """ + self.__table_name + """
            WHERE id = %s;
            """, (id,))
        return self.cursor.fetchone()

    @benchmark
    def get_all(self):
        self.cursor.execute("SELECT * FROM " + self.__table_name + ";")
        return self.cursor.fetchall()

    @benchmark
    def delete(self, id: int):
        self.cursor.execute("""
            DELETE FROM """ + self.__table_name + """
            WHERE id = %s;
            """, (id,))
        return self.cursor.rowcount

    @benchmark
    @abstractmethod
    def insert(self, entity):
        pass

    @benchmark
    @abstractmethod
    def update(self, entity):
        pass
