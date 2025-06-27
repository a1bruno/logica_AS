from dataclasses import dataclass

@dataclass
class Livro:
    id: int #código do livro
    titulo: str #título do livro
    autor: str #autor do livro
    anoPublicacao: int #ano de publicação
    genero: str #gênero do livro
    qtdExemplares: int #quantidade de exemplares disponíveis

@dataclass
class Usuario:
    id: int #identificador do usuário
    nome: str #nome do usuário
    tipo: str #tipo do usuário: professor ou aluno

@dataclass
class Emprestimo:
    idUsuario: int #registra o id do usuário para o empréstimo
    idLivro: int #define o livro que o usuário escolheu baseado no código do livro
    dataEmprestimo: int #define a data que foi realizado o empréstimo
    dataDevolucao: int
    status: str