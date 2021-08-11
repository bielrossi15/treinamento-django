from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, status
from core.serializers import UserSerializer
from core.models import User
from rest_framework.response import Response


class UserViewSet(viewsets.ViewSet):
    serializer_class = UserSerializer

    def list(self, request):
        queryset = User.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response('Error', status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = self.serializer_class(user)
        return Response(serializer.data)

    def destroy(self, request, pk):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        user.delete()
        return Response('Usuario excluido com sucesso', status=status.HTTP_204_NO_CONTENT)





    

    


    

    

