from models import Livro, Usuario, Emprestimo #importando os dataclasses criados

def menuGerenciarTempo(diaAtualSistema):
    while True:
        print("\n--- Gerenciar Tempo ---")
        print(f"Dia Atual do Sistema: {diaAtualSistema}")
        print("1. Avançar 1 dia")
        print("2. Avançar 7 dias (1 semana)")
        print("3. Avançar N dias")
        print("4. Consultar dia atual")
        print("5. Voltar ao Menu Principal")
        
        opcaoTempo = input("Escolha uma opção: ")
        print("------------------")

        if opcaoTempo == '1':
            diaAtualSistema += 1
            print(f"Sistema avançou para o dia: {diaAtualSistema}")
            print("------------------")
        elif opcaoTempo == '2':
            diaAtualSistema += 7
            print(f"Sistema avançou 7 dias. Novo dia: {diaAtualSistema}")
            print("------------------")
        elif opcaoTempo == '3':
            try:
                nDias = int(input("Quantos dias deseja avançar? "))
                if nDias > 0:
                    diaAtualSistema += nDias
                    print(f"Sistema avançou {nDias} dias. Novo dia: {diaAtualSistema}")
                    print("------------------")
                else:
                    print("Por favor, insira um número positivo de dias.")
                    print("------------------")
            except ValueError:
                print("Entrada inválida. Por favor, insira um número.")
                print("------------------")
        elif opcaoTempo == '4':
            print(f"O dia atual do sistema é: {diaAtualSistema}")
            print("------------------")
        elif opcaoTempo == '5':
            print("Retornando ao Menu Principal...")
            print("------------------")
            break # Sai do loop do menu_gerenciar_tempo
        else:
            print("Opção inválida. Tente novamente.")
            print("------------------")
    return diaAtualSistema # Retorna o dia atualizado

def listarLivrosCadastrados(listaLivros):
    print(f"Livros cadastrados: ")
    for i in range(len(listaLivros)):
        print(f"Título do livro: {listaLivros[i].titulo}")
        print(f"Código do livro: {listaLivros[i].id}")
        print(f"Autor: {listaLivros[i].autor}")
        print(f"Ano de publicação: {listaLivros[i].anoPublicacao}")
        print(f"Gênero: {listaLivros[i].genero}")
        print(f"Exemplares disponíveis: {listaLivros[i].qtdExemplares}")
        print("------------------")

def listarUsuarios(listaUsuarios):
    print(f"Lista de usuários: ")
    for i in range(len(listaUsuarios)):
        print(f"Nome: {listaUsuarios[i].nome}")
        print(f"ID: {listaUsuarios[i].id}")
        print(f"Tipo: {listaUsuarios[i].tipo}")
        print("------------------")

def buscarLivroPorId(listaLivros):
    livroEncontrado = False
    idLivro = int(input("Digite o código do livro que deseja buscar: "))
    for i in range(len(listaLivros)):
        if listaLivros[i].id == idLivro:
            livroEncontrado = True
            print(f"Título: {listaLivros[i].titulo}")
            print(f"ID: {listaLivros[i].id}")
            print(f"Autor: {listaLivros[i].autor}")
            print(f"Ano de publicação: {listaLivros[i].anoPublicacao}")
            print(f"Gênero: {listaLivros[i].genero}")
            print(f"Exemplares disponíveis: {listaLivros[i].qtdExemplares}")
            print("------------------")
    if livroEncontrado == False:
        print(f"Nào há nenhum livro com o ID {idLivro}.")
        print("------------------")


def cadastrarLivro():
    print(f"Iniciando cadastro de livro...")
    print("------------------")
    #solicitando ao usuário as informações do livro
    try:
        id = int(input(f"Digite o código para o livro: "))
        titulo = str(input(f"Título do livro: "))
        autor = str(input(f"Autor do livro: "))
        anoPublicacao = int(input(f"Ano de publicação do livro: "))
        genero = str(input(f"Gênero do livro: "))
        qtdExemplares = int(input("Digite a quantidade de exemplares disponíveis: "))
    except ValueError:
        print("Entrada de dados inválida.")
        print("------------------")
        return None
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
    #solicitando ao usuário as informações para 
    try:
        id = int(input(f"Digite o identificador do novo usuário: "))
        nome = str(input(f"Digite o nome do usuário: "))
        tipo = str(input(f"O usuário é aluno ou professor? "))
    except ValueError:
        print("Entrada de dados inválida.")
        print("------------------")
        return
    #criando um novo usuário com as propriedades que o usuário forneceu
    usuario = Usuario(
        id = id,
        nome = nome,
        tipo = tipo
    )
    #confirmando que o usuário foi criado
    print(f"\n Usuário {usuario.nome} registrado com sucesso!\n")
    return usuario

def realizarEmprestimo(listaUsuarios, listaLivros, listaEmprestimos, diaAtualSistema):
    if len(listaUsuarios) > 0 and len(listaLivros) > 0:
        usuarioValido = False
        try:
            idUsuario = int(input(f"Digite o ID do usuário: "))
            print("------------------")
        except ValueError:
            print("Entrada de dados inválida.")
            print("------------------")
            return
        for i in range(len(listaUsuarios)):
            if listaUsuarios[i].id == idUsuario:
                usuarioValido = True
                usuario = listaUsuarios[i]
        if usuarioValido == True:
            livroValido = False
            try:
                idLivro = int(input(f"Digite o código do livro para empréstimo: "))
                print("------------------")
            except ValueError:
                print("Entrada de dados inválida.")
                print("------------------")
                return
            for i in range(len(listaLivros)):
                if listaLivros[i].id == idLivro and listaLivros[i].qtdExemplares > 0:
                    livroValido = True
                    indexLivro = i
            if livroValido == False:
                print("O código do livro está incorreto ou não há mais exemplares disponíveis.")
                print("------------------")
        else:
            print(f"O ID está incorreto ou não há usuários para este ID.")
            print("------------------")

        if usuarioValido == True and livroValido == True:
            emprestimo = Emprestimo(
                idUsuario = idUsuario,
                idLivro = idLivro,
                dataEmprestimo = diaAtualSistema,
                dataDevolucao = diaAtualSistema,
                status = "ativo"
            )
            if usuario.tipo.lower() == "aluno":
                emprestimo.dataDevolucao = diaAtualSistema + 7
            elif usuario.tipo.lower() == "professor":
                emprestimo.dataDevolucao = diaAtualSistema + 10
            listaLivros[indexLivro].qtdExemplares -= 1
            listaEmprestimos.append(emprestimo)
            print(f"Empréstimo realizado com sucesso:")
            print(f"Usuário do empréstimo: {usuario.nome};")
            print(f"Livro: {listaLivros[indexLivro].titulo};")
            print(f"Data de devolução prevista para dia {emprestimo.dataDevolucao}.")
            print("------------------")
            return emprestimo
    else:
        print("Não é possível realizar um empréstimo. Não existem livros e/ou usuários cadastrados em nosso sistema.")
        print("------------------")
        
def devolverEmprestimo(listaEmprestimos, listaLivros, diaAtualSistema):
    emprestimoExistente = False
    livroCorreto = False
    idUsuario = int(input(f"Digite o id do usuário: "))
    print("------------------")
    for i in range(len(listaEmprestimos)):
        if listaEmprestimos[i].idUsuario == idUsuario:
            emprestimoExistente = True
            indexEmprestimo = i
            break
    if emprestimoExistente == True:
        idLivro = int(input(f"Digite o código do livro: "))
        print("------------------")
        for i in range(len(listaEmprestimos)):
            if listaEmprestimos[i].idLivro == idLivro:
                livroCorreto = True
                break
        if livroCorreto == True:
            dataDevolucaoEfetiva = diaAtualSistema
            for i in range(len(listaLivros)):
                if listaLivros[i].id == idLivro:
                    listaLivros[i].qtdExemplares += 1
                    break
            listaEmprestimos[indexEmprestimo].status = "devolvido"
            if dataDevolucaoEfetiva > listaEmprestimos[indexEmprestimo].dataDevolucao:
                valorMultaDia = 1.0
                diasEmAtraso = dataDevolucaoEfetiva - listaEmprestimos[indexEmprestimo].dataDevolucao
                multaUsuario = diasEmAtraso * valorMultaDia
                
                print(f"Devolução realizada com sucesso!")
                print("------------------")
                print(f"Entretanto, você passou {diasEmAtraso} dias do prazo de devolução.")
                print(f"Uma multa de R${multaUsuario} foi aplicada.")
                print("------------------")
            else:
                print(f"Devolução realizada com sucesso!")
                print("------------------")
            listaEmprestimos.pop(indexEmprestimo)

        else:
            print(f"Não existe um empréstimo/livro para este código.")
            print("------------------")
    else:
        print(f"Não existe um empréstimo para o ID fornecido.")
        print("------------------")

def listarEmprestimos(listaEmprestimos, listaUsuarios, listaLivros):
    if len(listaEmprestimos) > 0:
        print(f"Livros emprestados atualmente:")
        for i in range(len(listaEmprestimos)):
            idUsuario = listaEmprestimos[i].idUsuario
            idLivro = listaEmprestimos[i].idLivro
            dataDevolucaoPrevista = listaEmprestimos[i].dataDevolucao
            nomeUsuario = ""
            tituloLivro = ""
            for j in range(len(listaUsuarios)):
                if listaUsuarios[j].id == idUsuario:
                    nomeUsuario = listaUsuarios[j].nome
                    break
            for y in range(len(listaLivros)):
                if listaLivros[y].id == idLivro:
                    tituloLivro = listaLivros[y].titulo
                    break
            print(f"Usuário do empréstimo: {nomeUsuario}")
            print(f"Título emprestado: {tituloLivro}")
            print(f"Data de devolução prevista: dia {dataDevolucaoPrevista}")
            print("------------------")
    else:
        print(f"Não há empréstimos ativos.")
        print("------------------")

def listarEmprestimosAtrasados(listaEmprestimos, diaAtualSistema):
    livrosAtrasados = []
    if len(listaEmprestimos) > 0:
        for i in range(len(listaEmprestimos)):
            if listaEmprestimos[i].dataDevolucao < diaAtualSistema:
                livrosAtrasados.append(listaEmprestimos[i])
    if len(livrosAtrasados) > 0:
        print(f"Livros com empréstimo em atraso: ")
        for i in range(len(livrosAtrasados)):
            print(f"Livro com código: {livrosAtrasados[i].idLivro}")
            print(f"ID do responsável: {livrosAtrasados[i].idUsuario}")
            print(f"Data prevista para devolução: {livrosAtrasados[i].dataDevolucao} - Data atual: {diaAtualSistema}")
            print("------------------")
    else:
        print(f"Não há livros com empréstimo em atraso.")
        print("------------------")
