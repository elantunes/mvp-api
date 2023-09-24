from datetime import date
from sqlalchemy import Column, Date, DateTime, Float, ForeignKey, Integer, Table
from sqlalchemy.sql import func

from model.veiculo import Veiculo
from model import Base


class Aluguel(Base):
    __table__ = Table('aluguel', Base.metadata,
        Column('id', Integer, primary_key=True),
        Column('id_veiculo', Integer, ForeignKey('veiculo.id_veiculo'), nullable=False),
        Column('data_inicio', Date, nullable=False),
        Column('data_termino', Date, nullable=False),
        Column('valor', Float, nullable=False),
        Column('data_inclusao', DateTime, server_default=func.now()),
        sqlite_autoincrement=True)

    def __init__(self, id: int, id_veiculo: int, data_inicio: date, data_termino: date, veiculo: Veiculo, valor: float):
        """
        Instancia um Aluguel

        Arguments:
            id: ID do Aluguel
            id_veiculo: ID do Veículo
            data_inicio: data de início do aluguel
            data_termino: data do término do alguel
            veiculo: veículo alugado
            valor: valor do aluguel
        """
        self.id = id
        self.id_veiculo = id_veiculo
        self.data_inicio = data_inicio
        self.data_termino = data_termino
        self.veiculo = veiculo
        self.valor = valor
