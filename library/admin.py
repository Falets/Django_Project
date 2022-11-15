from django.contrib import admin
from library.models import Genre, Book, BookIns, Author, Post

# Register your models here.
admin.site.register(Genre)
admin.site.register(Book)
admin.site.register(BookIns)
admin.site.register(Author)
admin.site.register(Post)