from django.contrib import admin
from .models import (
    Tag,
    Recipe,
    Ingredient
)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('title', )


class IndentAdminTabularInLine(admin.TabularInline):
    model = Ingredient
    extra = 1


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    inlines = (IndentAdminTabularInLine, )
    list_display = ('id', 'title', 'author', 'created_date')
    search_fields = ('title', 'author__username')
    list_filter = ('author', 'created_date')
    autocomplete_fields = ('author', )
    date_hierarchy = 'created_date'
    filter_horizontal = ('tags', )
    readonly_fields = ('created_date', 'slug')


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('id', 'recipe', 'title', 'quantity', 'unit', 'is_active')
    search_fields = ('title', 'recipe__title')
    list_filter = ('is_active', 'unit')
    autocomplete_fields = ('recipe', )
