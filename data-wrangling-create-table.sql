-- Exercise: 1
-- Data Wrangling - Task Creating table

create table conta_azul (
	id int,
	ano int,
	municipio_cod-ibge character varying(8),
	municipio_nome character varying(200),
	uf character varying(2),
	quantidade_acidentes_com_cat_tipicos int,
	quantidade_acidentes_com_cat_trajeto int,
	quantidade_acidentes_com_cat_doenca_profissional int,
	quantidade_obitos int,
	quantidade_acidentes_sem_cat int
);
