import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

basedir = os.path.abspath(os.path.dirname(__file__))
dbpath = os.path.join(basedir, 'app.db')
engine = create_engine(f'sqlite:///{dbpath}', echo=True)
Base = declarative_base()

Session = sessionmaker()
