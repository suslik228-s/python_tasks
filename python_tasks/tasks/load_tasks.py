import json
from tasks.models import Task

with open('python_tasks_with_levels.json', encoding='utf-8') as f:
    tasks = json.load(f)

for item in tasks:
    Task.objects.create(
        title=item['title'],
        description=item['description'],
        answer_code=item['answer_code'],
        explanation=item['explanation'],
        level=item['level']
    )

print("Задачи загружены.")
