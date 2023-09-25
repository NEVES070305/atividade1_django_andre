# atividade1_django_andre

Esta é uma API para gerenciar informações de estudantes, disciplinas e tarefas.


A API oferece os seguintes endpoints:

- `/alunos/`: Lista todos os estudantes e permite criar um novo estudante.
- `/alunos/<int:id>/`: Obtém detalhes de um estudante específico, atualiza ou exclui o estudante.
- `/disciplinas/`: Lista todas as disciplinas e permite criar uma nova disciplina.
- `/disciplinas/<int:id>/`: Obtém detalhes de uma disciplina específica, atualiza ou exclui a disciplina.
- `/tarefas/`: Lista todas as tarefas e permite criar uma nova tarefa.
- `/tarefas/<int:id>/`: Obtém detalhes de uma tarefa específica, atualiza ou exclui a tarefa.
- `alunos/<int:aluno_id>/tarefas/`: Obtém lista de tarefas de um aluno.

## Uso

Para usar esta API, você pode fazer solicitações HTTP para os endpoints correspondentes usando o arquivo JSON PostmanUrls utilizando do Postman.

## Instalação

1. Clone este repositório;
2. Configure seu ambiente Python (.env);
3. Instale as dependências com `pip install -r requirements.txt`;
4. Faça o arquivo com o comando `python manage.py makemigrations`;
5. Execute as migrações do banco de dados com `python manage.py migrate`;
6. Inicie o servidor de desenvolvimento com `python manage.py runserver`.
