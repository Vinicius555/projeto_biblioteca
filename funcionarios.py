from conexao import banco,curso,error


def createFunc(nome,cpf,email,fone,uf):
    try:
        curso.execute(F"INSERT INTO funcionarios VALUES(NULL,'{nome}',{cpf},'{email}',{fone},'{uf}')")
        banco.commit()
    except error as ex:
        print(ex)
    finally:
        print("Funcionario Cadastrado com Sucesso!")


def readfunc():
    try:
        curso.execute("SELECT * FROM funcionarios")
        read = curso.fetchall()
        return read
    except error as ex:
        print(ex)

def updateFunc(novo_nome,id):
    try:
        novo_nome = input("NOME:")
        curso.execute(f"UPDATE funcionarios SET Nome='{novo_nome}' WHERE id={id}")
        banco.commit()
    except error as ex:
        print(ex)
    finally:
        print("Dados Atualizados com Sucesso!")


def deleteFunc(id):
    try:
        id = input("ID:")
        curso.execute(f"DELETE FROM funcionarios WHERE ID={id}")
        banco.commit()
    except error as ex:
        print(ex)
    finally:
        print("Funcionario Deletado Com sucesso!")

