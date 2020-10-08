from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer
from rest_framework import status


@api_view(['GET'])
def psot_list(request):
    if request.method == 'GET':
        obj = Post.object.all()
        serializer = PostSerializer(obj, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if seriazlier.is_valid():
            serializer.save()
            return Response(seriazlier.data, status=status.HTTP_201_CREATED)
