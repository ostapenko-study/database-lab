from storages.abstract_storage import AStorage
from models.game import Game


class GameStorage(AStorage):

    def insert(self, entity: Game):
        self.cursor.execute("""
            INSERT INTO public.games (teams_id_1, teams_id_2, playground_id, scheduled_start, tournament_id)
            VALUES (%s, %s, %s, %s, %s)
            RETURNING id;
            """, (entity.teams_id_1, entity.teams_id_2, entity.playground_id,
                  entity.scheduled_start, entity.tournament_id))
        return self.cursor.fetchall()[0]

    def update(self, entity: Game):
        self.cursor.execute("""
            UPDATE public.games 
            SET teams_id_1 = %s, teams_id_2 = %s, playground_id = %s, scheduled_start = %s, tournament_id = %s
            WHERE id = %s;
            """, (entity.teams_id_1, entity.teams_id_2, entity.playground_id,
                  entity.scheduled_start, entity.tournament_id, entity.id))
        return self.cursor.rowcount

    def generate(self, count: int):
        self.cursor.execute("""
            INSERT INTO public.games
            SELECT
            trunc(random() * 10)::int as tournaments_id,
            trunc(random() * 10)::int as teams_id_1,
            trunc(random() * 10)::int as teams_id_2,
            trunc(random() * 10)::int as playground_id,
            (time '06:00:00' + random() * (time '16:00:00')) as scheduled_start
            FROM generate_series(1, %s)
            """, (count,))
        return self.cursor.rowcount
