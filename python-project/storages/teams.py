from storages.abstract_storage import AStorage
from models.team import Team

class TeamStorage(AStorage):

    def insert(self, entity: Team):
        self.cursor.execute("""
            INSERT INTO public.teams (name, tournaments_id, registered_at)
            VALUES (%s, %s, %s)
            RETURNING id;
            """, (entity.name, entity.tournaments_id, entity.registered_at))
        return self.cursor.fetchall()[0]

    def update(self, entity: Team):
        self.cursor.execute("""
            UPDATE public.teams 
            SET name = %s, tournaments_id = %s, registered_at = %s
            WHERE id = %s;
            """, (entity.name, entity.tournaments_id, entity.registered_at, entity.id))
        return self.cursor.rowcount

    def generate(self, count: int):
        self.cursor.execute("""
        INSERT INTO
        public.teams(name, tournaments_id, registered_at)
        SELECT
        chr(trunc(65 + random() * 25)::int) || chr(trunc(65 + random() * 25)::int) || 
        chr(trunc(65 + random() * 25)::int) as name,
        trunc(random() * 10)::int as tournaments_id,
        timestamp '2000-01-01 00:00:00' + random() * (timestamp '2030-12-31 23:59:59' - timestamp '2000-01-01 00:00:00')
        as registered_at
        FROM generate_series(1, '%s')
        """, (count, ))
        return self.cursor.rowcount
