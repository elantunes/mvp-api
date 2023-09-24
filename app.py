from datetime import datetime
from flask import redirect, request
from flask_cors import CORS
from flask_openapi3 import OpenAPI, Info, Tag
from logger import logger
from sqlalchemy import select, update

from model import Session, Aluguel, Cliente, Veiculo
from schemas import *

info = Info(title="API do Moove-se", version="1.0.0")
app = OpenAPI(__name__, info=info)

CORS(app)

# definindo tags
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
alugueis_tag = Tag(name="Aluguel", description="Adição, visualização e remoção de aluguéis à base")
clientes_tag = Tag(name="Cliente", description="Adição, visualização e remoção de clientes à base")
veiculos_tag = Tag(name="Veiculo", description="Visualização de veículos à base")


# GET

@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')


@app.get('/alugueis', tags=[alugueis_tag],
         responses={"200": ListaAlugueisSchema, "404": ErrorSchema})
def get_alugueis():
    """Faz a busca por todos os aluguéis cadastrados
       Retorna uma representação da listagem de aluguéis.
    """
    logger.debug("Coletando aluguéis")

    session = Session()

    stmt = select(Aluguel, Veiculo).join(Veiculo)

    print(stmt)

    alugueis_e_veiculos = session.execute(stmt).fetchall()

    alugueis = []

    for row in alugueis_e_veiculos:
        aluguel = row[0]
        veiculo = row[1]
        aluguel.veiculo = veiculo
        alugueis.append(aluguel)

    if not alugueis:
        return {"alugueis": []}, 200
    else:
        logger.debug(f"%d aluguéis encontrados" % len(alugueis))
        print(alugueis)
        return show_alugueis(alugueis), 200


@app.get('/aluguel/<int:id>',
         tags=[alugueis_tag],
         responses={"202": AluguelViewSchema, "404": ErrorSchema})
def get_aluguel(path: AluguelGetSchema):
    """Faz a busca pelo aluguel com o ID informado
       Retorna uma representação da um aluguel.
    """

    try:
        logger.debug(f"Buscando o aluguel #{path.id}")

        stmt = select(Aluguel, Veiculo). \
               where(Aluguel.id == path.id).join(Veiculo)
        print(stmt)        

        session = Session()
        alugueis_e_veiculos = session.execute(stmt).fetchall()
        alugueis = []

        for row in alugueis_e_veiculos:
            aluguel = row[0]
            veiculo = row[1]
            aluguel.veiculo = veiculo
            alugueis.append(aluguel)

        if aluguel:
            logger.debug(f"Aluguel #{aluguel.id} encontrado")
            print(aluguel)
            return show_aluguel(aluguel), 200
        else:
            error_msg = "Aluguel não encontrado na base"
            logger.warning(f"Erro ao buscar o aluguel #'{path.id}', {error_msg}")
            return {"message": error_msg}, 404

    except Exception as e:
        logger.warning(f"Erro ao obter o aluguel #'{path.id}', {e.__traceback__}")
        return {"message": e.__traceback__}, 400


@app.get('/veiculos', tags=[veiculos_tag],
         responses={"200": ListaVeiculosSchema, "404": ErrorSchema})
def get_veiculos():
    """Faz a busca por todos os veículos cadastrados
       Retorna uma representação da listagem de veículos.
    """
    logger.debug("Coletando veículos")

    session = Session()

    veiculos = session.query(Veiculo).order_by(Veiculo.modelo).all()

    if not veiculos:
        return {"veiculos": []}, 200
    else:
        logger.debug(f"%d veículos encontrados" % len(veiculos))
        print(veiculos)
        return show_veiculos(veiculos), 200


# POST

@app.post('/aluguel',
          tags=[alugueis_tag],
          responses={"200": AluguelViewSchema, "404": ErrorSchema})
def add_aluguel(form: AluguelPostSchema):
    
    try:

        id_veiculo = form.id_veiculo
        data_inicio = form.data_inicio
        data_termino = form.data_termino

        session = Session()
        veiculo = session.get(Veiculo, id_veiculo)

        aluguel = Aluguel(
            id = None,
            id_veiculo = form.id_veiculo,
            data_inicio = data_inicio,
            data_termino = data_termino,
            valor = veiculo.valor_diaria * ((data_termino - data_inicio).days + 1),
            veiculo = None
        )

        logger.debug("Incluindo um aluguel")
        
        session.add(aluguel)
        session.commit()

        veiculo = session.get(Veiculo, aluguel.id_veiculo)

        aluguel.veiculo = veiculo

        logger.debug("Aluguel incluído com sucesso!")
        
        return show_aluguel(aluguel), 200

    except Exception as e:
        logger.warning(f"Erro ao adicionar um aluguel, {e}")
        return {"message": e.__traceback__}, 400


@app.post('/cliente',
          tags=[clientes_tag],
          responses={"200": ClienteViewSchema, "404": ErrorSchema})
def add_cliente(form: ClientePostSchema):
    
    try:

        logger.debug("Incluindo um cliente")

        cliente = Cliente(
            nome = form.nome,
            cpf = form.cpf,
            cep_endereco = form.cep_endereco,
            numero_endereco = form.numero_endereco,
            complemento_endereco = form.complemento_endereco
        )

        logger.debug("Incluindo um aluguel")
        
        session = Session()
        session.add(cliente)
        session.commit()

        logger.debug("Cliente incluído com sucesso!")
        
        return show_cliente(cliente), 200

    except Exception as e:
        logger.error(f"Erro ao adicionar um cliente, {e}")
        return {"message": e.__traceback__}, 400

# PUT

@app.put('/aluguel/<int:id>',
         tags=[alugueis_tag],
         responses={"200": AluguelViewSchema, "404": ErrorSchema})
def put_aluguel(path: AluguelPutSchema, form: AluguelPostSchema):

    id_veiculo = form.id_veiculo
    data_inicio = form.data_inicio
    data_termino = form.data_termino

    session = Session()
    veiculo = session.get(Veiculo, id_veiculo)

    aluguel = Aluguel(
        id = path.id,
        id_veiculo = form.id_veiculo,
        data_inicio = data_inicio,
        data_termino = data_termino,
        valor = veiculo.valor_diaria * ((data_termino - data_inicio).days + 1),
        veiculo= None
    )

    try:
        logger.debug("Alterando um aluguel")
        
        session = Session()
       
        stmt = update(Aluguel) \
            .where(Aluguel.id == aluguel.id) \
            .values( \
                id_veiculo = aluguel.id_veiculo, \
                data_inicio = aluguel.data_inicio, \
                data_termino = aluguel.data_termino, \
                valor = aluguel.valor)

        print(stmt)
        session.execute(stmt)

        session.commit()

        veiculo = session.get(Veiculo, aluguel.id_veiculo)

        aluguel.veiculo = veiculo

        logger.debug("Aluguel alterado com sucesso!")
        
        return show_aluguel(aluguel), 200

    except Exception as e:
        error_msg = "Não foi possível alterar o aluguel"
        logger.warning(f"Erro ao alterar o aluguel #'{path.id}', {error_msg}")
        return {"message": e.__traceback__}, 400


# DELETE

@app.delete('/aluguel/<int:id>',
            tags=[alugueis_tag],
            responses={"202": AluguelDeleteViewSchema, "404": ErrorSchema})
def del_aluguel(path: AluguelDeleteSchema):
    """Exclui um aluguel à Base de Dados
       Retorna uma mensagem de confirmação de remoção.
    """

    logger.debug("Excluindo um aluguel")

    session = Session()
    count = session.query(Aluguel).filter(Aluguel.id == path.id).delete()
    session.commit()

    if count:
        return {"message": "Aluguel removido", "id": path.id}
    else:
        error_msg = "Aluguel não encontrado na base"
        logger.warning(f"Erro ao deletar aluguel #'{path.id}', {error_msg}")
        return {"message": error_msg}, 404

app.run(debug=True)