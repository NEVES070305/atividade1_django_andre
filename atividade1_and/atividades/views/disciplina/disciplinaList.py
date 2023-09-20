from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from models.disciplinaModels import Disciplina
from serializers.disciplinaSerializer import DisciplinaSerializer

class DisciplinaList(APIView):
    def get(self, request):
        disciplinas = Disciplina.objects.all()
        serializer = DisciplinaSerializer(disciplinas, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DisciplinaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)