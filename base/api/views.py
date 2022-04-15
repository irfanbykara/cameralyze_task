from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models import Book
from rest_framework import status
from .serializers import BookSerializer
from django.shortcuts import get_object_or_404

# Explore urls for crud operations.
@api_view(['GET'])
def get_routes(request):
    routes = [
        'GET /api',
        'GET /api/books/',
        'GET /api/books/<str:pk>/',
        'POST /api/add-book/',
        'POST /api/update-book/<str:pk>/',
        'DELETE /api/delete-book/<str:pk>',

    ]
    return Response(routes,)


#This request returns the all books in the database.
@api_view(['GET'])
def fetch_books(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)

#This post request appends a new book to the database if the body is valid.
@api_view(['POST'])
def add_book(request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#This delete request returns HTTP 204 code if the book desired to be deleted exists.
@api_view(['GET','DELETE'])
def delete_book(request,pk):
    book = get_object_or_404(Book,pk=pk)
    book.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

#This get request returns a single book by id if exists
@api_view(['GET'])
def retrieve_book(request,pk):
    book = get_object_or_404(Book,pk=pk)
    serializer = BookSerializer(book, many=False)
    return Response(serializer.data)


# This post request returns an updated book if conditions are satisfied.
@api_view(['POST'])
def update_book(request,pk):
    book = get_object_or_404(Book,pk=pk)
    serializer = BookSerializer(instance=book, many=False,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


