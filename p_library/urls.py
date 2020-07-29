from django.contrib import admin
from django.urls import path, include
from p_library import views
from p_library.views import AuthorEdit, AuthorList, author_create_many, books_authors_create_many, FriendList, FriendAdd
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

app_name = 'p_library'
urlpatterns = [
	path('author/create', AuthorEdit.as_view(), name='author_create'),
	path('authors', AuthorList.as_view(), name='author_list'),
	path('author/create_many', author_create_many, name='author_create_many'),
	path('admin/', admin.site.urls),
	path('', views.books_list),
	path('index/', views.index),
	path('index/book_increment/', views.book_increment),
	path('index/book_decrement/', views.book_decrement),
	path('publisher/', views.book_publisher),
	path('author/create', AuthorEdit.as_view(), name='author_create'),
	path('authors', AuthorList.as_view(), name='author_list'),
	path('author/create_many', author_create_many, name='author_create_many'),
	path('author_book/create_many', books_authors_create_many, name='author_book_create_many'),
	path('friend_add', FriendAdd.as_view(), name='friend_add'),
	path('friend_list', FriendList.as_view(), name='friend_list'),
]