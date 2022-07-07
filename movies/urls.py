from django.urls import path
from . import views

urlpatterns = [
    path("", views.MovieView.as_view()),
    path("filter/<slug:slug>/", views.MovieGanreView.as_view(), name='ganre_filter'),
    path("search/", views.Search.as_view(), name='search'),
    path("about/", views.about),
    path("genres/", views.GanreView.as_view(), name='ganre'),
    path("contactus/", views.contact_us),
    path("<slug:slug>/", views.MovieDetailView.as_view(), name='movie_details'),
    path("actor/<str:slug>/", views.ActorDetailView.as_view(), name='actors_details'),
    path("/", views.AddReview.as_view(), name='add_review'),
]