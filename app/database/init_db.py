from app.database.connection import Base
from app.database.connection import engine

from app.models.doctor import Doctor
from app.models.paciente import Paciente
from app.models.cita import Cita


def init_db():
    Base.metadata.create_all(bind=engine)
    print("DB initialized")