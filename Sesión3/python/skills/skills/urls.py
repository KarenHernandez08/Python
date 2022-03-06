"""skills URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from books.views import (
    RetrieveBooks, 
    RetrieveAuthor,
    CreateAuthor,
    CreateBook,
    RetrieveAuthorAPIView,
    RetrieveBooksAPIView

    )

urlpatterns = [
    path('admin/', admin.site.urls), #url para entrar al administrador
    path('books/', RetrieveBooks.as_view()), 
    path('author/', RetrieveAuthor.as_view()),
    path('author/created', CreateAuthor.as_view()),
    path('books/created', CreateBook.as_view()),
    path('authors/<int:author_id>/',RetrieveAuthorAPIView.as_view()),
    path('books/<int:book_id>/',RetrieveBooksAPIView.as_view()),
]
