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
	select max(id_noti) into noti_count from notificacao;
    msg := 'Nova mensagem no mural no leilão ' || new.leilao_id_leilao;

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
