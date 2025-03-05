from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

from laserfocus.utils.database import DatabaseHandler
from laserfocus.utils.logger import logger

import os

Base = declarative_base()

class ExampleTable(Base):
    """Example table"""
    __tablename__ = 'example_table'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    updated = Column(String)
    created = Column(String)

logger.announcement('Initializing Database Service', 'info')

db_name = 'example_database'
db_path = os.path.join(os.path.dirname(__file__), '..', 'db', f'{db_name}.db')
db_url = f'sqlite:///{db_path}'

engine = create_engine(db_url)

db = DatabaseHandler(base=Base, engine=engine, type='sqlite')

logger.announcement('Successfully initialized Database Service', 'success')