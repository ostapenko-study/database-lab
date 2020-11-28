from benchmark import benchmark
from base import session


class Storage:

    def __init__(self, instance):
        self.instance = instance

    @benchmark
    def get_by_id(self, id: int):
        return session.\
            query(self.instance).\
            get(id)

    @benchmark
    def get_all(self):
        return session.\
            query(self.instance).\
            all()

    @benchmark
    def delete(self, id: int):
        result =  session.\
            query(self.instance).\
            filter(self.instance.id == id).\
            delete()
        session.commit()
        return result

    @benchmark
    def insert(self, entity):
        session.add(entity)
        session.commit()
        return entity.id

    @benchmark
    def update(self, entity):
        result = session.\
            query(self.instance).\
            filter(self.instance.id == entity.id).\
            update(entity)
        session.commit()
        return result
