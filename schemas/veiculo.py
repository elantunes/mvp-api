from pydantic import BaseModel
from typing import List

from model import Veiculo

#Classes

class VeiculoViewSchema(BaseModel):
    """ Define como deve ser a estrutura do veículo retornado após uma requisição
    """
    id_veiculo: int
    modelo: str
    valor_diaria: float


class ListaVeiculosSchema(BaseModel):
    """ Define como uma listagem de veículos será retornada.
    """
    veiculos:List[VeiculoViewSchema]


# Defs

def show_veiculo(veiculo: Veiculo):
    """ Retorna uma representação do veículo seguindo o schema definido em
        VeiculoViewSchema.
    """
    return {
        'id_veiculo': veiculo.id_veiculo,
        'modelo': veiculo.modelo,
        'valor_diaria': veiculo.valor_diaria
    }

def show_veiculos(veiculos: List[Veiculo]):
    """ Retorna uma representação de uma lista de veículos seguindo o schema definido em
        ListaVeiculosViewSchema.
    """
    result = []
    for veiculo in veiculos:
        result.append(show_veiculo(veiculo))

    return {"veiculos": result}