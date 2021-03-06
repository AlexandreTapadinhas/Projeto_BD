import psycopg2
from datetime import datetime,timedelta


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

def testeArgumentos(id_leilao,preco_base):
    con = getConnection()
    cursor = con.cursor()

    cursor.execute("""SELECT id_leilao,artigo_id_artigo FROM leilao WHERE id_leilao = %s and preco_base = %s;""",(id_leilao,preco_base))
    for row in cursor.fetchall():
        print(row)

    cursor.close()
    con.close()

def comparaDatas(inicio,now,fim):
    ini = inicio.split("-")
    f = fim.split("-")
    n = now.split("-")
    for i in range(len(ini)):
        ini[i] = int(ini[i])
        n[i] = int(n[i])
        f[i] = int(f[i])

    if((ini[2] <= n[2]) and (n[2] <= f[2])):
        if((ini[2] < n[2]) and (n[2] < f[2])):
            return True
        elif(ini[2] == n[2]): #comparar o now ao inicio
            if(ini[1] < n[1]):
                return True
            elif(ini[1] == n[1]):
                if(ini[0] < n[0]):
                    return True
                else:
                    return False 
            else:
                return False
        else: #comparar o now ao fim
            if(n[1] < f[1]):
                return True
            elif(n[1] == f[1]):
                if(n[0] < f[0]):
                    return True
                else:
                    return False
            
            else:
                return False

            
   
   
def teste(data):
    return data.year
   
def getNumLeiloes():
    con = getConnection()
    cursor = con.cursor()

    #TOP 10 artigos
    #cursor.execute("""SELECT utilizador.user_name,count(*)
    #FROM utilizador,artigo 
    #WHERE utilizador.user_name = artigo.utilizador_user_name
    #GROUP BY utilizador.user_name""")


    cursor.execute("""SELECT utilizador.user_name,count(*)
    FROM utilizador,artigo,leilao 
    WHERE utilizador.user_name = artigo.utilizador_user_name and artigo.id_artigo = leilao.artigo_id_artigo
    GROUP BY utilizador.user_name
    ORDER BY count(*) DESC""")

    #cursor.execute("""SELECT artigo.utilizador_user_name,count(*)
    #FROM artigo,leilao,utilizador
    #WHERE artigo.id_artigo = leilao.artigo_id_artigo and artigo.utilizador_user_name = utilizador.user_name
    #GROUP BY artigo.utilizador_user_name""")

    #TOP10 vencedores de leiloes
    #cursor.execute(""" SELECT leilao.user_vencedor,count(*)
   # FROM leilao
    #GROUP BY leilao.user_vencedor
    # """)
    
    for row in cursor.fetchall():
        print(row)

    cursor.close()
    con.close()
#print(comparaDatas("01-06-2021","02-06-2021","03-07-2021"))


#"data_ini": "01-06-2021",
#    "data_fim": "14-06-2021",
#print(geraId())
#testeArgumentos(778451,1750)

def testeDatas():
    con = getConnection()
    cursor = con.cursor()

    now = datetime.now()
    limite = datetime.now() -timedelta(days = 10)

    print(limite)
    cursor.execute("""SELECT count(*) FROM leilao WHERE data_ini > %s and data_ini < %s""",(limite,now))

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    con.close()

testeDatas()