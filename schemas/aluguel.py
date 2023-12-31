from datetime import datetime
from pydantic import BaseModel
from typing import List

from model import Aluguel


#Classes

class AluguelGetSchema(BaseModel):
    """ Define como uma requisição de aluguel deve ser representada.
    """
    id: int


class AluguelPostFormSchema(BaseModel):
    """ Define como um novo aluguel a ser inserido deve ser representado.
    """
    id_cliente: int
    id_veiculo: int
    data_inicio: datetime
    data_termino: datetime


class AluguelPutFormSchema(BaseModel):
    """ Define como deve-se fornecer os dados pra atualizar um Aluguel.
    """
    id_veiculo: int
    data_inicio: datetime
    data_termino: datetime

class AluguelPutPathSchema(BaseModel):
    """ Define como um remoção de aluguel deve ser representada.
    """
    id: int


class AluguelRequestSchema(BaseModel):
    """ Define como um remoção de aluguel deve ser representada.
    """
    id: int
    id_veiculo: int


class AluguelDeleteSchema(BaseModel):
    """ Define como um remoção de aluguel deve ser representada.
    """
    id: int


class AluguelViewSchema(BaseModel):
    """ Define como deve ser a estrutura do aluguel retornado após uma requisição
    """
    id: int
    data_inicio: datetime
    data_termino: datetime
    valor: float
    veiculo: str
    modelo_eiculo: str


class AluguelDeleteViewSchema(BaseModel):
    """ Define como deve ser a estrutura do aluguel retornado após uma requisição
        de remoção.
    """
    id: int
    message: str


class ListaAlugueisSchema(BaseModel):
    """ Define como uma listagem de aluguéis será retornada.
    """
    alugueis:List[AluguelViewSchema]


# Defs

def show_aluguel(aluguel: Aluguel):
    """ Retorna uma representação do aluguel seguindo o schema definido em
        AluguelViewSchema.
    """

    return {
        'id': aluguel.id,
        'data_inicio': aluguel.data_inicio,
        'data_termino': aluguel.data_termino,
        'valor': aluguel.valor,
        'cliente' : {
            'id': aluguel.cliente.id,
            'cpf' : aluguel.cliente.cpf,
            'nome' : aluguel.cliente.nome,

        },
        'veiculo' : { 
            'id': aluguel.veiculo.id_veiculo,
            'modelo' : aluguel.veiculo.modelo,
            'valor_diaria': aluguel.veiculo.valor_diaria
        }
    }


def show_alugueis(alugueis: List[Aluguel]):
    """ Retorna uma representação de uma lista de aluguéis seguindo o schema definido em
        ListaAlugueisSchema.
    """
    result = []
    for aluguel in alugueis:
        result.append(show_aluguel(aluguel))

    return {'alugueis': result}
