from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from models.tarefaModels import Tarefa
from serializers.tarefaSerializer import TarefaSerializer

class TarefaListByAluno(APIView):
    def get(self, request, aluno_id):
        tarefas = Tarefa.objects.filter(aluno__id=aluno_id)
        serializer = TarefaSerializer(tarefas, many=True)
        return Response(serializer.data)