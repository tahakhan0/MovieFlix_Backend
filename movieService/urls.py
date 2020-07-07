from django.urls import path

from . import views

urlpatterns = [
    path('genres/', views.GenresList.as_view()),
    path("genres/<int:pk>/", views.GenresDetail.as_view()),
    path('movies/', views.MoviesList.as_view()),
    path('movies/<int:pk>/', views.MoviesDetails.as_view()),
    path('movies/<int:pk>/delete/', views.MoviesDeleteView.as_view()),
]
