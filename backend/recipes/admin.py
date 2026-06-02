from django.contrib import admin
from django.db.models import Count
from django.utils.safestring import mark_safe

from .models import (
    Favourite,
    Ingredient,
    Recipe,
    RecipeIngredient,
    ShoppingCart,
    Tag,
)


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    extra = 1
    min_num = 1


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'measurement_unit')
    search_fields = ('name',)
    list_filter = ('measurement_unit',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    search_fields = ('name', 'slug')
    list_filter = ('name',)


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'author',
        'ingredients_list',
        'tags_list',
        'image_preview',
        'favourites_count',
        'pub_date',
    )
    search_fields = ('name', 'author__username', 'author__email')
    list_filter = ('tags',)
    inlines = (RecipeIngredientInline,)

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.annotate(
            _favourites_count=Count('favourites', distinct=True)
        ).prefetch_related('tags', 'ingredients')

    @admin.display(description='Ингредиенты')
    def ingredients_list(self, obj):
        return ', '.join(
            ingredient.name for ingredient in obj.ingredients.all()
        )

    @admin.display(description='Теги')
    def tags_list(self, obj):
        return ', '.join(tag.name for tag in obj.tags.all())

    @admin.display(description='Картинка')
    def image_preview(self, obj):
        return mark_safe(
            f'<img src="{obj.image.url}" width="80" height="60">'
        )

    @admin.display(description='Избранное', ordering='_favourites_count')
    def favourites_count(self, obj):
        return obj._favourites_count


@admin.register(RecipeIngredient)
class RecipeIngredientAdmin(admin.ModelAdmin):
    list_display = ('id', 'recipe', 'ingredient', 'amount')
    search_fields = ('recipe__name', 'ingredient__name')
    list_filter = ('ingredient',)


@admin.register(Favourite)
class FavouriteAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'recipe')
    search_fields = ('user__username', 'user__email', 'recipe__name')
    list_filter = ('recipe',)


@admin.register(ShoppingCart)
class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'recipe')
    search_fields = ('user__username', 'user__email', 'recipe__name')
    list_filter = ('recipe',)
