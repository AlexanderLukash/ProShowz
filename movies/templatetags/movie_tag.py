from django import template
from ..models import Ganre, Movie, Actor, Reviews


register = template.Library()


@register.simple_tag()
def get_ganres():
    return Ganre.objects.all()


@register.inclusion_tag('movies/tags/last_movies.html')
def get_last_movies():
    movies = Movie.objects.order_by('-id').filter(draft=False)[:10]
    return {"last_movies": movies}


@register.inclusion_tag('movies/tags/random_movies.html')
def get_random_movies():
    movies = Movie.objects.order_by('?')[:5]
    return {"random_movies": movies}


@register.inclusion_tag('movies/tags/need_watch.html')
def get_need_movies():
    movies = Movie.objects.order_by('?')[:5]
    return {"need_movies": movies}


@register.inclusion_tag('movies/tags/random_ganre.html')
def get_random_ganres():
    movies = Ganre.objects.order_by('?')[:8]
    return {"random_ganre": movies}


@register.inclusion_tag('movies/tags/random_banner.html')
def get_random_banner():
    movies = Movie.objects.order_by('?')[:4]
    return {"random_banner": movies}


@register.inclusion_tag('movies/tags/actor_list.html')
def get_random_actor():
    movies = Actor.objects.order_by('?')[:20]
    return {"random_actor": movies}


@register.inclusion_tag('movies/tags/film_banner.html')
def get_film_banner():
    movies = Movie.objects.order_by('?')[:1]
    return {"random_banners": movies}


@register.inclusion_tag('movies/tags/reviews_list.html')
def get_reviews_list():
    movies = Reviews.objects.order_by('-id').filter(draft=False)[:10]
    return {"review_list": movies}


@register.simple_tag()
def get_movies_count():
    return Movie.objects.all().count()


@register.simple_tag()
def get_reviews_count():
    return Reviews.objects.all().count()


@register.inclusion_tag('movies/tags/random_ganre_banner.html')
def get_random_ganre_banner():
    movies = Movie.objects.order_by('?')[:1]
    return {"random_banner_ganre": movies}
