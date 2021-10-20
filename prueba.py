import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from dotenv import load_dotenv

# Carga las variables de entorno que tengo en .env
load_dotenv()

engine= create_engine(os.getenv("DATABASE_URL"))
db =scoped_session(sessionmaker(bind=engine))

### Querys de creacion de las tablas
usuarios = db.execute("Select * from usuarios")

### Crea las tablas usando las querys
db.commit()

print(usuarios.key)