diaAtualSistema = 1 #variável global que servirá de controle para verificar o funcionamento de empréstimos e multas

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

    match escolhaUsuario:
        case 1:
            print("Em desenvolvimento")
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