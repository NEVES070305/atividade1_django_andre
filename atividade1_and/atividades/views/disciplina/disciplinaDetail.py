from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from atividades.models.disciplinaModels import Disciplina
from atividades.serializers.disciplinaSerializer import DisciplinaSerializer

class DisciplinaDetail(APIView):
    def get(self, request, pk):
        disciplina = Disciplina.objects.get(pk=pk)
        serializer = DisciplinaSerializer(disciplina)
        return Response(serializer.data)

    def put(self, request, pk):
        disciplina = Disciplina.objects.get(pk=pk)
        serializer = DisciplinaSerializer(disciplina, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        disciplina = Disciplina.objects.get(pk=pk)
        disciplina.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
