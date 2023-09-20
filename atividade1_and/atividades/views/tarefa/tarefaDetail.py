from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from models.tarefaModels import Tarefa
from serializers.tarefaSerializer import TarefaSerializer

class TarefaDetail(APIView):
    def get(self, request, pk):
        tarefa = Tarefa.objects.get(pk=pk)
        serializer = TarefaSerializer(tarefa)
        return Response(serializer.data)

    def put(self, request, pk):
        tarefa = Tarefa.objects.get(pk=pk)
        serializer = TarefaSerializer(tarefa, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        tarefa = Tarefa.objects.get(pk=pk)
        tarefa.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)