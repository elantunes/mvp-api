from pydantic import BaseModel 
 
from model import Cliente 
 
class ClientePostSchema(BaseModel): 
    """ Define como um novo cliente a ser inserido deve ser representado.
    """
    nome: str
    cpf: int
    cep_endereco: int
    numero_endereco: str
    complemento_endereco: str
 
class ClienteViewSchema(BaseModel): 
    """ Define como deve ser a estrutura do cliente retornado após uma requisição
    """
    id: int
    nome: str
    cpf: int
    cep_endereco: int
    numero_endereco: str
    complemento_endereco: str
 
# Defs 
 
def show_cliente(cliente: Cliente): 
    """ Retorna uma representação do cliente seguindo o schema definido em 
        ClinteViewSchema.
    """
 
    return { 
        'id': cliente.id,
        'nome': cliente.nome,
        'cpf': cliente.cpf,
        'cep_endereco': cliente.cep_endereco,
        'numero_endereco': cliente.numero_endereco,
        'complemento_endereco': cliente.complemento_endereco
    }