from django.contrib import admin

from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_date')
    # fields = ('title', 'content', 'created_date')
    readonly_fields = ('created_date', 'modified_date')
    list_filter = ('created_date', )
    list_display_links = ('id', )
    search_fields = ('title', )
    list_per_page = 25
    ordering = ('-id', )
    prepopulated_fields = {'slug': ('title', )}


admin.site.register(Article, ArticleAdmin)

