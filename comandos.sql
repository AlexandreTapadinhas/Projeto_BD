INSERT INTO utilizador (user_name, email,nome, password, genero, nif, data_nasc, estado, contacto, is_ban, is_admin) 
VALUES ('pedro','pedro@gmail.com','pedro tavares','password','masculino',245789632,'01-01-2000','solteiro',987654321,false,false);
INSERT INTO utilizador (user_name, email,nome, password, genero, nif, data_nasc, estado, contacto, is_ban, is_admin) 
VALUES ('tapadinhas','tapadinhas@gmail.com','rui tapadinhas','password','masculino',2478912632,'01-01-2000','solteiro',98521421,false,false);
INSERT INTO utilizador (user_name, email,nome, password, genero, nif, data_nasc, estado, contacto, is_ban, is_admin) 
VALUES ('ines','inestex@gmail.com','ines teixeira','password','feminino',2478974832,'01-01-2000','solteiro',987211125,false,false);
INSERT INTO utilizador (user_name, email,nome, password, genero, nif, data_nasc, estado, contacto, is_ban, is_admin) 
VALUES ('maria','maria@gmail.com','Maria Silva','password','feminino',245789611,'03-05-2000','solteiro',987654322,false,false);
INSERT INTO utilizador (user_name, email,nome, password, genero, nif, data_nasc, estado, contacto, is_ban, is_admin) 
VALUES ('sofia','sofia@gmail.com','sofia matos','password','feminia',2478912611,'27-11-2000','solteiro',95741421,false,false);
INSERT INTO utilizador (user_name, email,nome, password, genero, nif, data_nasc, estado, contacto, is_ban, is_admin) 
VALUES ('fernando','fernando@gmail.com','fernando cardoso','password','masculino',247897481,'01-01-2000','solteiro',917211125,false,false);
INSERT INTO utilizador (user_name, email,nome, password, genero, nif, data_nasc, estado, contacto, is_ban, is_admin) 
VALUES ('joao','joao@gmail.com','joao amaral','password','masculino',245719632,'01-08-2001','solteiro',917654321,false,false);
INSERT INTO utilizador (user_name, email,nome, password, genero, nif, data_nasc, estado, contacto, is_ban, is_admin) 
VALUES ('beatriz','beatriz@gmail.com','beatriz dias','password','femino',2778912632,'12-11-1994','solteiro',98521321,false,false);
INSERT INTO utilizador (user_name, email,nome, password, genero, nif, data_nasc, estado, contacto, is_ban, is_admin) 
VALUES ('rita','rita@gmail.com','rita curado','password','feminino',2478974132,'03-05-2001','solteiro',987212125,false,false);
INSERT INTO utilizador (user_name, email,nome, password, genero, nif, data_nasc, estado, contacto, is_ban, is_admin) 
VALUES ('rui','rui@gmail.com','rui silva','password','masculino',275789632,'01-01-2000','solteiro',987654381,false,false);
INSERT INTO utilizador (user_name, email,nome, password, genero, nif, data_nasc, estado, contacto, is_ban, is_admin) 
VALUES ('teresa','teresa@gmail.com','teresa teixeira','password','feminino',2478910632,'01-01-2000','solteiro',99521421,false,false);
INSERT INTO utilizador (user_name, email,nome, password, genero, nif, data_nasc, estado, contacto, is_ban, is_admin) 
VALUES ('diogo','diogo@gmail.com','diogo silva','password','masculino',2478904832,'05-05-2000','solteiro',987222225,false,false);
INSERT INTO utilizador (user_name, email,nome, password, genero, nif, data_nasc, estado, contacto, is_ban, is_admin) 
VALUES ('joana','joana@gmail.com','joana bertencourt','password','masculino',245729630,'06-12-2000','solteiro',907674321,false,false);
INSERT INTO utilizador (user_name, email,nome, password, genero, nif, data_nasc, estado, contacto, is_ban, is_admin) 
VALUES ('gustavo','gustavo@gmail.com','gustavo catalao','password','masculino',2478912032,'01-01-2000','solteiro',90521421,false,false);
INSERT INTO utilizador (user_name, email,nome, password, genero, nif, data_nasc, estado, contacto, is_ban, is_admin) 
VALUES ('goncalo','goncalo@gmail.com','goncalo mendes','password','feminino',2478974802,'01-01-2000','solteiro',907211125,false,false);

INSERT INTO artigo (id_artigo,codigoisbn,nome_artigo,categoria,descricao,utilizador_user_name) 
VALUES (123345,987654321,'quadro','arte','abstrata','ines');
INSERT INTO artigo (id_artigo,codigoisbn,nome_artigo,categoria,descricao,utilizador_user_name) 
VALUES (132245,985674321,'carro','veiculo','carro','tapadinhas');
INSERT INTO artigo (id_artigo,codigoisbn,nome_artigo,categoria,descricao,utilizador_user_name) 
VALUES (125545,986574321,'moto','veiculo','motociclo','pedro');
INSERT INTO artigo (id_artigo,codigoisbn,nome_artigo,categoria,descricao,utilizador_user_name) 
VALUES (123346,987654326,'quadro','arte','abstrata','ines');
INSERT INTO artigo (id_artigo,codigoisbn,nome_artigo,categoria,descricao,utilizador_user_name) 
VALUES (132246,985674326,'carro','veiculo','carro','tapadinhas');
INSERT INTO artigo (id_artigo,codigoisbn,nome_artigo,categoria,descricao,utilizador_user_name) 
VALUES (125546,986574326,'moto','veiculo','motociclo','pedro');
INSERT INTO artigo (id_artigo,codigoisbn,nome_artigo,categoria,descricao,utilizador_user_name) 
VALUES (1234,787654326,'quadro','arte','abstrata','ines');
INSERT INTO artigo (id_artigo,codigoisbn,nome_artigo,categoria,descricao,utilizador_user_name) 
VALUES (12347,785674326,'carro','veiculo','carro','tapadinhas');
INSERT INTO artigo (id_artigo,codigoisbn,nome_artigo,categoria,descricao,utilizador_user_name) 
VALUES (1123,786574326,'moto','veiculo','motociclo','pedro');
INSERT INTO artigo (id_artigo,codigoisbn,nome_artigo,categoria,descricao,utilizador_user_name) 
VALUES (7,852,'artigo_fim','terminado','atrigo para leilao terminado','pedro');

INSERT INTO leilao (id_leilao,data_ini,data_fim,preco_base,preco_atual,is_ativo,is_canceled,user_vencedor,artigo_id_artigo)
VALUES (123,'28-05-2021 21:30:12','02-06-2021 14:12:03',1500,1500,true,false,'',123345);
INSERT INTO leilao (id_leilao,data_ini,data_fim,preco_base,preco_atual,is_ativo,is_canceled,user_vencedor,artigo_id_artigo)
VALUES (12,'01-06-2021 23:03:02','15-06-2021 15:03:08',1500,1500,true,false,'',132245);
INSERT INTO leilao (id_leilao,data_ini,data_fim,preco_base,preco_atual,is_ativo,is_canceled,user_vencedor,artigo_id_artigo)
VALUES (1,'30-06-2021 20:02:02','15-07-2021 20:30:30',1500,1500,true,false,'',125545);
INSERT INTO leilao (id_leilao,data_ini,data_fim,preco_base,preco_atual,is_ativo,is_canceled,user_vencedor,artigo_id_artigo)
VALUES (2,'30-06-2021 20:02:02','30-06-2021 20:30:30',20,1500,true,false,'ines',7);
INSERT INTO leilao (id_leilao,data_ini,data_fim,preco_base,preco_atual,is_ativo,is_canceled,user_vencedor,artigo_id_artigo)
VALUES (4,'30-05-2021 20:02:02','30-05-2021 20:30:30',20,1500,true,false,'ines',7);
INSERT INTO leilao (id_leilao,data_ini,data_fim,preco_base,preco_atual,is_ativo,is_canceled,user_vencedor,artigo_id_artigo)
VALUES (124,'28-05-2021 21:30:12','02-06-2021 14:12:03',1600,1600,true,false,'',1234);
INSERT INTO leilao (id_leilao,data_ini,data_fim,preco_base,preco_atual,is_ativo,is_canceled,user_vencedor,artigo_id_artigo)
VALUES (11,'01-06-2021 23:03:02','15-06-2021 15:03:08',1500,1500,true,false,'',12347);
INSERT INTO leilao (id_leilao,data_ini,data_fim,preco_base,preco_atual,is_ativo,is_canceled,user_vencedor,artigo_id_artigo)
VALUES (5,'30-06-2021 20:02:02','15-07-2021 20:30:30',1500,1500,true,false,'',1123);
INSERT INTO leilao (id_leilao,data_ini,data_fim,preco_base,preco_atual,is_ativo,is_canceled,user_vencedor,artigo_id_artigo)
VALUES (7,'30-06-2021 20:02:02','30-06-2021 20:30:30',20,1500,true,false,'ines',123346);
INSERT INTO leilao (id_leilao,data_ini,data_fim,preco_base,preco_atual,is_ativo,is_canceled,user_vencedor,artigo_id_artigo)
VALUES (9,'30-05-2021 20:02:02','30-05-2021 20:30:30',20,1500,true,false,'ines',125545);


INSERT INTO comentarios(type,texto,data_pub,leilao_id_leilao,utilizador_user_name) VALUES ('comentario','queixa1','30-05-2021 12:02:03',123,'pedro');
INSERT INTO comentarios(type,texto,data_pub,leilao_id_leilao,utilizador_user_name) VALUES ('queixa','queixa2','29-05-2021 15:02:03 ',123,'ines');
INSERT INTO comentarios(type,texto,data_pub,leilao_id_leilao,utilizador_user_name) VALUES ('comentario','queixa3','29-05-2021 21:02:06',123,'tapadinhas');

INSERT INTO registolicitacao(preco_licitacao,data_licitacao,leilao_id_leilao,utilizador_user_name) VALUES (123,'30-05-2021 12:30:03',123,'pedro');
INSERT INTO registolicitacao(preco_licitacao,data_licitacao,leilao_id_leilao,utilizador_user_name) VALUES (156,'28-05-2021 06:02:15',123,'tapadinhas');
INSERT INTO registolicitacao(preco_licitacao,data_licitacao,leilao_id_leilao,utilizador_user_name) VALUES (196,'29-05-2021 19:19:19',123,'ines');

INSERT INTO notificacao(id_noti, msg,data,is_open,utilizador_user_name) VALUES (0, 'init notificacao','29-05-2000 21:02:06',FALSE,'tapadinhas');

/*notificacao de licitacao ultrapassada*/
DROP trigger if exists avisolicitacao on registolicitacao;
DROP function if exists novalicitacao cascade;

CREATE function novalicitacao() returns trigger
language plpgsql
AS $$
DECLARE
	noti_count numeric;
    msg varchar;
	c1 cursor for
		select data_licitacao
		from registolicitacao
        where registolicitacao.leilao_id_leilao = new.leilao_id_leilao 
		and new.preco_licitacao > registolicitacao.preco_licitacao;
		
BEGIN
	noti_count := 0;
	select max(id_noti) into noti_count from notificacao;
    msg := 'nova licitacao no leilao' || new.leilao_id_leilao;
	for r in c1
	loop
        noti_count :=  noti_count + 1;
        insert into notificacao(id_noti,msg,data,is_open,utilizador_user_name)
		values(noti_count,msg,r.data_licitacao,false,new.utilizador_user_name); 
	end loop;
	return new;
end;
$$;

create trigger avisolicitacao
after insert or update or delete on registolicitacao
for each row
execute procedure novalicitacao();

/*notificacao de novo comentario*/
DROP trigger if exists aviso_comentario on comentarios;
DROP function if exists noti_novo_comentario cascade;


CREATE function noti_novo_comentario() returns trigger
language plpgsql
AS $$
DECLARE
	noti_count numeric;
    msg varchar;
	
	c1 cursor for
		select utilizador_user_name, data_pub
		from comentarios
        where comentarios.leilao_id_leilao = new.leilao_id_leilao 
		    and comentarios.utilizador_user_name != new.utilizador_user_name;
		
BEGIN
	noti_count := 0;
	select max(id_noti) into noti_count from notificacao;
    msg := 'Nova mensagem no mural do leilão ' || new.leilao_id_leilao;

	for r in c1
	loop
        noti_count := noti_count + 1;
        insert into notificacao(id_noti, msg, data, is_open, utilizador_user_name)
		values(noti_count, msg, r.data_pub, false, new.utilizador_user_name);
	end loop;
	return new;
end;
$$;

create trigger aviso_comentario
after insert on comentarios
for each row
execute procedure noti_novo_comentario();
