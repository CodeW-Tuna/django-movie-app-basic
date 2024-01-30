from django.urls import path
from . import views


#http://127.0.0.1:8000/movies/1
#http://127.0.0.1:8000/anasayfa/
#http://127.0.0.1:8000/


urlpatterns = [
    path("",views.anasayfa),
    path("anasayfa/",views.anasayfa, name="anasayfa"),
    path("movies/", views.movies, name="filmler"),
    path("movies/<int:id>", views.watch, name="watchnow"),
    path("categories/", views.categories, name="categories")
]

 