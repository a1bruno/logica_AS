from models import Livro, Usuario, Emprestimo
from functions import cadastrarLivro
diaAtualSistema = 1 #variável global que servirá de controle para verificar o funcionamento de empréstimos e multas
listaLivros = [] #lista para armazenar os livros
listaUsuarios = [] #lista para armazenar os usuários

#implementação do laço de repetição que exibe o menu principal:
while True:
    print(f"1. Gerenciar livros")
    print(f"2. Gerenciar usuários")
    print(f"3. Realizar empréstimo")
    print(f"4. Realizar devolução")
    print(f"5. Relatórios")
    print(f"6. Gerenciar tempo (avançar/consultar dias)")
    print(f"7. Sair")
    

    escolhaUsuario = int(input(f"Digite a sua ação: "))
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
                        print(f"Livros cadastrados:")
                        for i in range (len(listaLivros)):
                            print(f"ID: {listaLivros[i].id}")
                            print(f"Título: {listaLivros[i].titulo}")
                            print(f"Autor: {listaLivros[i].autor}")
                            print(f"Ano de publicação: {listaLivros[i].anoPublicacao}")
                            print(f"Gênero: {listaLivros[i].genero}")
                            print(f"Exemplares disponíveis: {listaLivros[i].qtdExemplares}")
                            print("------------------")
                    case 3:
                        idBusca = int(input(f"Digite o código do livro que deseja buscar: "))
                        for i in range(len(listaLivros)):
                            if listaLivros[i].id == idBusca:
                                print(f"ID: {listaLivros[i].id}")
                                print(f"Título: {listaLivros[i].titulo}")
                                print(f"Autor: {listaLivros[i].autor}")
                                print(f"Ano de publicação: {listaLivros[i].anoPublicacao}")
                                print(f"Gênero: {listaLivros[i].genero}")
                                print(f"Exemplares disponíveis: {listaLivros[i].qtdExemplares}")
                                print("------------------")
                    case 4:
                        print("Voltando para o menu principal...")
                        print("------------------")
                        break
                    case _:
                        print(f"Opção inválida. Tente outra vez.")
                        print("------------------")
        case 2:
            print("Em desenvolvimento")
        case 3:
            print("Em desenvolvimento")
        case 4:
            print("Em desenvolvimento")
        case 5:
            print("Em desenvolvimento")
        case 6: 
            print("Em desenvolvimento")
        case 7:
            print("Saindo...")
            break
        case _:
            print("Opção inválida")