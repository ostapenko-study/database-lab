# models/storages/participants.py

from models.participant import Participant
from storages.abstract_storage import AStorage


class ParticipantStorage(AStorage):

    def insert(self, entity: Participant):
        self.cursor.execute("""
            INSERT INTO public.participants (name, surname, birthday)
            VALUES (%s, %s, %s)
            RETURNING id;
            """, (entity.name, entity.surname, entity.birthday))
        return self.cursor.fetchall()[0]

    def update(self, entity: Participant):
        self.cursor.execute("""
            UPDATE public.participants 
            SET name = %s, surname = %s, birthday = %s
            WHERE id = %s;
            """, (entity.name, entity.surname, entity.birthday, entity.id))
        return self.cursor.rowcount

    def generate(self, count: int):
        print('')
