from django.shortcuts import get_object_or_404 # esta funcion devuelve una respuesta 404 para no hacer metodos try y catch

from rest_framework import status

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from books.models import Books, Author
from books.serializers import AuthorSerializer, BooksSerializer

# Create your views here.

class RetrieveBooks(APIView):
    permission_classes=(AllowAny,)
    
    def get(self, request):
        books_list= Books.objects.all()
        serializer= BooksSerializer(books_list, many=True)
        return Response(serializer.data)
    
class RetrieveAuthor(APIView):
    permission_classes=(AllowAny,)
    
    def get(self, request):
        author_list= Author.objects.all()
        serializer= AuthorSerializer(author_list, many=True)
        return Response (serializer.data)
    
class CreateAuthor(APIView):
    permission_classes=(AllowAny,)
    
    def post(self, request):
        data = request.data
        serializer = AuthorSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
       # if serializer.is_valid():
         #   return Response(serializer.errors,  status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CreateBook(APIView):
    permission_classes =(AllowAny,)
    
    def post(self, request):
        data = request.data
        serializer = BooksSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    
class RetrieveAuthorAPIView(APIView):
    permission_classes = (AllowAny,)
    
    def get(self,request, author_id):
        author_obj =Author.objects.get(id= author_id) #id y pk trabaja igual
        serializer= AuthorSerializer(author_obj)
        return Response(serializer.data)
    
class RetrieveBooksAPIView(APIView):
    permission_classes = (AllowAny,)
    
    def get(self,request, book_id):
       # book_obj =Books.objects.get(id= book_id) #id y pk trabaja igual
        book_obj =get_object_or_404(Books, pk= book_id) # Nueva modificacion para que solo nos mande que no encontro el registro
        serializer= BooksSerializer(book_obj)
        return Response(serializer.data)

