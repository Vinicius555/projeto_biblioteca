from conexao import curso,banco,error

def createClientes(nome,cpf,fone):
    try:
        curso.execute(f"INSERT INTO clientes VALUES (NULL,'{nome}',{cpf},{fone})")
        print("Usuário Criado com Sucesso!")
        banco.commit()
    except:
        print("Erro ao criar Usuário!")
        


def readTable():
    curso.execute("SELECT * FROM clientes")
    read = curso.fetchall()
    return read


def updateClientes(novo_nome,id):
    try:
      novo_nome = input("Nome:")
      curso.execute(f"UPDATE clientes SET Nome='{novo_nome}' WHERE id={id}")
      banco.commit()
    except error as ex:
        print(ex)
    finally:
        print("Informções atualizadasa com sucesso!")
    


def deleteClientes(id):
    try:
       id = input("ID:")
       curso.execute(f"DELETE FROM clientes WHERE id={id}")
    except error as ex:
        print(ex)
    finally:
        print("Usuário Deletado com Sucesso!")
    


