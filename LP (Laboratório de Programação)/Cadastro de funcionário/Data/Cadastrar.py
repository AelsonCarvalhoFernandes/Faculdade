import sqlite3

class Cadastrar:
    def __init__(self):
        self.caminho = "\Projetos\Python\database.db"
        self.con = sqlite3.connect(self.caminho)
        self.cur = self.con.cursor()
        self.cur.execute('''
            create table if not exists Pessoas(
                nome varchar(30) not null,
                matricula varchar(30) not null,
                idade int not null,
                ano_de_ingresso varchar(10) not null,
                salario number not null,
                constraint pk_matricula primary key(matricula)
            )
        ''')
        self.cur.execute('''
            create table if not exists Cursos(
                id int auto_increment
                matricula varchar(30),
                nome varchar(30) not null,
                importancia varchar(1) not null check(importancia in('1', '2', '3')),
                ano_de_conclusao varchar(10) not null,
                constraint pk_idc primary key(id)
                constraint fk_matricula foreign key(matricula) references Pessoas(matricula)
            )
        ''')
    def cadastrarC(self, matricula, nome, importancia, ano):

        self.cur.execute(
            f'''
            insert into Cursos (matricula, nome, importancia, ano_de_conclusao)
            values('{matricula}', '{nome}', '{importancia}', '{ano}')
            '''
        )
        self.con.commit()

    def cadastrarP(self, nome, matricula, idade, ano, salario):
        try:
            self.cur.execute(
                f'''
                insert into Pessoas (nome, matricula, idade, ano_de_ingresso, salario)
                values('{nome}', '{matricula}', {idade}, '{ano}', {salario})
                '''
            )
            self.con.commit()
        except:
            print('Valor incorreto ou ja existente')
        
