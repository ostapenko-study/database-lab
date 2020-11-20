from models.storages.abstract_storage import AStorage
from models.entities.game import Game
from benchmark import benchmark


class GameStorage(AStorage):

    @benchmark
    def insert(self, entity: Game):
        self.cursor.execute("""
            INSERT INTO public.games (teams_id_1, teams_id_2, scheduled_start)
            VALUES (%s, %s, %s)
            RETURNING id;
            """, (entity.teams_id_1, entity.teams_id_2,
                  entity.scheduled_start))
        return self.cursor.fetchall()[0]

    @benchmark
    def update(self, entity: Game):
        self.cursor.execute("""
            UPDATE public.games 
            SET teams_id_1 = %s, teams_id_2 = %s, scheduled_start = %s
            WHERE id = %s;
            """, (entity.teams_id_1, entity.teams_id_2,
                  entity.scheduled_start, entity.id))
        return self.cursor.rowcount

    def generate_in_tournament(self, tournament_id: int):
        self.cursor.callproc('public.generate_game_for_tournament', (tournament_id, ))
        return self.cursor.fetchall()[0]
