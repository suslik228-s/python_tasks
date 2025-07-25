# tasks/views.py
from django.shortcuts import render
from django.utils.translation import get_language
from .models import Task
from django.db.models import Q

def task_list(request):
    lang = get_language()

    q = request.GET.get('q', '').strip()
    level_filter = request.GET.get('level', '').strip()

    tasks = Task.objects.all()

    if level_filter in ['beginner', 'intermediate', 'advanced']:
        tasks = tasks.filter(level=level_filter)

    if q:
        # Поиск в заголовках на обоих языках (можно добавить описание, если нужно)
        tasks = tasks.filter(
            Q(title_ru__icontains=q) | Q(title_en__icontains=q)
        )

    # Добавляем атрибуты для шаблона (title, description, explanation с учётом языка)
    for task in tasks:
        task.title = task.get_title(lang)
        task.description = task.get_description(lang)
        task.explanation = task.get_explanation(lang)
        task.level_display = task.get_level_display()

    context = {
        'tasks': tasks,
        'q': q,
        'level_filter': level_filter,
    }
    return render(request, 'tasks/task_list.html', context)
