from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer

@api_view(['GET'])
def task_list_api(request):
    level = request.GET.get('level')
    tasks = Task.objects.all()
    if level:
        tasks = tasks.filter(level=level)
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)
