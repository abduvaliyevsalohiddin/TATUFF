from rest_framework.generics import *
from rest_framework.views import APIView

from mainApp.models import Book, CheckBook
from mainApp.serializers import BookSerializer, CheckBookSerializer


class BookCreateAPIView(CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookListAPIView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookRetrieveAPIView(RetrieveAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class CheckBookCreateAPIView(CreateAPIView):
    queryset = CheckBook.objects.all()
    serializer_class = CheckBookSerializer
