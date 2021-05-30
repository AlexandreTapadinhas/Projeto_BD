INSERT INTO utilizador (user_name, email,nome, password, genero, nif, data_nasc, estado, contacto, is_ban, is_admin) 
VALUES ('pedro','pedro@gmail.com','pedro tavares','password','masculino',245789632,'01-01-2000','solteiro',987654321,false,false);
INSERT INTO utilizador (user_name, email,nome, password, genero, nif, data_nasc, estado, contacto, is_ban, is_admin) 
VALUES ('tapadinhas','tapadinhas@gmail.com','rui tapadinhas','password','masculino',2478912632,'01-01-2000','solteiro',98521421,false,false);
INSERT INTO utilizador (user_name, email,nome, password, genero, nif, data_nasc, estado, contacto, is_ban, is_admin) 
VALUES ('ines','inestex@gmail.com','ines teixeira','password','feminino',2478974832,'01-01-2000','solteiro',987211125,false,false);

INSERT INTO artigo (id_artigo,codigoisbn,nome_artigo,categoria,descricao,utilizador_user_name) 
VALUES (123345,987654321,'quadro','arte','abstrata','ines');
INSERT INTO artigo (id_artigo,codigoisbn,nome_artigo,categoria,descricao,utilizador_user_name) 
VALUES (132245,985674321,'carro','veiculo','carro','tapadinhas');
INSERT INTO artigo (id_artigo,codigoisbn,nome_artigo,categoria,descricao,utilizador_user_name) 
VALUES (125545,986574321,'moto','veiculo','motociclo','pedro');

INSERT INTO leilao (id_leilao,data_ini,data_fim,preco_base,preco_atual,is_ative,is_canceled,user_vencedor,artigo_id_artigo)
VALUES (134,'28-05-2021 12:06:12','15-06-2021 12:20:30',1500,1500,true,false,'',123345);
INSERT INTO leilao (id_leilao,data_ini,data_fim,preco_base,preco_atual,is_ative,is_canceled,user_vencedor,artigo_id_artigo)
VALUES (137,'01-06-2021 21:02:03','15-06-2021 14:12:02',1500,1500,true,false,'',132245);
INSERT INTO leilao (id_leilao,data_ini,data_fim,preco_base,preco_atual,is_ative,is_canceled,user_vencedor,artigo_id_artigo)
VALUES (140,'01-06-2021 20:02:02','15-07-2021 20:30:30',1500,1500,true,false,'',125545);


INSERT INTO comentarios(type,texto,data_pub,leilao_id_leilao,utilizador_user_name) VALUES ('comentario','queixa1','30-05-2021 12:02:03',134,'pedro');
INSERT INTO comentarios(type,texto,data_pub,leilao_id_leilao,utilizador_user_name) VALUES ('queixa','queixa2','29-05-2021 15:02:03 ',134,'ines');
INSERT INTO comentarios(type,texto,data_pub,leilao_id_leilao,utilizador_user_name) VALUES ('comentario','queixa3','29-05-2021 21:02:06',134,'tapadinhas');

INSERT INTO registolicitacao(preco_licitacao,data_licitacao,leilao_id_leilao,utilizador_user_name) VALUES (123,'30-05-2021 12:30:03',134,'pedro');
INSERT INTO registolicitacao(preco_licitacao,data_licitacao,leilao_id_leilao,utilizador_user_name) VALUES (156,'28-05-2021 06:02:15',134,'tapadinhas');
INSERT INTO registolicitacao(preco_licitacao,data_licitacao,leilao_id_leilao,utilizador_user_name) VALUES (196,'29-05-2021 19:19:19',134,'ines');
