from django.db import models

class Disciplina(models.Model):
    """
    Modelo para representar informações sobre disciplinas.

    A classe Disciplina define os campos e métodos relacionados a disciplinas.
    Cada disciplina tem um nome e uma descrição.

    Exemplo de uso:
    >>> disciplina = Disciplina.objects.get(pk=1)
    >>> print(disciplina)
    'Nome da Disciplina'
    """

    # Campo para armazenar o nome da disciplina com um comprimento máximo de 255 caracteres.
    nome = models.CharField(max_length=255)

    # Campo para armazenar a descrição da disciplina como um texto longo.
    descricao = models.TextField()

    def __str__(self):
        """
        Retorna uma representação em string do objeto Disciplina.

        Esta função é chamada quando você imprime um objeto Disciplina ou o exibe em
        administração do Django.

        Exemplo de uso:
        >>> disciplina = Disciplina.objects.get(pk=1)
        >>> print(disciplina)
        'Nome da Disciplina'
        """
        return self.nome
