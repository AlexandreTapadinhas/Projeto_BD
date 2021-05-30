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

from encryption_functions import *

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
tokens_online={}  #{"token" : "user_name"}


def geraToken(user_name):
    global tokens_online
    aux = random.randint(1,25000)
    
    while(aux in tokens_online.keys()):
        aux = random.randint(1,25000)
    
    tokens_online[aux] = user_name
    return aux


def geraId():
    now = datetime.now()
    dt_string = now.strftime("%d%m-%H%M%S")
    return dt_string

#1
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
                          VALUES ( %s,   %s ,  %s,  %s , %s,   %s ,   %s, %s,   %s ,  %s,  %s )"""

    
    values = (payload["user_name"], payload["email"], payload["nome"], payload["password"],payload["genero"],payload["nif"],payload["data_nasc"],payload["estado"],payload["contacto"], False ,payload["is_admin"])

    try:
        cur.execute(statement, values)
        cur.execute("commit")

        result = {"user_name":  payload["user_name"]}
    except (Exception, psycopg2.DatabaseError) as error:
        logger.error(error)
        cur.rollback()
        result = {"erro" : str(error)}
    finally:
        if conn is not None:
            conn.close()
            cur.close()

    return jsonify(result)

#3
@app.route("/artigo/", methods=['POST'])
def criar_artigo():
    logger.info("###              DEMO: POST /artigo              ###");   
    payload = request.get_json()

    if(payload["token"] not in tokens_online.keys()):
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
        #cur.execute("commit")

        #result = 'Inserted Artigo!'

      
        statement = """
                INSERT INTO leilao (id_leilao,data_ini,data_fim,preco_base,artigo_id_artigo) 
                        VALUES ( %s,   %s ,  %s,  %s , %s)"""

        values = (payload["id_leilao"],payload["data_ini"],payload["data_fim"],payload["preco_base"],payload["id_artigo"])

        try:
            cur.execute(statement, values)
            cur.execute("commit")

            result = {"leilaoId":payload["id_leilao"]}

        except (Exception, psycopg2.DatabaseError) as error:
            logger.error(error)
            cur.rollback()
            #result = 'Failed to insert leilao!'
            result = {"erro" : str(error)}

    except (Exception, psycopg2.DatabaseError) as error:
        logger.error(error)
        cur.rollback()
        #result = 'Failed!'
        result = {"erro" : str(error)}
    finally:
        if conn is not None:
            conn.close()

    return jsonify(result)

#4
@app.route("/leilao/", methods=['GET'], strict_slashes=True)
def get_all_leiloes():
    logger.info("###              DEMO: GET /leilao             ###");   
    
    dados = request.get_json()
    
    if(dados["token"] not in tokens_online.keys()):
        logger.debug(tokens_online)
        return(jsonify({'token invalido': dados["token"]}))
    
    conn = db_connection()
    cur = conn.cursor()

    cur.execute("""SELECT leilao.id_leilao,artigo.descricao,artigo.codigoisbn
                FROM leilao,artigo
                WHERE artigo_id_artigo = id_artigo""")
    
    rows = cur.fetchall()
    print(rows)
    payload = []
    
  

    logger.debug("---- leiloes  ----")
    for row in rows:
        content = {}
        logger.debug(row)
        content = {'leilaoId': int(row[0]), 'descricao': row[1]}
        payload.append(content) # appending to the payload to be returned

    cur.close()
    conn.close()
    result = {}
    result["lista_leiloes"] = payload
    return jsonify(result)

#5
@app.route("/leiloes/<keyword>", methods=['GET'])
def search_leilao(keyword):
    logger.info("###              DEMO: GET /leilao             ###");   

    dados = request.get_json()
    
    if(dados["token"] not in tokens_online.keys()):
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

#6
@app.route("/leilao/<leilaoId>", methods=['GET'])
def consult_leilao(leilaoId):
    logger.info("###              DEMO: GET /leilao             ###");   
    dados = request.get_json()
    #TODO: Imprimir msg do mural e registo de licitacoes
    #TODO: Verificar datas
    if(dados["token"] not in tokens_online.keys()):
        logger.debug(tokens_online)
        return(jsonify({'token invalido': dados["token"]}))

    conn = db_connection()
    cur = conn.cursor()


    cur.execute("""SELECT leilao.id_leilao,artigo.descricao,leilao.data_ini,leilao.data_fim,leilao.preco_base,artigo.nome_artigo,artigo.categoria
                FROM leilao,artigo
                WHERE leilao.artigo_id_artigo = artigo.id_artigo and leilao.id_leilao = %s""", (str(leilaoId),) )
    
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

    dados = request.get_json()
    #TODO: Verificar datas
    #TODO: Falta checkar os criadores do leilão
    if(dados["token"] not in tokens_online.keys()):
        logger.debug(tokens_online)
        return(jsonify({'token invalido': dados["token"]}))

    conn = db_connection()
    cur = conn.cursor()
    try:
        cur.execute("""SELECT id_leilao, user_name FROM registolicitacao""")
        cur.execute("commit")

    except (Exception, psycopg2.DatabaseError) as error:
        logger.error(error)
        cur.rollback()
        result = {"erro":str(error)}
        cur.close()
        conn.close()
        return jsonify(result)


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
        try:
            cur.execute("""SELECT leilao.id_leilao,artigo.descricao,leilao.data_ini,leilao.data_fim,leilao.preco_base,artigo.nome_artigo,artigo.categoria FROM leilao,artigo
                        WHERE leilao.artigo_id_artigo = artigo.id_artigo and leilao.id_leilao = %s;""", (str(leilaoId),) )
            cur.execute("commit")
        except (Exception, psycopg2.DatabaseError) as error:
            logger.error(error)
            cur.rollback()
            result = {"erro":str(error)}
            cur.close()
            conn.close()
            return jsonify(result)

        for row in cur.fetchall():
            logger.debug(row)
            content = {'leilaoId': row[0],'descricao': row[1],"data_ini": row[2],"data_fim":row[3],"preco_base":row[4],"nome_artigo": row[5],"categoria": row[6]}
            payload.append(content)

    cur.close()
    conn.close()
    return jsonify({'leiloes':payload})



#2
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

    token_aux = geraToken(content["user_name"])
    try:
        res = cur.execute(statement, values)
        result = {'authToken': token_aux}
        cur.execute("commit")


    except (Exception, psycopg2.DatabaseError) as error:
        logger.error(error)
        cur.rollback()
        result = {"erro":str(error)}
        cur.close()
        conn.close()
        return jsonify(result)
    finally:
        if conn is not None:
            conn.close()
            cur.close()
    return jsonify(result)

#colocar is_ativo == false
def put_is_ativo_false( id_leilao):
    conn = db_connection()
    cur = conn.cursor()

    statement = """
            UPDATE leilao
            SET is_ativo = %s
            WHERE id_leilao = %s"""


    values = (False, id_leilao)  
    

    try:
        cur.execute(statement, values)
        cur.execute("commit")

    except (Exception, psycopg2.DatabaseError) as error:
        cur.rollback()
        logger.error(error)

    #notificar o user !!! vencedor 

    statement = """
                INSERT INTO notificacao (id_noti,msg, data, is_open, utilizador_user_name) 
                VALUES (  %s,   %s ,  %s,  %s ,%s)"""


    msg="Parabéns : Ganhou o leilao "+id_leilao+"!!!"

    try:
        cur.execute("""
                select user_vencedor
                from leilao
                WHERE id_leilao = %s""", (id_leilao,))

        username= cur.fetchall()
        username=username[0][0]
        cur.execute("commit")
    except (Exception, psycopg2.DatabaseError) as error:
        logger.error(error)

    try:
        cur.execute("""
                select max(id_noti)
                from notificacao """)
        id_noti=cur.fetchall()
        id_noti = id_noti[0][0]
        cur.execute("commit")
    except (Exception, psycopg2.DatabaseError) as error:
        logger.error(error)

    id_noti = id_noti+1
    values = (id_noti, msg, datetime.today(), False, username )  
    

    try:
        cur.execute(statement, values)
        cur.execute("commit")

    except (Exception, psycopg2.DatabaseError) as error:
        cur.rollback()
        logger.error(error)

    finally:
        if conn is not None:
            cur.close()
            conn.close()
       

#8
@app.route("/leiloes/<id_leilao>/<licitacao>", methods=['GET'])
def licitar(id_leilao, licitacao):
    logger.info("###              DEMO: GET /licitar              ###");   

    logger.debug(f'id_leilao: {id_leilao}')


    payload = request.get_json()

    if(payload["token"] not in tokens_online.keys()):
        logger.debug(tokens_online)
        return(jsonify({'token invalido': payload["token"]}))

    conn = db_connection()
    cur = conn.cursor()

    #cur.execute("begin transaction")
    #execute -> ja comeca a transation

    cur.execute("SELECT data_ini, data_fim, preco_atual, is_ativo, is_canceled FROM leilao where id_leilao = %s", (id_leilao,) )
    rows = cur.fetchall()

    row = rows[0]
    if(row[3] == True):
        if(row[4] == False):
            if(row[0]<= datetime.today() and row[1]>datetime.today()):
                if(row[2]<int(licitacao)):
                        statement = """
                            UPDATE leilao
                            SET preco_atual = %s , user_vencedor = %s
                            WHERE id_leilao = %s"""

            
                        values = (licitacao,tokens_online[payload["token"]], id_leilao)                                

                        try:
                            cur.execute(statement, values)
                            cur.execute("commit")
                            #cur.commit()

                            #por na tabela registo licitacao
                            statement = """
                                    INSERT INTO registolicitacao (preco_licitacao,data_licitacao, leilao_id_leilao, utilizador_user_name) 
                                    VALUES (  %s,   %s ,  %s,  %s )"""
                                    

                            values = (licitacao,datetime.today(), id_leilao , tokens_online[payload["token"]])  
                            

                            try:
                                cur.execute(statement, values)
                                cur.execute("commit")

                            except (Exception, psycopg2.DatabaseError) as error:
                                cur.rollback()
                                logger.error(error)
                                content = {"erro" : str(error)}
                    

                            content = 'Sucesso'
                        except (Exception, psycopg2.DatabaseError) as error:
                            logger.error(error)
                            cur.rollback()
                            content = {"erro" : str(error)}
                        finally:
                            if conn is not None:
                                cur.close()
                                conn.close()
                                
                else:
                    cur.execute("commit")
                    cur.close()
                    conn.close ()
                    return 'Erro: o valor do artigo e maior que a licitacao'
            else:
                #por o is_ativo a false
                cur.execute("commit")
                put_is_ativo_false( id_leilao)
                cur.close()
                conn.close ()
                return'Erro leilao ja acabou/ainda nao comecou'
        else:
            cur.execute("commit")
            put_is_ativo_false( id_leilao)
            cur.close()
            conn.close ()
            return'Erro: leilao foi desativado pelo admin'
    else:
            cur.execute("commit")
            cur.close()
            conn.close ()
            return'Erro: leilao ja terminou'

    logger.debug("---- licitou  ----")
    logger.debug(row)

    return jsonify(content)




#9
@app.route("/leilao/editar/<leilaoId>", methods=['PUT'])
def editar_leilao(leilaoId):
    logger.info("###          Editar Leilão           ###");   
    content = request.get_json()

    if(content["token"] not in tokens_online.keys()):
        logger.debug(tokens_online)
        return(jsonify({'token invalido': content["token"]}))


    conn = db_connection()
    cur = conn.cursor()

    statement = """SELECT leilao.id_leilao, leilao.data_ini, leilao.data_fim, leilao.preco_base, artigo.nome_artigo, artigo.categoria, artigo.descricao, leilao.artigo_id_artigo
                FROM leilao, artigo
                WHERE leilao.id_leilao = %s and artigo.id_artigo = leilao.artigo_id_artigo;"""

    values = (leilaoId,)
    
    try:
        cur.execute(statement, values)
        cur.execute("commit")

    
    except (Exception, psycopg2.DatabaseError) as error:
        logger.error(error)
        cur.rollback()
        result = {"erro":str(error)}
        cur.close()
        conn.close()
        return jsonify(result)

    rows = cur.fetchall()
    logger.debug("len(rows) = " + str(len(rows)))
    row = rows[0]
    logger.debug("len(row) = " + str(len(row)))


    statement = """INSERT INTO updateartigo 
                VALUES (%s, %s ,%s, %s, %s, %s, %s, %s, %s);"""
    
    values = (datetime.today(), row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])

    leilaoId = row[0]

    try:
        cur.execute(statement, values)
        cur.execute("commit")
    except (Exception, psycopg2.DatabaseError) as error:
        logger.error(error)
        cur.rollback()
        result = {"erro":str(error)}
        cur.close()
        conn.close()
        return jsonify(result)

    
    logger.debug("leilaoId = " + str(leilaoId))

    keys_leilao = ['data_ini', 'data_fim', 'preco_base']
    keys_artigo = ['nome_artigo', 'categoria', 'descricao']

    #

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
        
        try:
            cur.execute(statement, values)
            cur.execute("commit")
        except (Exception, psycopg2.DatabaseError) as error:
            logger.error(error)
            cur.rollback()
            result = {"erro":str(error)}
            cur.close()
            conn.close()
            return jsonify(result)

    statement = """SELECT * FROM leilao,artigo
                WHERE leilao.artigo_id_artigo = artigo.id_artigo and leilao.id_leilao = %s;"""
    values = (str(leilaoId),)
    try:
        cur.execute(statement, values)
        cur.execute("commit")

        rows = cur.fetchall()
    except (Exception, psycopg2.DatabaseError) as error:
        logger.error(error)
        cur.rollback()
        result = {"erro":str(error)}
        cur.close()
        conn.close()
        return jsonify(result)
    finally:
        if conn is not None:
            cur.close()
            conn.close()

    
    return jsonify({'leilao':rows})


#10
@app.route("/escreve_msg_mural", methods=['POST'])
def escreve_msg_mural():

    content = request.get_json()

    if(content["token"] not in tokens_online.keys()):
        logger.debug(tokens_online)
        return(jsonify({'token invalido': content["token"]}))


    logger.info("###             POST /escreve_msg_mural              ###");   


    conn = db_connection()
    cur = conn.cursor()

    logger.info("---- new msg  ----")
    logger.debug(f'content: {content}')

    # parameterized queries, good for security and performance
    statement = """
                  INSERT INTO utilizador (texto, data_pub, leilao_id_leilao, utilizador_user_name) 
                          VALUES ( %s,   %s ,  %s,  %s , %s )"""

    
    values = (content["texto"], datetime.today(), content["id_leilao"], tokens_online[content["token"]])

    try:
        cur.execute(statement, values)
        cur.execute("commit")

        result = 'Mensagem publicada com sucesso'
    except (Exception, psycopg2.DatabaseError) as error:
        logger.error(error)
        cur.rollback()
        result = {"erro" : str(error)}
    finally:
        if conn is not None:
            conn.close()
            cur.close()

    return jsonify(result)

#extra1
@app.route("/comentarios/<leilaoId>", methods=['GET'])
def listar_comentarios(leilaoId):
    dados = request.get_json()
    if(dados["token"] not in tokens_online.keys()):
        logger.debug(tokens_online)
        return(jsonify({'token invalido': dados["token"]}))

        
    logger.info("###              DEMO: GET /comentario            ###");   

    conn = db_connection()
    cur = conn.cursor()


    cur.execute("""SELECT texto, data_pub, utilizador_user_name
                FROM comentarios
                WHERE leilao_id_leilao = %s""", (str(leilaoId),) )
    
    payload = []

    logger.debug("---- mural do leilao  ----")
    logger.debug(leilaoId)
    for row in cur.fetchall():
        logger.debug(row)
        content = {'utilizador_user_name': row[2],'data_pub': row[1],"texto": row[0]}
        payload.append(content)


    cur.close()
    conn.close()
    return jsonify({'MURAL LEILAO':payload})


#13 -> termina e lista
@app.route("/terminarLeiloes", methods=['GET'])
def terminar_leiloes():
    dados = request.get_json()
    if(dados["token"] not in tokens_online.keys()):
        logger.debug(tokens_online)
        return(jsonify({'token invalido': dados["token"]}))

        
    logger.info("###              DEMO: GET /terminar leiloes            ###");   

    conn = db_connection()
    cur = conn.cursor()

    try:
        cur.execute("SELECT  data_fim, is_canceled,id_leilao, is_ative FROM leilao" )
        rows = cur.fetchall()
    except (Exception, psycopg2.DatabaseError) as error:
        logger.error(error)
        result = {"erro" : str(error)}
        cur.execute("commit")
        cur.close()
        conn.close()
        return jsonify(result)

    

    logger.debug("---- terminar leiloes  ----")

    payload = []

    for row in rows:
        if((row[0]<= datetime.today() or row[1] == True)and row[3] == True):
            put_is_ativo_false(row[2])

    result="Leiloes terminados!!"
    cur.close()
    conn.close()
    return jsonify(result)



##########################################################
## DATABASE ACCESS
##########################################################

def db_connection():
    db = psycopg2.connect(user = "postgres",
                            password = "bd2021",
                            host = "localhost",
                            port = "5432",
                            database = "projeto")  #dbname
    return db


##########################################################
## MAIN
##########################################################
if __name__ == "__main__":

    read_encryption_key()
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