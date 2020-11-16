from abc import ABC, abstractmethod


class AStorage(ABC):

    def __init__(self, cursor, table_name):
        self.cursor = cursor
        self.__table_name = table_name

    def getById(self, id: int):
        self.cursor.execute("""
            SELECT * FROM """ + self.__table_name +"""
            WHERE id = %s;
            """, (id,))
        return self.cursor.fetchone()

    def getAll(self):
        self.cursor.execute("SELECT * FROM " + self.__table_name + ";")
        return self.cursor.fetchall()

    def delete(self, id: int):
        self.cursor.execute("""
            DELETE FROM """ + self.__table_name +"""
            WHERE id = %s;
            """, (id,))
        return self.cursor.rowcount

    @abstractmethod
    def insert(self, entity):
        pass

    @abstractmethod
    def update(self, entity):
        pass
