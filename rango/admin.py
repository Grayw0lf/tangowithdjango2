from django.contrib import admin
from .models import Category, Page, UserProfile


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'views', 'likes']
    prepopulated_fields = {'slug': ('name',)}


class PageAdmin(admin.ModelAdmin):
    list_display = ['title', 'url', 'category']
    list_filter = ['category']
    list_editable = ['category']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(UserProfile)
