from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.db.models import Count

from .models import Subscription, User


@admin.register(User)
class FoodgramUserAdmin(UserAdmin):
    list_display = (
        'id',
        'username',
        'email',
        'first_name',
        'last_name',
        'recipes_count',
        'followers_count',
        'is_staff',
    )
    search_fields = (
        'username',
        'email',
        'first_name',
        'last_name',
    )
    list_filter = ('is_staff', 'is_active', 'is_superuser')
    fieldsets = UserAdmin.fieldsets + (
        ('Дополнительно', {'fields': ('avatar',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Дополнительно', {'fields': ('avatar',)}),
    )

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.annotate(
            _recipes_count=Count('recipes', distinct=True),
            _followers_count=Count('subscriptions_to_the_author',
                                   distinct=True),
        )

    @admin.display(description='Рецепты', ordering='_recipes_count')
    def recipes_count(self, obj):
        return obj._recipes_count

    @admin.display(description='Подписчики', ordering='_followers_count')
    def followers_count(self, obj):
        return obj._followers_count


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'author')
    search_fields = (
        'user__username',
        'user__email',
        'author__username',
        'author__email',
    )
