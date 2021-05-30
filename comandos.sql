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
VALUES (134,'01-06-2021','15-06-2021',1500,1500,true,false,'',123345);
INSERT INTO leilao (id_leilao,data_ini,data_fim,preco_base,preco_atual,is_ative,is_canceled,user_vencedor,artigo_id_artigo)
VALUES (137,'01-06-2021','15-06-2021',1500,1500,true,false,'',132245);
INSERT INTO leilao (id_leilao,data_ini,data_fim,preco_base,preco_atual,is_ative,is_canceled,user_vencedor,artigo_id_artigo)
VALUES (140,'01-06-2021','15-06-2021',1500,1500,true,false,'',125545);


INSERT INTO comentarios(type,texto,data_pub,leilao_id_leilao,utilizador_user_name) VALUES ('comentario','123','01-01-2000',1236,'pedro');
INSERT INTO comentarios(type,texto,data_pub,leilao_id_leilao,utilizador_user_name) VALUES ('queixa','456','01-01-2000',1236,'ines');
INSERT INTO comentarios(type,texto,data_pub,leilao_id_leilao,utilizador_user_name) VALUES ('comentario','789','01-01-2000',1236,'tapadinhas');

INSERT INTO registolicitacao(preco_licitacao,data_licitacao,leilao_id_leilao,utilizador_user_name) VALUES (2500,'01-01-2000',1236,'pedro');
INSERT INTO registolicitacao(preco_licitacao,data_licitacao,leilao_id_leilao,utilizador_user_name) VALUES (2600,'02-01-2000',1236,'tapadinhas');
INSERT INTO registolicitacao(preco_licitacao,data_licitacao,leilao_id_leilao,utilizador_user_name) VALUES (2800,'03-01-2000',1236,'ines');