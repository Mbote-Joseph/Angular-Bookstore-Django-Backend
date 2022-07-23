from django.shortcuts import render
from .models import Book
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import BookSerializer
# Create your views here.
@api_view(['GET'])
def getBook(request):
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
    return Response(status=400)

@api_view(['POST'])
def postBook(request):
    if request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    return Response(status=400)

@api_view(['PUT'])
def putBook(request, pk):
    if request.method == 'PUT':
        book = Book.objects.get(pk=pk)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    return Response(status=400)

@api_view(['DELETE'])
def deleteBook(request, pk):
    if request.method == 'DELETE':
        book = Book.objects.get(pk=pk)
        book.delete()
        return Response(status=204)
    return Response(status=400)