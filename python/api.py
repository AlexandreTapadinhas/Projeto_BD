##
## =============================================
## ============== Bases de Dados ===============
## ============== LEI  2020/2021 ===============
## =============================================
## =================== Demo ====================
## =============================================
## =============================================
## === Department of Informatics Engineering ===
## =========== University of Coimbra ===========
## =============================================
##
## Authors: 
##   ines , pedro e rui
##   BD 2021
##   University of Coimbra

 
from flask import Flask, jsonify, request
from datetime import datetime
import logging, psycopg2, time
import random

app = Flask(__name__) 


@app.route('/') 
def hello(): 
    return """
    Hello World!  <br/>
    <br/>
    Check the sources for instructions on how to use the endpoints!<br/>
    <br/>
    BD 2021 Team<br/>
    <br/>
    """

'''


##
##      Demo GET
##
## Obtain all departments, in JSON format
##
## To use it, access: 
## 
##   http://localhost:8080/departments/
##

@app.route("/departments/", methods=['GET'], strict_slashes=True)
def get_all_departments():
    logger.info("###              DEMO: GET /departments              ###");   

    conn = db_connection()
    cur = conn.cursor()

    cur.execute("SELECT ndep, nome, local FROM dep")
    rows = cur.fetchall()

    payload = []
    logger.debug("---- departments  ----")
    for row in rows:
        logger.debug(row)
        content = {'ndep': int(row[0]), 'nome': row[1], 'localidade': row[2]}
        payload.append(content) # appending to the payload to be returned

    conn.close()
    return jsonify(payload)



##
##      Demo GET
##
## Obtain department with ndep <ndep>
##
## To use it, access: 
## 
##   http://localhost:8080/departments/10
##

@app.route("/departments/<ndep>", methods=['GET'])
def get_department(ndep):
    logger.info("###              DEMO: GET /departments/<ndep>              ###");   

    logger.debug(f'ndep: {ndep}')

    conn = db_connection()
    cur = conn.cursor()

    cur.execute("SELECT ndep, nome, local FROM dep where ndep = %s", (ndep,) )
    rows = cur.fetchall()

    row = rows[0]

    logger.debug("---- selected department  ----")
    logger.debug(row)
    content = {'ndep': int(row[0]), 'nome': row[1], 'localidade': row[2]}

    conn.close ()
    return jsonify(content)



##
##      Demo POST
##
## Add a new department in a JSON payload
##
## To use it, you need to use postman or curl: 
##
##   curl -X POST http://localhost:8080/departments/ -H "Content-Type: application/json" -d '{"localidade": "Polo II", "ndep": 69, "nome": "Seguranca"}'
##


@app.route("/departments/", methods=['POST'])
def add_departments():
    logger.info("###              DEMO: POST /departments              ###");   
    payload = request.get_json()

    conn = db_connection()
    cur = conn.cursor()

    logger.info("---- new department  ----")
    logger.debug(f'payload: {payload}')

    # parameterized queries, good for security and performance
    statement = """
                  INSERT INTO dep (ndep, nome, local) 
                          VALUES ( %s,   %s ,   %s )"""

    values = (payload["ndep"], payload["localidade"], payload["nome"])

    try:
        cur.execute(statement, values)
        cur.execute("commit")
        result = 'Inserted!'
    except (Exception, psycopg2.DatabaseError) as error:
        logger.error(error)
        result = 'Failed!'
    finally:
        if conn is not None:
            conn.close()

    return jsonify(result)




##
##      Demo PUT
##
## Update a department based on the a JSON payload
##
## To use it, you need to use postman or curl: 
##
##   curl -X PUT http://localhost:8080/departments/ -H "Content-Type: application/json" -d '{"ndep": 69, "localidade": "Porto"}'
##

@app.route("/departments/", methods=['PUT'])
def update_departments():
    logger.info("###              DEMO: PUT /departments              ###");   
    content = request.get_json()

    conn = db_connection()
    cur = conn.cursor()


    #if content["ndep"] is None or content["nome"] is None :
    #    return 'ndep and nome are required to update'

    if "ndep" not in content or "localidade" not in content:
        return 'ndep and localidade are required to update'


    logger.info("---- update department  ----")
    logger.info(f'content: {content}')

    # parameterized queries, good for security and performance
    statement ="""
                UPDATE dep 
                  SET local = %s
                WHERE ndep = %s"""


    values = (content["localidade"], content["ndep"])

    try:
        res = cur.execute(statement, values)
        result = f'Updated: {cur.rowcount}'
        cur.execute("commit")
    except (Exception, psycopg2.DatabaseError) as error:
        logger.error(error)
        result = 'Failed!'
    finally:
        if conn is not None:
            conn.close()
    return jsonify(result)





'''



def geraRandom():
    return random.randint(1,2500)


def geraId():
    now = datetime.now()
    dt_string = now.strftime("%d%m-%H%M%S")
    return dt_string


@app.route("/utilizador/", methods=['POST'])
def registo_utilizadores():
    logger.info("###              DEMO: POST /utilizador              ###");   
    payload = request.get_json()

    conn = db_connection()
    cur = conn.cursor()

    logger.info("---- new utilizador  ----")
    logger.debug(f'payload: {payload}')

    # parameterized queries, good for security and performance
    statement = """
                  INSERT INTO utilizador (user_name, email,nome, password, genero, nif, data_nasc, estado, contacto, is_ban, is_admin, token) 
                          VALUES ( %s,   %s ,  %s,  %s , %s,   %s ,   %s, %s,   %s ,  %s,  %s,%s )"""

    values = (payload["user_name"], payload["email"], payload["nome"], payload["password"],payload["genero"],payload["nif"],payload["data_nasc"],payload["estado"],payload["contacto"], False ,payload["is_admin"],geraRandom())

    try:
        cur.execute(statement, values)
        cur.execute("commit")

        result = 'Inserted!'
    except (Exception, psycopg2.DatabaseError) as error:
        logger.error(error)
        result = 'Failed!'
    finally:
        if conn is not None:
            conn.close()

    return jsonify(result)

@app.route("/artigo/", methods=['POST'])
def criar_artigo():
    logger.info("###              DEMO: POST /artigo              ###");   
    payload = request.get_json()

    conn = db_connection()
    cur = conn.cursor()

    logger.info("---- new artigo  ----")
    logger.debug(f'payload: {payload}')

    # parameterized queries, good for security and performance
    statement = """
                  INSERT INTO artigo (id_artigo,codigoisbn,nome_artigo,categoria,descricao,user_vendedor,user_vencedor,utilizador_user_name) 
                          VALUES ( %s,   %s ,  %s,  %s , %s,   %s, %s, %s)"""

    values = (payload["id_artigo"],payload["codigoisbn"],payload["nome_artigo"],payload["categoria"],payload["descricao"],payload["utilizador_user_name"],payload["user_vencedor"],payload["utilizador_user_name"])

    try:
        cur.execute(statement, values)
        cur.execute("commit")

        #result = 'Inserted Artigo!'

      
        statement = """
                INSERT INTO leilao (id_leilao,data_ini,data_fim,preco_base,is_ativo,artigo_id_artigo) 
                        VALUES ( %s,   %s ,  %s,  %s , %s,   %s)"""

        values = (payload["id_leilao"],payload["data_ini"],payload["data_fim"],payload["preco_base"],payload["is_ativo"],payload["id_artigo"])

        try:
            cur.execute(statement, values)
            cur.execute("commit")

            result = {"leilaoId":payload["id_leilao"]}

        except (Exception, psycopg2.DatabaseError) as error:
            logger.error(error)
            #result = 'Failed to insert leilao!'
            result = {"erro" : str(error)}

    except (Exception, psycopg2.DatabaseError) as error:
        logger.error(error)
        #result = 'Failed!'
        result = {"erro" : str(error)}
    finally:
        if conn is not None:
            conn.close()

    return jsonify(result)


@app.route("/leilao/", methods=['GET'], strict_slashes=True)
def get_all_leiloes():
    logger.info("###              DEMO: GET /leilao             ###");   

    conn = db_connection()
    cur = conn.cursor()

    cur.execute("""SELECT leilao.id_leilao,artigo.descricao,artigo.codigoisbn FROM leilao,artigo""")
    rows = cur.fetchall()

    payload = []
    logger.debug("---- leiloes  ----")
    for row in rows:
        logger.debug(row)
        content = {'leilaoId': int(row[0]), 'descricao': row[1]}
        payload.append(content) # appending to the payload to be returned

    cur.close()
    conn.close()
    return jsonify(payload)


@app.route("/leiloes/<keyword>", methods=['GET'])
def search_leilao(keyword):
    logger.info("###              DEMO: GET /leilao             ###");   

    conn = db_connection()
    cur = conn.cursor()

    cur.execute("""SELECT leilao.id_leilao,artigo.descricao,artigo.codigoisbn FROM leilao,artigo""")
    
    payload = []

    logger.debug("---- leiloes  ----")
    logger.debug(keyword)
    for row in cur.fetchall():
        logger.debug(row)
        if(keyword.isdecimal()):
            if(int(keyword) == row[2]):
                content = {'leilaoId': row[0],'descricao': row[1]}
                payload.append(content)

        else:
            if(keyword in row[1]):
                content = {'leilaoId': row[0],'descricao': row[1]}
                payload.append(content)
    

    cur.close()
    conn.close()
    return jsonify(payload)

@app.route("/leilao/<leilaoId>", methods=['GET'])
def consult_leilao(leilaoId):
    logger.info("###              DEMO: GET /leilao             ###");   

    conn = db_connection()
    cur = conn.cursor()

    cur.execute("""SELECT leilao.id_leilao,artigo.descricao,leilao.data_ini,leilao.data_fim,leilao.preco_base,artigo.nome_artigo,artigo.categoria FROM leilao,artigo
            WHERE leilao.artigo_id_artigo = artigo.id_artigo and leilao.id_leilao = %s;""", (str(leilaoId),) )
    
    payload = []

    logger.debug("---- leiloes  ----")
    logger.debug(leilaoId)
    for row in cur.fetchall():
        logger.debug(row)
        content = {'leilaoId': row[0],'descricao': row[1],"data_ini": row[2],"data_fim":row[3],"preco_base":row[4],"nome_artigo": row[5],"categoria": row[6]}
        payload.append(content)


    cur.close()
    conn.close()
    return jsonify(payload)
#7
@app.route("/leiloes/<user>", methods=['GET'])
def get_all_leiloes_from_user(user):
    logger.info("###              DEMO: GET /user/leiloes             ###");   
    conn = db_connection()
    cur = conn.cursor()

    cur.execute("""SELECT id_leilao, user_name FROM registolicitacao""")

    content = {}
    leiloes = []
    
    logger.debug("Vou imprimir da tabela registolicitacao")
    for row in cur.fetchall():
        #logger.debug(f'row: {row}')
        #logger.debug(f'user = {user}')
        if (row[1] == user):
            #logger.debug("encontrei")
            leiloes.append(row[0])
            
    payload = {'leiloesIds':leiloes}

        
    cur.close()
    conn.close()
    return jsonify(payload)




##########################################################
## DATABASE ACCESS
##########################################################

def db_connection():
    db = psycopg2.connect(user = "postgres",
                            password = "django500",
                            host = "localhost",
                            port = "5432",
                            database = "projeto")
    return db


##########################################################
## MAIN
##########################################################
if __name__ == "__main__":

    # Set up the logging
    logging.basicConfig(filename="logs/log_file.log")
    logger = logging.getLogger('logger')
    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    # create formatter
    formatter = logging.Formatter('%(asctime)s [%(levelname)s]:  %(message)s',
                              '%H:%M:%S')
                              # "%Y-%m-%d %H:%M:%S") # not using DATE to simplify
    ch.setFormatter(formatter)
    logger.addHandler(ch)


    time.sleep(1) # just to let the DB start before this print :-)


    logger.info("\n---------------------------------------------------------------\n" + 
                  "API v1.0 online: http://localhost:8080/utilizador/\n\n")


    

    app.run(host="0.0.0.0", debug=True, threaded=True)