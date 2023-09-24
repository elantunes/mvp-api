from pydantic import BaseModel
from typing import List
 
from model import Cliente


#Classes

class ClienteBuscaPorCpfHeaderSchema(BaseModel):
    """ Define o header da Busca de Cliente Por CPF.
    """
    cpf: int

class ClienteDeleteSchema(BaseModel):
    """ Define como um remoção de Cliente deve ser representada.
    """
    id: int


class ClienteDeleteViewSchema(BaseModel):
    """ Define como deve ser a estrutura do Cliente retornado após uma requisição
        de remoção.
    """
    id: int
    message: str


class ClienteGetSchema(BaseModel):
    """ Define como uma requisição de Cliente deve ser representada.
    """
    id: int

class ClienteGetPorCpfSchema(BaseModel):
    """ Define como uma requisição de Cliente por CPF deve ser representada.
    """
    cpf: int


class ClientePostSchema(BaseModel): 
    """ Define como um novo Cliente a ser inserido deve ser representado.
    """
    nome: str
    cpf: int
    cep_endereco: int
    logradouro_endereco: str
    numero_endereco: str
    complemento_endereco: str
    localidade_endereco: str
    cidade_endereco: str
    uf_endereco: str
 

class ClientePutSchema(BaseModel):
    """ Define como um remoção de Cliente deve ser representada.
    """
    id: int


class ClienteViewSchema(BaseModel): 
    """ Define como deve ser a estrutura do Cliente retornado após uma requisição
    """
    id: int
    nome: str
    cpf: int
    cep_endereco: int
    logradouro_endereco: int
    numero_endereco: str
    complemento_endereco: str
    localidade_endereco: str
    cidade_endereco: str
    uf_endereco: str
 

class ListaClientesSchema(BaseModel):
    """ Define como uma listagem de Clientes será retornada.
    """
    clientes:List[ClienteViewSchema]


# Defs 
 
def show_cliente(cliente: Cliente): 
    """ Retorna uma representação do Clientes seguindo o schema definido em 
        ClinteViewSchema.
    """
 
    return { 
        'id': cliente.id,
        'nome': cliente.nome,
        'cpf': cliente.cpf,
        'cep_endereco': cliente.cep_endereco,
        'logradouro_endereco': cliente.logradouro_endereco,       
        'numero_endereco': cliente.numero_endereco,
        'complemento_endereco': cliente.complemento_endereco,
        'localidade_endereco': cliente.localidade_endereco,
        'cidade_endereco': cliente.cidade_endereco,
        'uf_endereco': cliente.uf_endereco
    }


def show_clientes(clientes: List[Cliente]):
    """ Retorna uma representação de uma lista de Clientes seguindo o schema definido em
        ListaClintesSchema.
    """
    result = []
    for cliente in clientes:
        result.append(show_cliente(cliente))

    return {'clientes': result}