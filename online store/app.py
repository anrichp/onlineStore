from base import Session, engine, Base
from users import *
from shopping import *

Base.metadata.create_all(engine, checkfirst=True)

