from sqlalchemy import Column, DateTime, Integer, String, Table
from sqlalchemy.sql import func

from model import Base


class Cliente(Base):
    __table__ = Table('cliente', Base.metadata,
        Column('id', Integer, primary_key=True),
        Column('nome', String, nullable=False),
        Column('cpf', Integer, nullable=False),
        Column('logradouro_endereco', String, nullable=False),
        Column('numero_endereco', String, nullable=False),
        Column('complemento_endereco', String, nullable=False),
        Column('cep_endereco', Integer, nullable=False),
        Column('localidade_endereco', String, nullable=False),
        Column('cidade_endereco', String, nullable=False),
        Column('uf_endereco', String, nullable=False),
        Column('data_inclusao', DateTime, server_default=func.now()),
        sqlite_autoincrement=True)

    def __init__(
            self, id: int,
            nome: str,
            cpf: int,
            cep_endereco: int,
            logradouro_endereco: str,
            numero_endereco: str,
            complemento_endereco: str,
            localidade_endereco: str,
            cidade_endereco: str,
            uf_endereco: str):
        """
        Instancia um Cliente

        Arguments:
            id: ID do Cliente
            nome: Nome do Cliente
            cpf: CPF do Cliente
            cep_endereco: CEP do endereço do Cliente
            logradouro_endereco: Logradouro do endereço do Cliente
            numero_endereco: Número do endereço do Cliente
            complemento_endereco: Complemento do endereço do Cliente
            localidade_endereco: Localidade do endereço do Cliente
            cidade_endereco: Cidade do endereço do Cliente
            uf_endereco: Unidade Federativa do endereço do Cliente
            data_inclusao: Data de Inclusão do Cliente no sistema
        """
        self.id = id
        self.nome = nome
        self.cpf = cpf
        self.cep_endereco = cep_endereco
        self.logradouro_endereco = logradouro_endereco
        self.numero_endereco = numero_endereco
        self.complemento_endereco = complemento_endereco
        self.localidade_endereco = localidade_endereco
        self.cidade_endereco = cidade_endereco
        self.uf_endereco = uf_endereco
