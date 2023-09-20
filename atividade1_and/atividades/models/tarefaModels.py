from django.db import models
from atividades.models.disciplinaModels import Disciplina
from atividades.models.alunoModels import Aluno

class Tarefa(models.Model):
    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    data_entrega = models.DateField()
    concluida = models.BooleanField(default=False)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    disciplinas = models.ManyToManyField(Disciplina)

    def __str__(self):
        return self.titulo
    