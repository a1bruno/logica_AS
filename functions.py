from models import Livro, Usuario, Emprestimo #importando os dataclasses criados

def cadastrarLivro():
    print(f"Iniciando cadastro de livro...")
    print("------------------")
    #solicitando ao usuário as informações do livro
    id = int(input(f"Digite o código para o livro: "))
    titulo = str(input(f"Título do livro: "))
    autor = str(input(f"Autor do livro: "))
    anoPublicacao = int(input(f"Ano de publicação do livro: "))
    genero = str(input(f"Gênero do livro: "))
    qtdExemplares = int(input("Digite a quantidade de exemplares disponíveis: "))
    #criando um novo livro com as propriedades que o usuário forneceu
    livro = Livro(
        id = id,
        titulo = titulo,
        autor = autor,
        anoPublicacao = anoPublicacao,
        genero = genero,
        qtdExemplares = qtdExemplares
    )
    #mostrando ao usuário o livro que foi criado
    print(f'\nO livro "{livro.titulo}" foi cadastrado com sucesso.\n')
    print("------------------")
    return livro

def cadastrarUsuario():
    print(f"Iniciando cadastro de usuário...")
    print("------------------")
    #solicitando ao usuário as informações para registro
    id = int(input(f"Digite o identificador do novo usuário: "))
    nome = str(input(f"Digite o nome do usuário: "))
    tipo = str(input(f"O usuário é aluno ou professor?"))
    #criando um novo usuário com as propriedades que o usuário forneceu
    usuario = Usuario(
        id = id,
        nome = nome,
        tipo = tipo
    )
    #confirmando que o usuário foi criado
    print(f"\n{usuario.nome} registrado com sucesso!\n")
    return usuario


