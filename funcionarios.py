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


