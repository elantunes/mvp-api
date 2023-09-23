from sqlalchemy import Column, Date, DateTime, Float, ForeignKey, Integer, String, Table
from sqlalchemy.sql import func

from model import Base


class Cliente(Base):
    __table__ = Table('cliente', Base.metadata,
        Column('id', Integer, primary_key=True),
        Column('nome', String, nullable=False),
        Column('cpf', Integer, nullable=False),
        Column('cep_endereco', Integer, nullable=False),
        Column('numero_endereco', String, nullable=False),
        Column('complemento_endereco', String, nullable=False),
        Column('data_inclusao', DateTime, server_default=func.now()),
        sqlite_autoincrement=True)

    #def __init__(self, id: int, id_veiculo:int, data_inicio:date, data_termino:date, veiculo:Veiculo, valor:float):
    #     """
    #     Instancia um Aluguel

    #     Arguments:
    #         id: ID do Aluguel
    #         id_veiculo: ID do Veículo
    #         data_inicio: data de início do aluguel
    #         data_termino: data do término do alguel
    #         veiculo: veículo alugado
    #         valor: valor do aluguel
    #     """
    #     self.id = id
    #     self.id_veiculo = id_veiculo
    #     self.data_inicio = data_inicio
    #     self.data_termino = data_termino
    #     self.veiculo = veiculo
    #     self.valor = valor
