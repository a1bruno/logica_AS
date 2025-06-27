from models import Livro, Usuario, Emprestimo #importando os dataclasses criados
diaAtualSistema = 1 #variável global que servirá de controle para verificar o funcionamento de empréstimos e multas

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
    tipo = str(input(f"O usuário é aluno ou professor? "))
    #criando um novo usuário com as propriedades que o usuário forneceu
    usuario = Usuario(
        id = id,
        nome = nome,
        tipo = tipo
    )
    #confirmando que o usuário foi criado
    print(f"\n Usuário {usuario.nome} registrado com sucesso!\n")
    return usuario

def realizarEmprestimo(listaUsuarios, listaLivros):
    if len(listaUsuarios) > 0 and len(listaLivros) > 0:
        idUsuario = int(input(f"Digite o ID do usuário: "))
        print("------------------")
        usuarioValido = False
        idLivro = int(input(f"Digite o código do livro para empréstimo: "))
        print("------------------")
        livroValido = False

        for i in range(len(listaUsuarios)):
            if listaUsuarios[i].id == idUsuario:
                usuarioValido = True
                usuario = listaUsuarios[i]
        for i in range(len(listaLivros)):
            if listaLivros[i].id == idLivro and listaLivros[i].qtdExemplares > 0:
                livroValido = True
                indexLivro = i
        if livroValido == False:
            print("O código do livro está incorreto ou não há mais exemplares disponíveis.")
            print("------------------")

        if usuarioValido == True and livroValido == True:
            emprestimo = Emprestimo(
                idUsuario = idUsuario,
                idLivro = idLivro,
                dataEmprestimo = diaAtualSistema,
                dataDevolucao = diaAtualSistema,
                status = "ativo"
            )
            if usuario.tipo == "aluno" or usuario.tipo == "Aluno":
                emprestimo.dataDevolucao = diaAtualSistema + 7
            elif usuario.tipo == "professor" or usuario.tipo == "Professor":
                emprestimo.dataDevolucao = diaAtualSistema + 10
            listaLivros[indexLivro].qtdExemplares -= 1
            print(f"Empréstimo realizado com sucesso:")
            print(f"Usuário do empréstimo: {usuario.nome};")
            print(f"Livro: {listaLivros[indexLivro].titulo};")
            print(f"Data de devolução prevista para dia {emprestimo.dataDevolucao}.")
            print("------------------")
            return emprestimo
    else:
        print("Não é possível realizar um empréstimo. Não existem livros e/ou usuários cadastrados em nosso sistema.")
        print("------------------")
        