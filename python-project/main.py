import psycopg2
conn = psycopg2.connect(dbname='tournaments', user='postgres',
                        password='1', host='localhost')
cursor = conn.cursor()
