from django.http import request
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, DetailView
from pyexpat import model

from .models import Movie, Ganre, Actor
from .forms import ReviewForm


def about(request):
    return render(request, 'movies/about.html')


def contact_us(request):
    return render(request, 'movies/contact.html')


def ganres_list(request):
    return render(request, 'movies/genre.html')


class MovieView(ListView):
    model = Movie
    queryset = Movie.objects.filter(draft=False)
    template_name = "movies/index.html"
    paginate_by = 20


class MovieDetailView(DetailView):
    model = Movie
    slug_field = 'url'


class ActorDetailView(DetailView):
    model = Actor
    template_name = 'movies/actors_detail.html'
    slug_field = "name"


class MovieGanreView(ListView):
    model = Ganre
    template_name = 'movies/ganre_filter.html'
    context_object_name = 'movie_list'

    def get_queryset(self):
        return Movie.objects.filter(ganres__url=self.kwargs.get('slug'))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['ganre_name'] = self.kwargs.get('slug')
        return context


class AddReview(View):
    def post(self, request):
        form = ReviewForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
        return redirect("../")


class Search(ListView):
    template_name = "movies/search.html"

    def get_queryset(self):
        return Movie.objects.filter(title__icontains=self.request.GET.get('q'))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['q'] = self.request.GET.get('q')
        return context


class GanreView(ListView):
    model = Ganre
    template_name = "movies/genre.html"

    def get_queryset(self):
        return Movie.objects.filter(ganres__url=self.kwargs.get('slug'))
