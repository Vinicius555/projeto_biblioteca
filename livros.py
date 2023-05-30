from conexao import banco,curso,error


def createLivro(nomeLivro,nomeAutor):
    try:
        curso.execute(f"INSERT INTO livros VALUES(NULL,'{nomeLivro}','{nomeAutor}')")
        banco.commit()
    except error as ex:
        print(ex)
    finally:
        print("Livro adicionado com Sucesso!")

def readLivro():
    try:
        curso.execute("SELECT * FROM livros")
        read = curso.fetchall()
        return read
    except error as ex:
        print(ex)

def updateLivro(nomeLivro,id):
    try:
        nomeLivro = input("NOVO NOME DO LIVRO:")
        curso.execute(f"UPDATE livros SET NomeLivro='{nomeLivro}' WHERE id={id}")
        banco.commit()
    except error as ex:
        print(ex)
    finally:
        print("Nome do livro Atualizado com Sucesso!")


def deleteLivro(id):
    try:
        id = input("ID:")
        curso.execute(f"DELETE FROM livros WHERE id={id}")
        banco.commit()
    except error as ex:
        print(ex)
    finally:
        print("Livro Apagado com Sucesso!")