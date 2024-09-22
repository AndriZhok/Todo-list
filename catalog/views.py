from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404

from catalog.forms import TagsForm, TasksForm
from catalog.models import Tag, Task


class TagsListView(ListView):
    model = Tag
    template_name = "catalog/tags_list.html"


class TagsCreateView(CreateView):
    model = Tag
    form_class = TagsForm
    success_url = reverse_lazy("catalog:tags-list")
    template_name = "catalog/tags_form.html"


class TagsUpdateView(UpdateView):
    model = Tag
    form_class = TagsForm
    success_url = reverse_lazy("catalog:tags-list")
    template_name = "catalog/tags_form.html"


class TagsDeleteView(DeleteView):
    model = Tag
    success_url = reverse_lazy("catalog:tags-list")
    template_name = "catalog/tags_form_confirm_delete.html"


class TaskListView(ListView):
    model = Task
    template_name = "catalog/tasks_list.html"


class TaskCreateView(CreateView):
    model = Task
    form_class = TasksForm
    success_url = reverse_lazy("catalog:task-list")
    template_name = "catalog/task_form.html"


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TasksForm
    success_url = reverse_lazy("catalog:task-list")
    template_name = "catalog/task_form.html"


class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy("catalog:task-list")
    template_name = "catalog/task_confirm_delete.html"


def toggle_task_status(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.if_field = not task.if_field
    task.save()
    return HttpResponseRedirect(reverse("catalog:task-list"))
