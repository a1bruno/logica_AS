from functions import cadastrarLivro, cadastrarUsuario, realizarEmprestimo, devolverEmprestimo, listarEmprestimos, listarEmprestimosAtrasados, menuGerenciarTempo
from banco_base import users, books, rents
diaAtualSistema = 1
listaLivros = [books.sangueEGelo, books.oMorroDosVentosUivantes, books.asVantagensDeSerInvisivel, books.psicologiaFinanceira] #lista para armazenar os livros
listaUsuarios = [users.bruno, users.josefina, users.antonio, users.melissa] #lista para armazenar os usuários
listaEmprestimos = [rents.emprestimoBruno, rents.emprestimoAntonio] #lista para armazenar os emprestimos realizados

#implementação do laço de repetição que exibe o menu principal:
while True:
    print(f"1. Gerenciar livros")
    print(f"2. Gerenciar usuários")
    print(f"3. Realizar empréstimo")
    print(f"4. Realizar devolução")
    print(f"5. Relatórios")
    print(f"6. Gerenciar tempo (avançar/consultar dias)")
    print(f"7. Sair")
    

    escolhaUsuario = int(input(f"\nDigite a sua ação: "))
    print("------------------")

    match escolhaUsuario:
        case 1:
            while True:
                opcaoMenuLivros = int(input("1. Cadastrar novo livro\n2. Listar todos os livros\n3. Buscar livro\n4. Voltar para o menu principal\n"))
                match opcaoMenuLivros:
                    case 1:
                        livro = cadastrarLivro()
                        listaLivros.append(livro)
                    case 2:
                        if len(listaLivros) > 0:
                            print(f"Livros cadastrados:")
                            for i in range (len(listaLivros)):
                                print(f"Título: {listaLivros[i].titulo}")
                                print(f"ID: {listaLivros[i].id}")
                                print(f"Autor: {listaLivros[i].autor}")
                                print(f"Ano de publicação: {listaLivros[i].anoPublicacao}")
                                print(f"Gênero: {listaLivros[i].genero}")
                                print(f"Exemplares disponíveis: {listaLivros[i].qtdExemplares}")
                                print("------------------")
                    case 3:
                        idBusca = int(input(f"Digite o código do livro que deseja buscar: "))
                        print("------------------")
                        livroEncontrado = False
                        for i in range(len(listaLivros)):
                            if listaLivros[i].id == idBusca:
                                livroEncontrado = True
                                print(f"Título: {listaLivros[i].titulo}")
                                print(f"ID: {listaLivros[i].id}")
                                print(f"Autor: {listaLivros[i].autor}")
                                print(f"Ano de publicação: {listaLivros[i].anoPublicacao}")
                                print(f"Gênero: {listaLivros[i].genero}")
                                print(f"Exemplares disponíveis: {listaLivros[i].qtdExemplares}")
                                print("------------------")
                        if livroEncontrado == False:
                            print(f"Não há nenhum livro com o ID {idBusca}.")
                            print("------------------")
                    case 4:
                        print("Voltando para o menu principal...")
                        print("------------------")
                        break
                    case _:
                        print(f"Opção inválida. Tente outra vez.")
                        print("------------------")
        case 2:
            while True:
                opcaoMenuUsuarios = int(input(f"1. Cadastrar novo usuário\n2. Listar todos os usuários\n3. Voltar\n"))
                match opcaoMenuUsuarios:
                    case 1:
                        usuario = cadastrarUsuario()
                        listaUsuarios.append(usuario)
                    case 2:
                        if len(listaUsuarios) > 0:
                            print(f"Lista de usuários: ")
                            for i in range(len(listaUsuarios)):
                                print(f"Nome: {listaUsuarios[i].nome}")
                                print(f"ID: {listaUsuarios[i].id}")
                                print(f"Tipo: {listaUsuarios[i].tipo}")
                                print("------------------")
                        else:
                            print(f"A lista de usuários está vazia no momento.")
                            print("------------------")
                    case 3:
                        print(f"Voltando para o menu principal...")
                        print("------------------")
                        break
                    case _:
                        print(f"Opção inválida. Tente outra vez.")
                        print("------------------")
        case 3:
            novoEmprestimo = realizarEmprestimo(listaUsuarios, listaLivros, listaEmprestimos, diaAtualSistema)
        case 4:
            devolucao = devolverEmprestimo(listaEmprestimos, listaLivros, diaAtualSistema)
        case 5:
            while True:
                opcaoMenuEmprestimos = int(input("1. Listar livros com empréstimo ativo\n2. Listar livros com devolução em atraso\n3. Voltar\n"))
                match opcaoMenuEmprestimos:
                    case 1:
                        listarEmprestimos(listaEmprestimos, listaUsuarios, listaLivros)
                    case 2:
                        listarEmprestimosAtrasados(listaEmprestimos, diaAtualSistema)
                    case 3:
                        print(f"Voltando para o menu principal...")
                        break
                    case _:
                        print(f"Opção inválida. Tente novamente.")
        case 6: 
            diaAtualSistema = menuGerenciarTempo(diaAtualSistema)
        case 7:
            print("Saindo...")
            break
        case _:
            print("Opção inválida")