import sqlite3
from sqlite3 import Error

error = Error

banco = sqlite3.connect("blibioteca.db")

curso = banco.cursor()

curso.execute("CREATE TABLE IF NOT EXISTS funcionarios (ID INTEGER PRIMARY KEY AUTOINCREMENT,Nome VARCHAR(100),CPF VARCHAR(11) NOT NULL,Email VARCHAR(20) NOT NULL,Fone VARCHAR(20),UF VARCHAR(2) NOT NULL)")
curso.execute("CREATE TABLE IF NOT EXISTS livros (id INTEGER PRIMARY KEY AUTOINCREMENT,NomeLivro VARCHAR(100) NOT NULL,NomeAutor VARCHAR(100) NOT NULL)")
curso.execute("CREATE TABLE IF NOT EXISTS clientes (id INTEGER PRIMARY KEY AUTOINCREMENT,Nome VARCHAR(100) NOT NULL,CPF VARCHAR(11) NOT NULL,Fone VARCHAR(20))")
