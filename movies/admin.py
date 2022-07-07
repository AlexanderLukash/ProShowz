from django.contrib import admin
from django import forms
from django.utils.safestring import mark_safe
from .models import Category, Ganre, Movie, MovieShots, Actor, Rating, RatingStar, Reviews


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display =("id", "name", "url")
    list_display_links = ("name",)





class MovieShotsInline(admin.TabularInline):
    model = MovieShots
    extra = 0
    readonly_fields = ("get_full_image",)

    def get_full_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="200" height="110"')

    get_full_image.short_description = "Зображення"

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display =("id", "title", "category", "url", "draft")
    list_display_links = ("title",)
    list_filter = ("category", "ganres")
    search_fields = ("title", "category__name")
    inlines = [MovieShotsInline]
    save_on_top = True
    save_as = True
    actions = ["published", "unpublished"]
    readonly_fields = ("get_full_image", "get_banner_image")
    list_editable = ("draft",)
    fieldsets = (
        (None, {
            "fields": (("title", "tagline"), )
        }),
        (None, {
            "fields": (("description"),)
        }),
        (None, {
            "fields": (("description_small"),)
        }),
        (None, {
            "fields": (("time_h", "time_m"),)
        }),
        (None, {
            "fields": (("poster", "banner", "get_full_image", "get_banner_image"),)
        }),
        (None, {
            "fields": (("treiler", "films"),)
        }),
        (None, {
            "fields": (("year", "country", "world_premiere"),)
        }),
        ("Actors", {
            "classes": ("collapse",),
            "fields": (("directors", "actor", "ganres"),)
        }),
        (None, {
            "fields": (("budget", "fees_in_usa", "fees_in_world"),)
        }),
        ("Options", {
            "fields": (("category", "url", "draft"),)
        }),
    )

    def unpublished(self, request, queryset):
        row_update = queryset.update(draft=True)
        if row_update == 1:
            message_bit = "1 запис був оновлений."
        else:
            message_bit = f"{row_update} записів було оновлено."
        self.message_user(request, f"{message_bit}")

    def published(self, request, queryset):
        row_update = queryset.update(draft=False)
        if row_update == 1:
            message_bit = "1 запис був опублікований."
        else:
            message_bit = f"{row_update} записів було опубліковано."
        self.message_user(request, f"{message_bit}")

    def get_full_image(self, obj):
        return mark_safe(f'<img src={obj.poster.url} width="100" height="110"')

    def get_banner_image(self, obj):
        return mark_safe(f'<img src={obj.banner.url} width="200" height="90"')

    get_full_image.short_description = "Постер"
    get_banner_image.short_description = "Баннер"
    published.short_description = "Опублікувати"
    published.allowed_permissions = ("change", )
    unpublished.short_description = "Зняти з публікації"
    unpublished.allowed_permissions = ("change",)


@admin.register(Reviews)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "last_name", "email", "loc")
    list_display_links = ("name", "last_name")


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ("name", "age", "get_image",)
    readonly_fields = ("get_full_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60"')

    def get_full_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100" height="110"')

    get_image.short_description = "Зображення"
    get_full_image.short_description = "Зображення"


@admin.register(MovieShots)
class MovieShotsAdmin(admin.ModelAdmin):
    list_display = ("title", "movie", "get_image",)
    readonly_fields = ("get_full_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="70" height="40"')

    def get_full_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="200" height="110"')

    get_image.short_description = "Зображення"
    get_full_image.short_description = "Зображення"


admin.site.register(Ganre)
admin.site.register(Rating)
admin.site.register(RatingStar)


admin.site.site_title = "ProShows"
admin.site.site_header = "ProShows"
