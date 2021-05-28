import psycopg2
from datetime import datetime


#artigo(ID_Artigo,ID_Leilao,Inicio,Fim),leilao(ID_Leilao,Inicio,Fim),utilizador(ID_Utilizador,NOME,IDADE,MORADA,GENERO,NACIONALIDADE,SEXO,TELEFONE)
def geraId():
    now = datetime.now()
    dt_string = now.strftime("%d%m-%H%M%S")
    return dt_string


def getConnection():
    con = psycopg2.connect(user = "postgres",
                            password = "django500",
                            host = "localhost",
                            port = "5432",
                            database = "projeto")
    return con


def insertLeilao():
    con = getConnection()
    cursor = con.cursor()
    inicio = input("Data de inicio: ")
    fim = input("Data de inicio: ")
    postgres_insert_query = """ INSERT INTO leilao (ID_Leilao,Inicio,FIM) VALUES(%s,%s,%s)"""
    record_to_insert = (geraId(),inicio,fim)
    cursor.execute(postgres_insert_query,record_to_insert)
    con.commit()

    cursor.close()
    con.close()


def insertArtigo():
    con = getConnection()
    cursor = con.cursor()
    id_leilao = input("Id do leilao: ")
    inicio = input("Data de inicio: ")
    fim = input("Data de inicio: ")
    postgres_insert_query = """ INSERT INTO artigo (ID_Artigo,ID_Leilao,Inicio,Fim) VALUES(%s,%s,%s,%s)"""
    record_to_insert = (geraId(),id_leilao,inicio,fim)
    cursor.execute(postgres_insert_query,record_to_insert)
    con.commit()

    cursor.close()
    con.close()


def printLeilao():
    con = getConnection()
    cursor = con.cursor()
    cursor.execute("""SELECT * FROM leilao""")
    for row in cursor.fetchall():
        print(row)

    cursor.close()
    con.close()


def printArtigo():
    con = getConnection()
    cursor = con.cursor()
    cursor.execute("""SELECT * FROM artigo""")
    for row in cursor.fetchall():
        print(row)

    cursor.close()
    con.close()


def insertUtilizador():
    con = getConnection()
    cursor = con.cursor()

    nome = input("Insira o seu nome: ")
    idade = input("Insira a sua idade: ")
    morada = input("Insira a sua morada: ")
    genero = input("Insira o seu genero: ")
    nacionalidade = input("Insira a sua nacionalidade: ")
    telefone = input("Insira o seu telefone: ")

    postgres_insert_query = """ INSERT INTO utilizador (ID_Utilizador,NOME,IDADE,MORADA,GENERO,NACIONALIDADE,TELEFONE) VALUES(%s,%s,%s,%s,%s,%s,%s)"""
    record_to_insert = (geraId(),nome,int(idade),morada,genero,nacionalidade,telefone)
    cursor.execute(postgres_insert_query,record_to_insert)
    con.commit()

    cursor.close()
    con.close()


def printUtilizador():
    con = getConnection()
    cursor = con.cursor()
    cursor.execute("""SELECT * FROM utilizador""")
    for row in cursor.fetchall():
        print(row)

    cursor.close()
    con.close()


def cleanLeilao():
    con = getConnection()
    cursor = con.cursor()

    cursor.execute("""DELETE FROM leilao""")
    con.commit()

    cursor.close()
    con.close()


def cleanArtigo():
    con = getConnection()
    cursor = con.cursor()

    cursor.execute("""DELETE FROM artigo""")
    con.commit()

    cursor.close()
    con.close()


def cleanUtilizador():
    con = getConnection()
    cursor = con.cursor()

    cursor.execute("""DELETE FROM utilizador""")
    con.commit()

    cursor.close()
    con.close()


def menu():
    while(True):
        print("(1) Mostrar Valores\n(2) Inserir Valores\n(3) Limpar tabelas\n(0) Exit")
        escolha = input("Escolha: ")

        if(escolha == '1'):
            print("(1) Mostrar Leiloes\n(2) Mostrar Artigos\n(3) Mostrar Utilizadores")
            escolha = input("Escolha: ")
            if(escolha == '1'):
                print("==========")
                printLeilao()
                print("==========")
            elif(escolha == '2'):
                print("==========")
                printArtigo()
                print("==========")

            elif(escolha == '3'):
                print("==========")
                printUtilizador()
                print("==========")

        elif(escolha == '2'):
            print("(1) Inserir Leilao\n(2) Inserir Artigo\n(3) Inserir Utilizador")
            escolha = input("Escolha: ")
            if(escolha == '1'):
                print("==========")
                insertLeilao()
                print("==========")
            elif(escolha == '2'):
                print("==========")
                insertArtigo(2)
                print("==========")
            elif(escolha == '3'):
                print("==========")
                insertUtilizador()
                print("==========")
                
        elif(escolha == '3'):
            print("(1) Limpar Leilao\n(2) Limpar Artigo\n(3) Limpar Utilizador")
            escolha = input("Escolha: ")
            if(escolha == '1'):
                cleanLeilao()
            elif(escolha == '2'):
                cleanArtigo()
            elif(escolha == '3'):
                cleanUtilizador()
            
        elif(escolha == '0'):
            break

#insertLeilao(32,'27/05','02/06')
#printTable()
#geraId()
#insertArtigo(geraId(),123456,'30/05','07/06')
#printArtigo()

def procuraItem(keyword):
    con = getConnection()
    cursor = con.cursor()

    cursor.execute("""SELECT leilao.id_leilao,artigo.descricao,artigo.codigoisbn FROM leilao,artigo""")
    for row in cursor.fetchall():
        if(keyword.isdecimal()):
            if(row[2] == int(keyword)):
                print(row)
        else:
            if(keyword in row[1]):
                print(row)
    

    cursor.close()
    con.close()


def consultaItem(keyword):
    con = getConnection()
    cursor = con.cursor()

    cursor.execute("""SELECT leilao.id_leilao,artigo.descricao,artigo.codigoisbn FROM leilao,artigo
            WHERE leilao.artigo_id_artigo = artigo.id_artigo and leilao.id_leilao = %s;""", (str(keyword),) )
    for row in cursor.fetchall():
        print(row)

    cursor.close()
    con.close()

consultaItem(77451)