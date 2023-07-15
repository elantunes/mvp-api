from sqlalchemy import Column, Float, Integer, String, Table

from model import Base

class Veiculo(Base):
    __table__ = Table('veiculo', Base.metadata,
        Column('id_veiculo', Integer, primary_key=True),
        Column('modelo', String(100), nullable=False),
        Column('valor_diaria', Float, nullable=False),
        sqlite_autoincrement=True)

    def __init__(self, id_veiculo:int, modelo:str, valor_diaria:float):
        self.id_veiculo = id_veiculo
        self.modelo = modelo
        self.valor_diaria = valor_diaria