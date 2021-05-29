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
tokens_online=list()


def geraToken():
    global tokens_online
    aux = random.randint(1,25000)
    
    while(aux in tokens_online):
        aux = random.randint(1,25000)
    
    tokens_online.append(aux)
    return aux


def geraId():
    now = datetime.now()
    dt_string = now.strftime("%d%m-%H%M%S")
    return dt_string


@app.route("/registoUtilizador/", methods=['POST'])
def registo_utilizadores():
    logger.info("###             POST /utilizador              ###");   
    payload = request.get_json()

    conn = db_connection()
    cur = conn.cursor()

    logger.info("---- new utilizador  ----")
    logger.debug(f'payload: {payload}')

    # parameterized queries, good for security and performance
    statement = """
                  INSERT INTO utilizador (user_name, email,nome, password, genero, nif, data_nasc, estado, contacto, is_ban, is_admin) 
                          VALUES ( %s,   %s ,  %s,  %s , %s,   %s ,   %s, %s,   %s ,  %s,  %s,%s )"""

    
    values = (payload["user_name"], payload["email"], payload["nome"], payload["password"],payload["genero"],payload["nif"],payload["data_nasc"],payload["estado"],payload["contacto"], False ,payload["is_admin"])

    try:
        cur.execute(statement, values)
        cur.execute("commit")

        result = {"user_name":  payload["user_name"]}
    except (Exception, psycopg2.DatabaseError) as error:
        logger.error(error)
        result = {"erro" : str(error)}
    finally:
        if conn is not None:
            conn.close()
            cur.close()

    return jsonify(result)

@app.route("/artigo/", methods=['POST'])
def criar_artigo():
    logger.info("###              DEMO: POST /artigo              ###");   
    payload = request.get_json()

    if(payload["token"] not in tokens_online):
        logger.debug(tokens_online)
        return(jsonify({'token invalido': payload["token"]}))
   
    conn = db_connection()
    cur = conn.cursor()

    logger.info("---- new artigo  ----")
    logger.debug(f'payload: {payload}')

    # parameterized queries, good for security and performance
    statement = """
                  INSERT INTO artigo (id_artigo,codigoisbn,nome_artigo,categoria,descricao,user_vencedor,utilizador_user_name) 
                          VALUES (%s ,  %s,  %s , %s,   %s, %s, %s)"""

    values = (payload["id_artigo"],payload["codigoisbn"],payload["nome_artigo"],payload["categoria"],payload["descricao"],"",payload["utilizador_user_name"])

    try:
        cur.execute(statement, values)
        cur.execute("commit")

        #result = 'Inserted Artigo!'

      
        statement = """
                INSERT INTO leilao (id_leilao,data_ini,data_fim,preco_base,is_ativo,artigo_id_artigo) 
                        VALUES ( %s,   %s ,  %s,  %s , %s,   %s)"""

        values = (payload["id_leilao"],payload["data_ini"],payload["data_fim"],payload["preco_base"],True,payload["id_artigo"])

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
    
    dados = request.get_json()
    
    if(dados["token"] not in tokens_online):
        logger.debug(tokens_online)
        return(jsonify({'token invalido': dados["token"]}))
    
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

    dados = request.get_json()
    
    if(dados["token"] not in tokens_online):
        logger.debug(tokens_online)
        return(jsonify({'token invalido': dados["token"]}))

    conn = db_connection()
    cur = conn.cursor()

    cur.execute("""SELECT leilao.id_leilao,artigo.descricao,artigo.codigoisbn FROM leilao,artigo""")
    dados = request.get_json()
    

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

    dados = request.get_json()
    
    if(dados["token"] not in tokens_online):
        logger.debug(tokens_online)
        return(jsonify({'token invalido': dados["token"]}))

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
@app.route("/leiloes/user/<user>", methods=['GET'])
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



    #payload = {'leiloesIds':leiloes}
    payload = []

    #cur.execute("""SELECT * FROM leilao""")
    for leilaoId in leiloes:
        cur.execute("""SELECT leilao.id_leilao,artigo.descricao,leilao.data_ini,leilao.data_fim,leilao.preco_base,artigo.nome_artigo,artigo.categoria FROM leilao,artigo
                    WHERE leilao.artigo_id_artigo = artigo.id_artigo and leilao.id_leilao = %s;""", (str(leilaoId),) )
        for row in cur.fetchall():
            logger.debug(row)
            content = {'leilaoId': row[0],'descricao': row[1],"data_ini": row[2],"data_fim":row[3],"preco_base":row[4],"nome_artigo": row[5],"categoria": row[6]}
            payload.append(content)

    cur.close()
    conn.close()
    return jsonify({'leiloes':payload})




@app.route("/login/", methods=['PUT'])
def login():
    logger.info("###             Login              ###");   
    content = request.get_json()

    conn = db_connection()
    cur = conn.cursor()


    #if content["ndep"] is None or content["nome"] is None :
    #    return 'ndep and nome are required to update'

    if "user_name" not in content or "password" not in content:
        return 'user_name and password are required to login'


    logger.info("---- login  ----")
    logger.info(f'content: {content}')

    # parameterized queries, good for security and performance
    #como o user_name e unico basta fazermos assim e nao temos que contar as rows
    statement ="""

                select user_name , password
                from utilizador
                where user_name = %s and password = %s """


    values = (content["user_name"], content["password"])

    token_aux = geraToken()
    try:
        res = cur.execute(statement, values)
        result = 'login correto'
        cur.execute("commit")

        
        statement2 ="""

                UPDATE utilizador
                SET token = %s
                WHERE user_name = %s """

        values = (token_aux,content["user_name"])

        try:
            res = cur.execute(statement2, values)
            result = {"authToken": token_aux}
            cur.execute("commit")
        except (Exception, psycopg2.DatabaseError) as error:
            logger.error(error)
            result = {"erro" : str(error)}




    except (Exception, psycopg2.DatabaseError) as error:
        logger.error(error)
        result = {"erro" : str(error)}
    finally:
        if conn is not None:
            conn.close()
            cur.close()
    return jsonify(result)



#9
@app.route("/leilao/editar/<leilaoId>", methods=['PUT'])
def editar_leilao(leilaoId):
    logger.info("###          Editar Leilão           ###");   
    content = request.get_json()

    if(content["token"] not in tokens_online):
        logger.debug(tokens_online)
        return(jsonify({'token invalido': content["token"]}))


    conn = db_connection()
    cur = conn.cursor()

    #TODO:Copiar as rows que sao alteradas para a tabela updateartigo e alterar a tabela para guardar todos os dados que podem ser alterados
    statement = """SELECT artigo_id_artigo FROM leilao
                    WHERE id_leilao = %s;"""
    values = (str(leilaoId),)

    cur.execute(statement, values)
    rows = cur.fetchall()
    leilaoId = rows[0][0]
    logger.debug("leilaoId = " + str(leilaoId))

    keys_leilao = ['data_ini', 'data_fim', 'preco_base']
    keys_artigo = ['codigoisbn', 'nome_artigo', 'categoria', 'descricao', 'user_vendedor', 'utilizador_user_name']

    logger.debug(content)
    for key,val in content.items():
        if key in keys_leilao:
            statement = """UPDATE leilao
                    SET """ + key + """ = %s
                    WHERE id_leilao = %s"""
            values = (str(val), str(leilaoId))
        elif key in keys_artigo:
            statement = """UPDATE artigo
                    SET """ + key + """ = %s
                    WHERE id_artigo = %s"""
            values = (str(val), str(leilaoId))
        elif key == "token":
            continue
        else:
            logger.debug("parametro nao existe nas tabelas leilao ou artigo")
            return
        
        cur.execute(statement, values)

    statement = """SELECT * FROM leilao,artigo
                WHERE leilao.artigo_id_artigo = artigo.id_artigo and leilao.id_leilao = %s;"""
    values = (str(leilaoId),)
    cur.execute(statement, values)

    rows = cur.fetchall()


    return jsonify({'leilao':rows})



##########################################################
## DATABASE ACCESS
##########################################################

def db_connection():
    db = psycopg2.connect(user = "postgres",
                            password = "postgresql1",
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