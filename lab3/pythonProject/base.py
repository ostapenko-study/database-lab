from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import info

engine = create_engine(f'postgresql://{info.user}:{info.passwd}@{info.url}/{info.db_name}')
Session = sessionmaker(bind=engine)
Base = declarative_base()

session = Session()