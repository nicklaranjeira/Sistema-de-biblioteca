livros = {
        'ROMANCE': {},
        'TERROR' : {},
        'FANTASIA' : {}
}

def cadastro_user():
    pass

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
    pass

def devolver():
    pass

def atualizar():
    pass 

def listar_livros():
    pass