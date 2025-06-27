from models import Emprestimo
from functions import diaAtualSistema

emprestimoBruno = Emprestimo(
    idUsuario = 1,
    idLivro = 2,
    dataEmprestimo = diaAtualSistema,
    dataDevolucao = diaAtualSistema + 7,
    status = "ativo"
)

emprestimoAntonio = Emprestimo(
    idUsuario = 3,
    idLivro = 4,
    dataEmprestimo = diaAtualSistema,
    dataDevolucao = diaAtualSistema + 10,
    status = "ativo"
)