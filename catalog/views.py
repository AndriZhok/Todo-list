from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from catalog.models import Tag, Task


def index(request: HttpRequest) -> HttpResponse:
    num_tags = Tag.objects.count()
    num_tasks = Task.objects.count()

    context = {
        "num_tags": num_tags,
        "num_tasks": num_tasks,
    }
    return render(request, "catalog/index.html", context=context)
