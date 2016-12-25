from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from eae.serializers import *
from eae.models import *

# Create your views here.

@api_view(['GET'])
def getbooks(request,pk):
    books = Book.objects.get(pk=pk)
    serializer = BookSerializer(books)
    return Response(serializer.data)

class all_books(APIView):
    def get(self,request):
        Books = Book.objects.all()
        serializer = BookSerializer(Books,many=True)
        return Response(serializer.data)

class get_book(APIView):
    def get(request,self,pk):
        book = Book.objects.get(pk=pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)
