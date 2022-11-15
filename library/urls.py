from django.urls import path
from library import views

urlpatterns = [
    path('', views.home, name='libhome'),
    path('about/', views.about, name='libabout'),
    path('books/', views.BookListView.as_view(), name='libbooks'),
    path('books/book/<int:pk>/', views.BookDetailView.as_view(), name="book-detail"),
    path('my_books/', views.RentedBooksByUserListView.as_view(), name="my_books"),
    path('books/book/?P<pk>[-\w]+/renew', views.BookUpdate.as_view(), name='renew-book-librarian')
]