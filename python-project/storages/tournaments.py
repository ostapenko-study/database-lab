# models/storages/tournaments.py

from models.tournament import Tournament
from storages.abstract_storage import AStorage


class TournamentStorage(AStorage):

    def insert(self, entity: Tournament):
        self.cursor.execute("""
                               INSERT INTO public.tournaments (name, date)
                               VALUES (%s, %s)
                               RETURNING id;
                               """, (entity.name, entity.date))
        return self.cursor.fetchall()[0]

    def update(self, entity: Tournament):
        self.cursor.execute("""
                               UPDATE public.tournaments 
                               SET name = %s, date = %s
                               WHERE id = %s;
                               """, (entity.name, entity.date, entity.id))
        return self.cursor.rowcount

    def generate(self, count: int):
        print('')
