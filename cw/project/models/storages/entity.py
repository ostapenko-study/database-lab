from benchmark import benchmark
from db import session


def get_entity_mapped_keys(item):
    mapped_values = {}
    for entity in item.__dict__.items():
        key = entity[0]
        value = entity[1]
        if key != '_sa_instance_state' and key != 'id':
            mapped_values[key] = value
    return mapped_values


class StorageEntity:

    def __init__(self, instance):
        self.instance = instance

    @benchmark
    def get_by_id(self, id: int):
        return session. \
            query(self.instance). \
            get(id)

    @benchmark
    def get_all(self):
        return session. \
            query(self.instance). \
            all()

    @benchmark
    def delete(self, id: int):
        result = session. \
            query(self.instance). \
            filter(self.instance.id == id). \
            delete()
        session.commit()
        return result

    @benchmark
    def insert(self, entity):
        entity.id = None
        session.add(entity)
        session.commit()
        return entity.id

    @benchmark
    def update(self, entity):
        result = session. \
            query(self.instance). \
            filter(self.instance.id == entity.id). \
            update(get_entity_mapped_keys(entity))
        session.commit()
        return result
