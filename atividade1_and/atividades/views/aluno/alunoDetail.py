from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from models.alunoModels import Aluno
from serializers.alunoSerializer import AlunoSerializer

class AlunoDetail(APIView):
    def get(self, request, pk):
        aluno = Aluno.objects.get(pk=pk)
        serializer = AlunoSerializer(aluno)
        return Response(serializer.data)

    def put(self, request, pk):
        aluno = Aluno.objects.get(pk=pk)
        serializer = AlunoSerializer(aluno, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        aluno = Aluno.objects.get(pk=pk)
        aluno.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)