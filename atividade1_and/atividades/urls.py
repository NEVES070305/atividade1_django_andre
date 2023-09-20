from django.urls import path
# from views.tarefa.tarefaList import TarefaList
# from .views.tarefa.tarefaDetail import TarefaDetail
# from .views.tarefa.tarefaListByAluno import TarefaListByAluno
# #from views.aluno import alunoList, alunoDetail
# #from views.disciplina import disciplinaList, disciplinaDetail
# from .views.aluno.alunoList import AlunoList
# from .views.aluno.alunoDetail import AlunoDetail
# from .views.disciplina.disciplinaList import DisciplinaList
# from .views.disciplina.disciplinaDetail import DisciplinaDetail
from atividades.views.aluno.alunoList import AlunoList
from atividades.views.aluno.alunoDetail import AlunoDetail
from atividades.views.disciplina.disciplinaList import DisciplinaList
from atividades.views.disciplina.disciplinaDetail import DisciplinaDetail
from atividades.views.tarefa.tarefaList import TarefaList
from atividades.views.tarefa.tarefaDetail import TarefaDetail
from atividades.views.tarefa.tarefaListByAluno import TarefaListByAluno


urlpatterns = [
    # path('alunos/', alunoList.AlunoList.as_view(), name='aluno-list-create'),
    # path('alunos/<int:pk>/', alunoDetail.AlunoDetail.as_view(), name='aluno-detail'),
    # path('disciplinas/', disciplinaList.DisciplinaList.as_view(), name='disciplina-list-create'),
    # path('disciplinas/<int:pk>/', disciplinaDetail.DisciplinaDetail.as_view(), name='disciplina-detail'),
    path('alunos/', AlunoList.as_view(), name='aluno-list'),
    path('alunos/<int:id>/', AlunoDetail.as_view(), name='aluno-detail'),
    path('disciplinas/', DisciplinaList.as_view(), name='disciplina-list'),
    path('disciplinas/<int:id>/', DisciplinaDetail.as_view(), name='disciplina-detail'),
    path('tarefas/', TarefaList.as_view(), name='tarefa-list'),
    path('tarefas/<int:id>/', TarefaDetail.as_view(), name='tarefa-detail'),
    path('alunos/<int:aluno_id>/tarefas/', TarefaListByAluno.as_view(), name='tarefa-list-by-aluno'),
]
