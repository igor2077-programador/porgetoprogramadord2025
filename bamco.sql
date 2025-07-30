-- ddl linguagem de definiçao de dados
CREATE TABLE usuario(
    id INT PRIMARY KEY AUTO_INCREMENT not null,
    nome varchar(45),
    cpf varchar(14),
    email varchar(45),
    senha varchar(45)
);
alter TABLE usuario add idade INT;
alter TABLE usuario drop column idade;

--dml linguagem de manipulacao de dados
insert into usuario(nome,cpf,email,senha) values 
('joaquim','123.123.123-12','joaquim@gmail.com','123'),
('marlon','111.111.111-11','marlon@gmail.com','321');
('','','',''),

update usuario set nome="alice" where id=2;

select * from usuario;

select * from usuario where id between 1 and 3 order by nome 

--ddl linguagem de definiçao de dadosddl linguagem de definiçao de dados
CREATE TABLE regiao(
    id INT not null AUTO_INCREMENT,
    nome varchar(45)
);
--dml linguagem de manipulacao de dados
insert into regiao(nome)values
('noroeste'),
('sul'); 

CREATE TABLE cidade(
    id INT PRIMARY KEY not null AUTO_INCREMENT,
    nome varchar(45) not null ,
    cep varchar(14),
    estado char (2),
    id_regiao_fk INT ,
    foreign KEY ( id_regiao_fk ) references regiao(id)
);

insert into cidade (nome,cep,estado,id_regiao_fk)
('nova londrina','87970-000','pr'1),
('marilena','87960-000','pr'1),
('palmas','85555-000','pr'2);

select cidade.nome, regiao.nome 
from cidade inner join regiao
on cidade. id_regioan_fk = regiao.id;

CREATE TABLE ponto_focal(
    id INT PRIMARY KEY not null AUTO_INCREMENT,
    nome varchar(45),
    razao_social  varchar(45),
    tipo  varchar(45),
    cnpj_cpf  varchar(45),
    endereco  varchar(45),
    telefone  varchar(45),
    celular   varchar(45),
    email  varchar(45),
    id_cidade_fk INT, 
    foreign KEY (id_cidade_fk) references cidade (id)
)

insert into ponto_focal (nome,razao_social,tipo,cnpj_cpf,endereco,telefone,celular,email,id_cidade_fk) values
('feclopes','feclopes ltda','privada','12.345.111/0001-99','rua das flores,123','(44) 1234-5678','(44) 1234-5678','feclopes@gmail.com',1),
('assitencia social','assistencia ltda','publica','11.222.333/0001-01','av central,456','(44) 4002-8922','(44) 4002-8922','assitencia @gmail.com',2);

CREATE TABLE area (
    id INT PRIMARY KEY not null AUTO_INCREMENT,
    nome varchar(45) not null,
    numero INT
);

insert into area(nome,numero)values
('tecnologia',010101),
('gastronomia',123123),
('gestao',123499),

CREATE TABLE venda(
    id int PRIMARY KEY not null AUTO_INCREMENT,
    data data,
    origem varchar(255),
    obs varchar(255),
    id_area_fk int,
    id_ponto_focal_fk INT,
    foreign KEY (id_area_fk ) references ponto_focal(id),
    foreign KEY (id_ponto_focal_fk)  references area(id)
);

insert into venda(data,origen,obs , id_ponto_focal_fk,id_area_fk) values
('2025-07-30','instagran','conprdo',1,3),
('2027-07-28','evento','prefito',2,1);

select cidade.nome, area.nome 
from cidade 
inner join ponto_focal
on cidade.id = ponto_focal.id_cidade_fk
inner join venda 
on ponto_focal= venda.id_ponto_focal_fk
inner join area
on area.id_area_fk