#tournaments=# \d games
                                        Table "public.games"
     Column      |          Type          | Collation | Nullable |              Default
-----------------+------------------------+-----------+----------+-----------------------------------
 id              | integer                |           | not null | nextval('games_id_seq'::regclass)
 teams_id_1      | integer                |           | not null | 
 teams_id_2      | integer                |           | not null | 
 scheduled_start | time without time zone |           | not null | 
Indexes:
    "games_pkey" PRIMARY KEY, btree (id)
    "fki_teams_id_1_fkey" btree (teams_id_1)
    "fki_teams_id_2_fkey" btree (teams_id_2)
Foreign-key constraints:
    "teams_id_1_fkey" FOREIGN KEY (teams_id_1) REFERENCES teams(id) ON UPDATE CASCADE ON DELETE CASCADE NOT VALID
    "teams_id_2_fkey" FOREIGN KEY (teams_id_2) REFERENCES teams(id) ON UPDATE CASCADE ON DELETE CASCADE NOT VALID

#tournaments=# \d teams
                                          Table "public.teams"
     Column     |            Type             | Collation | Nullable |              Default
----------------+-----------------------------+-----------+----------+-----------------------------------
 id             | integer                     |           | not null | nextval('teams_id_seq'::regclass)
 name           | name                        |           | not null | 
 tournaments_id | integer                     |           | not null | 
 registered_at  | timestamp without time zone |           | not null | 
Indexes:
    "teams_pkey" PRIMARY KEY, btree (id)
    "fki_tournaments_id_fkey" btree (tournaments_id)
Foreign-key constraints:
    "tournaments_id_fkey" FOREIGN KEY (tournaments_id) REFERENCES tournaments(id) ON UPDATE CASCADE ON DELETE CASCADE NOT VALID
Referenced by:
    TABLE "games" CONSTRAINT "teams_id_1_fkey" FOREIGN KEY (teams_id_1) REFERENCES teams(id) ON UPDATE CASCADE ON DELETE CASCADE NOT VALID
    TABLE "games" CONSTRAINT "teams_id_2_fkey" FOREIGN KEY (teams_id_2) REFERENCES teams(id) ON UPDATE CASCADE ON DELETE CASCADE NOT VALID

#tournaments=# \d tournaments
                            Table "public.tournaments"
 Column |  Type   | Collation | Nullable |                 Default
--------+---------+-----------+----------+-----------------------------------------
 id     | integer |           | not null | nextval('tournaments_id_seq'::regclass)
 name   | name    |           | not null | 
 date   | date    |           |          | 
Indexes:
    "tournaments_pkey" PRIMARY KEY, btree (id)
Referenced by:
    TABLE "teams" CONSTRAINT "tournaments_id_fkey" FOREIGN KEY (tournaments_id) REFERENCES tournaments(id) ON UPDATE CASCADE ON DELETE CASCADE NOT VALID

