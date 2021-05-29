CREATE TABLE artigo (
	id_artigo		 INTEGER UNIQUE NOT NULL,
	codigoisbn		 INTEGER UNIQUE NOT NULL,
	nome_artigo		 VARCHAR(512) NOT NULL,
	categoria		 VARCHAR(512),
	descricao		 VARCHAR(512) NOT NULL,
	user_vencedor	 VARCHAR(512) DEFAULT null,
	utilizador_user_name VARCHAR(512) NOT NULL,
	PRIMARY KEY(id_artigo)
);

CREATE TABLE registolicitacao (
	id_leilao		 INTEGER UNIQUE NOT NULL,
	preco_licitacao	 BIGINT UNIQUE NOT NULL,
	data_licitacao	 TIMESTAMP NOT NULL,
	leilao_id_leilao	 INTEGER,
	utilizador_user_name VARCHAR(512),
	PRIMARY KEY(leilao_id_leilao,utilizador_user_name)
);

CREATE TABLE comentarios (
	id_leilao		 INTEGER UNIQUE NOT NULL,
	texto		 VARCHAR(512) NOT NULL,
	data_pub		 TIMESTAMP NOT NULL,
	leilao_id_leilao	 INTEGER,
	utilizador_user_name VARCHAR(512),
	PRIMARY KEY(leilao_id_leilao,utilizador_user_name)
);

CREATE TABLE utilizador (
	user_name VARCHAR(512) UNIQUE NOT NULL,
	email	 VARCHAR(512) UNIQUE NOT NULL,
	nome	 VARCHAR(512) NOT NULL,
	password	 VARCHAR(512) NOT NULL,
	genero	 VARCHAR(512) DEFAULT null,
	nif	 BIGINT UNIQUE NOT NULL,
	data_nasc DATE NOT NULL,
	estado	 VARCHAR(512),
	contacto	 BIGINT UNIQUE NOT NULL,
	is_ban	 BOOL NOT NULL DEFAULT false,
	is_admin	 BOOL NOT NULL,
	PRIMARY KEY(user_name)
);

CREATE TABLE leilao (
	id_leilao	 INTEGER UNIQUE NOT NULL,
	data_ini	 TIMESTAMP NOT NULL,
	data_fim	 TIMESTAMP NOT NULL,
	preco_base	 BIGINT NOT NULL,
	is_ativo	 BOOL NOT NULL,
	artigo_id_artigo INTEGER NOT NULL,
	PRIMARY KEY(id_leilao)
);

CREATE TABLE notificacao (
	id_noti		 INTEGER UNIQUE NOT NULL,
	msg			 VARCHAR(512) NOT NULL,
	data		 TIMESTAMP NOT NULL,
	is_open		 BOOL NOT NULL DEFAULT false,
	utilizador_user_name VARCHAR(512) NOT NULL,
	PRIMARY KEY(id_noti)
);

CREATE TABLE updateartigo (
	id_leilao	 INTEGER NOT NULL,
	descricao	 VARCHAR(512) NOT NULL,
	artigo_id_artigo INTEGER,
	PRIMARY KEY(artigo_id_artigo)
);

ALTER TABLE artigo ADD CONSTRAINT artigo_fk1 FOREIGN KEY (utilizador_user_name) REFERENCES utilizador(user_name);
ALTER TABLE registolicitacao ADD CONSTRAINT registolicitacao_fk1 FOREIGN KEY (leilao_id_leilao) REFERENCES leilao(id_leilao);
ALTER TABLE registolicitacao ADD CONSTRAINT registolicitacao_fk2 FOREIGN KEY (utilizador_user_name) REFERENCES utilizador(user_name);
ALTER TABLE comentarios ADD CONSTRAINT comentarios_fk1 FOREIGN KEY (leilao_id_leilao) REFERENCES leilao(id_leilao);
ALTER TABLE comentarios ADD CONSTRAINT comentarios_fk2 FOREIGN KEY (utilizador_user_name) REFERENCES utilizador(user_name);
ALTER TABLE leilao ADD CONSTRAINT leilao_fk1 FOREIGN KEY (artigo_id_artigo) REFERENCES artigo(id_artigo);
ALTER TABLE notificacao ADD CONSTRAINT notificacao_fk1 FOREIGN KEY (utilizador_user_name) REFERENCES utilizador(user_name);
ALTER TABLE updateartigo ADD CONSTRAINT updateartigo_fk1 FOREIGN KEY (artigo_id_artigo) REFERENCES artigo(id_artigo);

