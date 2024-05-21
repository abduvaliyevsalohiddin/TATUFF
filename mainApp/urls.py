from django.urls import path, include
from .views import *

urlpatterns = [
    path('bookCreate/', BookCreateAPIView.as_view(), name='book_create'),
    path('books/', BoookListAPIView.as_view(), name='books'),
    path('book/<int:pk>/', BookRetrieveAPIView.as_view(), name='book'),
    path('checkBookCreate/', CheckBookCreateAPIView.as_view(), name='checkbook_create'),
]
