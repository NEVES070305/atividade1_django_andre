from django.db import models
from atividades.models.disciplinaModels import Disciplina
from atividades.models.alunoModels import Aluno

class Tarefa(models.Model):
    """
    Modelo para representar informações sobre tarefas.

    A classe Tarefa define os campos e métodos relacionados a tarefas.
    Cada tarefa possui um título, uma descrição, uma data de entrega, um estado
    de conclusão, um aluno associado e uma ou mais disciplinas associadas.

    Atributos:
    - titulo (CharField): O título da tarefa, com um comprimento máximo de 255 caracteres.
    - descricao (TextField): A descrição da tarefa, que pode ser um texto longo.
    - data_entrega (DateField): A data de entrega da tarefa.
    - concluida (BooleanField): Um campo booleano que indica se a tarefa está concluída (True) ou não (False).
    - aluno (ForeignKey para Aluno): Estabelece uma relação Many-to-One com o modelo Aluno, representando a associação da tarefa a um aluno específico.
    - disciplinas (ManyToManyField para Disciplina): Estabelece uma relação Many-to-Many com o modelo Disciplina, permitindo que a tarefa esteja associada a uma ou mais disciplinas.

    Métodos:
    - __str__(): Retorna uma representação em string do objeto Tarefa, usando seu título como representação.

    Exemplo de uso:
    >>> tarefa = Tarefa.objects.get(pk=1)
    >>> print(tarefa)
    'Título da Tarefa'
    """
    # Campo para armazenar o título da tarefa com um comprimento máximo de 255 caracteres.
    titulo = models.CharField(max_length=255)

    # Campo para armazenar a descrição da tarefa como um texto longo.
    descricao = models.TextField()

    # Campo para armazenar a data de entrega da tarefa.
    data_entrega = models.DateField()

    # Campo para armazenar o estado de conclusão da tarefa (True se estiver concluída, False caso contrário).
    concluida = models.BooleanField(default=False)

    # Relacionamento Many-to-One com Aluno: Uma tarefa pertence a um aluno.
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)

    # Relacionamento Many-to-Many com Disciplina: Uma tarefa pode estar associada a uma ou mais disciplinas.
    disciplinas = models.ManyToManyField(Disciplina)

    def __str__(self):
        """
        Retorna uma representação em string do objeto Tarefa.

        Exemplo de uso:
        >>> tarefa = Tarefa.objects.get(pk=1)
        >>> print(tarefa)
        'Título da Tarefa'
        """
        return self.titulo

    