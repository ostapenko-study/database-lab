# models/storages/tournaments.py

from models.entities.tournament import Tournament
from models.storages.abstract_storage import AStorage
from benchmark import benchmark


class TournamentStorage(AStorage):

    @benchmark
    def insert(self, entity: Tournament):
        self.cursor.execute("""
                               INSERT INTO public.tournaments (name, date)
                               VALUES (%s, %s)
                               RETURNING id;
                               """, (entity.name, entity.date))
        return self.cursor.fetchall()[0]

    @benchmark
    def update(self, entity: Tournament):
        self.cursor.execute("""
                               UPDATE public.tournaments 
                               SET name = %s, date = %s
                               WHERE id = %s;
                               """, (entity.name, entity.date, entity.id))
        return self.cursor.rowcount

    def generate(self):
        self.cursor.callproc('generate_tournament')
        return self.cursor.fetchall()[0]
