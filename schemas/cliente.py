from pydantic import BaseModel 
 
from model import Cliente 
 
class ClientePostSchema(BaseModel): 
    """ Define como um novo cliente a ser inserido deve ser representado. 
    """ 
    nome: str 
    # cpf: int 
    # cep_endereco: int 
    # numero_endereco: str 
    # complemento_endereco: str 
 
class ClienteViewSchema(BaseModel): 
    """ Define como deve ser a estrutura do cliente retornado após uma requisição 
    """ 
    nome: str 
    # id: int 
    # data_inicio: datetime 
    # data_termino: datetime 
    # valor: float 
    # veiculo: str 
    # modelo_eiculo: str 
 
# Defs 
 
def show_cliente(cliente: Cliente): 
    """ Retorna uma representação do aluguel seguindo o schema definido em 
        AluguelViewSchema. 
    """ 
 
    return { 
        'nada': 'nada' 
        # 'id': aluguel.id, 
        # 'data_inicio': aluguel.data_inicio, 
        # 'data_termino': aluguel.data_termino, 
        # 'valor': aluguel.valor, 
        # 'veiculo' : {  
        #     'id': aluguel.veiculo.id_veiculo, 
        #     'modelo' : aluguel.veiculo.modelo, 
        #     'valor_diaria': aluguel.veiculo.valor_diaria 
        # } 
    }