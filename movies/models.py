
from django.core.validators import FileExtensionValidator
from django.db import models
from datetime import date
from django.urls import reverse
import random


# Категории


class Category(models.Model):
    name = models.CharField("Категорія", max_length=150)
    description = models.TextField("Описання")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категорія"
        verbose_name_plural = "Категорії"


# Actor
class Actor(models.Model):
    name = models.CharField("Ім'я", max_length=100)
    age = models.PositiveSmallIntegerField("Вік", default=0)
    description = models.TextField("Описання")
    image = models.ImageField("Зображення", upload_to="actors/")


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("actors_details", kwargs={"slug": self.name})


    class Meta:
        verbose_name = "Актори та режисери"
        verbose_name_plural = "Актори та режисери"


# Ganre
class Ganre(models.Model):
    name = models.CharField("Ім'я", max_length=100)
    description = models.TextField("Описання")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("ganre_filter", kwargs={"slug": self.url})


    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанри"


# Films
class Movie(models.Model):
    title = models.CharField("Назва", max_length=100)
    tagline = models.CharField("Слоган", max_length=100, default='')
    description = models.TextField("Описання")
    description_small = models.CharField("Описання коротко", max_length=100, null=True)
    time_h = models.IntegerField("Години", default=1)
    time_m = models.IntegerField("Хвилини", default=1)
    poster = models.ImageField("Постер", upload_to="movies/")
    banner = models.ImageField("Банер", upload_to="movies/banner/", null=True)
    treiler = models.URLField("Трейлер", max_length=300, null=True)
    films = models.URLField("Фільм", max_length=300, null=True)
    year = models.PositiveSmallIntegerField("Дата виходу", default=2019)
    country = models.CharField("Країна", max_length=30)
    directors = models.ManyToManyField(Actor, verbose_name="режисер", related_name="film_director")
    actor = models.ManyToManyField(Actor, verbose_name="актори", related_name="film_actor")
    ganres = models.ManyToManyField(Ganre, verbose_name="жанри")
    world_premiere = models.DateField("Прем'єра у світі", default=date.today)
    budget = models.PositiveIntegerField("Бюджет", default=0, help_text="вказуйте сумму в доларах.")
    fees_in_usa = models.PositiveIntegerField("Зібрав у США", default=0, help_text="вказуйте сумму в доларах.")
    fees_in_world = models.PositiveIntegerField("Зібрав у світі", default=0, help_text="вказуйте сумму в доларах.")
    category = models.ForeignKey(Category, verbose_name="Категорія", on_delete=models.SET_NULL, null=True)
    url = models.SlugField(max_length=130, unique=True)
    draft = models.BooleanField("Чернетка", default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("movie_details", kwargs={"slug": self.url})


    class Meta:
        verbose_name = "Фільм"
        verbose_name_plural = "Фільми"


# MovieShots
class MovieShots(models.Model):
    title = models.CharField("Заголовок", max_length=100)
    description = models.TextField("Описання")
    image = models.ImageField("Зображення", upload_to="movie_shots/")
    movie = models.ForeignKey(Movie, verbose_name="Фільм", on_delete=models.CASCADE)

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = "Кадр із фільму"
        verbose_name_plural = "Кадри з фільму"


# RatingStar
class RatingStar(models.Model):
    value = models.SmallIntegerField("Значення", default=0)

    def __str__(self):
        return self.value


    class Meta:
        verbose_name = "Зірка рейтингу"
        verbose_name_plural = "Зірки рейтингу"


class Rating(models.Model):
    ip = models.CharField("IP адрес", max_length=15)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name="зірка")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name="фільм")

    def __str__(self):
        return f"{self.star} - {self.movie}"


    class Meta:
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"


# Reviews
class Reviews(models.Model):
    email = models.EmailField()
    name = models.CharField("Ім'я", max_length=100)
    last_name = models.CharField("Прізвище", max_length=100, null=True)
    loc = models.CharField("Країна", max_length=100, null=True)
    text = models.TextField("Повідомлення", max_length=200)
    draft = models.BooleanField("Чернетка", default=True)

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = "Відгук"
        verbose_name_plural = "Відгуки"
