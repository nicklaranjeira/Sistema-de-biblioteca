import os
livros = {
        'ROMANCE': {},
        'TERROR' : {},
        'FANTASIA' : {}
}

pessoas = {}

def menu():
    while True:
        print("Escolha uma opção: ")
        cadastro(pessoas)
        if cadastro == 1:
            while True:
                print("Bem vindo a biblioteca online!")
                cadastro_usuario(pessoas)
                escolha_user = ("Escolha uma opção: \n1-Emprestar livro\n2-Devolver livro\n----->")
                if escolha_user == 1:
                    emprestar()
                if escolha_user == 2:
                    devolver()
        if cadastro == 2:
            while True:
                print("Bem vindo bibliotecário!")
                cadastro_bibliotecario(pessoas)
                escolha_bibliotecario = ("Escolha uma opção: \n1-Cadastrar livro \n2-Atualizar informações\n3-Vizualizar\n----->")
                if escolha_bibliotecario == 1:
                    cadastro_livro()
                if escolha_bibliotecario == 2:
                    atualizar()
                if escolha_bibliotecario == 3:
                    listar_livros()
        break

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
    
# --------------------------------------------------------------------------------

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

#---------------------------------------------------------------------------------

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

#---------------------------------------------------------------------------------

def cadastro_livro():
    titulo = input("Digite o titulo do livro: ")
    categorialivros = input("Digite a categoria do livro (ROMANCE TERROR FANTASIA): ").upper()
    if categorialivros in livros:
        livros[categorialivros][titulo] = {}
        print(f"Livro '{titulo}' cadastrado com sucesso na categoria {categorialivros}.")
    else:
        print("Categoria errada")
    pass

#---------------------------------------------------------------------------------

def emprestar():
    print("Emprestar:")
    print()
    print("Qual seu gênero de interesse?: \n1-Romance\n2-Terror\n3-Fantasia")
    emprestimo = int(input("------> "))
    if emprestimo == 1:
        #liros de romance
        pass
    if emprestimo == 2:
        #livros de Terror 
        pass
    if emprestimo == 3:
        #Livro de fantasia
        pass

#---------------------------------------------------------------------------------

def devolver():
    print ("--- Devolução de livros ----")
    escolha=int(input("Deseja devolver algum livro? \n 1. Sim \n 2. Não \n 0. Sair \n ->"))
    if escolha == 1:
        devolver=int(input("Informe o livro que deseja devolver \n ->"))



    elif escolha == 2:
        pass


    elif escolha == 0:
        print ("Saindo...")
        os.system ("pause")
        os.system ("cls")
        pass

    
    else:
        print ("Opção invalida, tente novamente")
        os.system ("pause")
        os.system ("cls")
        pass

#---------------------------------------------------------------------------------

def atualizar():
    categoria_antiga = input("Qual a categoria de agora do livro que você quer atualizar? (ROMANCE TERROR FANTASIA): ").upper()
    nome_antigo = input("Qual o nome atual do livro?: ")
    if categoria_antiga in livros and nome_antigo in livros[categoria_antiga]:
        print("Livro encontrado o que você quer atualizar?")
        print("1 - Mudar o nome do livro")
        print("2 - Mudar a categoria do livro")
        opcao = input("Digite sua opção: ")

        
    pass 

#---------------------------------------------------------------------------------

def listar_livros():
    pass