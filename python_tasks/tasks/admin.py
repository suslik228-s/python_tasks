from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title_ru', 'title_en', 'level')
    list_filter = ('level',)  # фильтр по уровню
    search_fields = ('title_ru', 'title_en')  # поиск по названиям
