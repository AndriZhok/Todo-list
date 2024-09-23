from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404

from catalog.forms import TagsForm, TasksForm
from catalog.models import Tag, Task


class TagViewBase(View):
    model = Tag
    success_url = reverse_lazy("catalog:tags-list")


class TagsListView(TagViewBase, ListView):
    template_name = "catalog/tags_list.html"


class TagsCreateView(TagViewBase, CreateView):
    form_class = TagsForm
    template_name = "catalog/tags_form.html"


class TagsUpdateView(TagViewBase, UpdateView):
    form_class = TagsForm
    template_name = "catalog/tags_form.html"


class TagsDeleteView(TagViewBase, DeleteView):
    template_name = "catalog/tags_form_confirm_delete.html"


class TaskViewBase(View):
    model = Task
    success_url = reverse_lazy("catalog:task-list")


class TaskListView(TaskViewBase, ListView):
    template_name = "catalog/tasks_list.html"


class TaskCreateView(TaskViewBase, CreateView):
    form_class = TasksForm
    template_name = "catalog/task_form.html"


class TaskUpdateView(TaskViewBase, UpdateView):
    form_class = TasksForm
    template_name = "catalog/task_form.html"


class TaskDeleteView(TaskViewBase, DeleteView):
    template_name = "catalog/task_confirm_delete.html"


class ToggleTaskStatusView(View):
    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.if_field = not task.if_field
        task.save()
        return HttpResponseRedirect(reverse("catalog:task-list"))
