from models.storages.abstract_storage import AStorage
from models.entities.team import Team
from benchmark import benchmark


class TeamStorage(AStorage):

    @benchmark
    def insert(self, entity: Team):
        self.cursor.execute("""
            INSERT INTO public.teams (name, tournaments_id, registered_at)
            VALUES (%s, %s, %s)
            RETURNING id;
            """, (entity.name, entity.tournaments_id, entity.registered_at))
        return self.cursor.fetchall()[0]

    @benchmark
    def update(self, entity: Team):
        self.cursor.execute("""
            UPDATE public.teams 
            SET name = %s, tournaments_id = %s, registered_at = %s
            WHERE id = %s;
            """, (entity.name, entity.tournaments_id, entity.registered_at, entity.id))
        return self.cursor.rowcount

    def generate_in_tournament(self, tournament_id: int):
        self.cursor.callproc('generate_team_for_tournament', tournament_id, )
        return self.cursor.fetchall()[0]

