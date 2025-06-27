from models import Emprestimo

emprestimoBruno = Emprestimo(
    idUsuario = 1,
    idLivro = 2,
    dataEmprestimo = 1,
    dataDevolucao = 1 + 7,
    status = "ativo"
)

emprestimoAntonio = Emprestimo(
    idUsuario = 3,
    idLivro = 4,
    dataEmprestimo = 1,
    dataDevolucao = 1 + 10,
    status = "ativo"
)