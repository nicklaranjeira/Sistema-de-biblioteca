import os
livros = {
        'ROMANCE': {},
        'TERROR' : {},
        'FANTASIA' : {}
}

def cadastro(pessoas):
    os.system("cls")
    print("-- TELA DE CADASTRO --\n")
    escolha = int(input(" Você deseja se cadastrar como:\n1 - Usuário\n2 - Bibliotecário\n--> "))

    if escolha == 1:
        return cadastro_usuario(pessoas)
    elif escolha == 2:
        return cadastro_bibliotecario(pessoas)
    else:
        print(" Opção inválida!")
        input("Pressione ENTER para continuar...")
        return None

def cadastro_usuario(pessoas):
    os.system("cls")
    print("-- CADASTRO DE USUÁRIO --")
    nome = input("Informe o seu nome completo: ")
    email = input("Informe o seu email: ")
    
    user_id = len(pessoas) + 1
    pessoas[user_id] = {"tipo": "usuario", "nome": nome, "email": email}

    print(f"\n Bem-vindo {nome}, você foi cadastrado como USUÁRIO com id: {user_id}")
    input("\nPressione ENTER para continuar...")
    return {"id": user_id, "tipo": "usuario", "nome": nome, "email": email}


def cadastro_bibliotecario(pessoas):
    os.system("cls")
    print("-- CADASTRO DE BIBLIOTECÁRIO --")
    nome = input("Informe o seu nome completo: ")
    email = input("Informe o seu email: ")
    unidade = input("Informe sua unidadea: ")
    senha = input("Crie uma senha de acesso: ")
    
    user_id = len(pessoas) + 1
    pessoas[user_id] = {
        "tipo": "bibliotecario",
        "nome": nome,
        "email": email,
        "unidade": unidade,
        "senha": senha
    }

    print(f"\n Bem-vindo {nome}, você foi cadastrado como BIBLIOTECÁRIO com id: {user_id}")
    input("\nPressione ENTER para continuar...")
    return {"id": user_id, "tipo": "bibliotecario", "nome": nome, "email": email}

def cadastro_livro():
    titulo = input("Digite o titulo do livro: ")
    categorialivros = input("Digite a categoria do livro (ROMANCE TERROR FANTASIA): ").upper()
    if categorialivros in livros:
        livros[categorialivros][titulo] = {}
        print(f"Livro '{titulo}' cadastrado com sucesso na categoria {categorialivros}.")
    else:
        print("Categoria errada")
    pass

def emprestar():
    print("Emprestar:")
    print()
    print("Qual seu genêro de interesse?:")
    print("")

def devolver():
    pass

def atualizar():
    pass 

def listar_livros():
    pass