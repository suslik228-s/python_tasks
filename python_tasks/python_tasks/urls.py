# python_tasks/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django.views.generic import RedirectView

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('', RedirectView.as_view(pattern_name='tasks:task_list', permanent=False)),  # редирект с корня на текущий язык
]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include('tasks.urls')),  # 👈 чтобы /ru/ вело на список задач
)
