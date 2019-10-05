from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DaoGeneral:
    engine = create_engine('sqlite:///ficus.db', echo=True)
    sessionConfig = sessionmaker(bind=engine)
    session = None
    connector = None

# Base.metadata.create_all(DaoGeneral.engine)
