from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://postgres:Z3ff3r@$zaq@localhost:5432/onlinestore', echo=True)

Base = declarative_base()

Session = sessionmaker(bind=engine)