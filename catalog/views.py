from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, render
from task_lib_wrapper import get_task_summary, count_tasks_with_tag, calculate_progress

from catalog.forms import TagsForm, TasksForm
from catalog.models import Tag, Task


def task_list_view(request):
    tasks = Task.objects.all().order_by('if_field', '-datetime')
    summary = get_task_summary([task.if_field for task in tasks])
    tagged_count = count_tasks_with_tag([tag.id for task in tasks for tag in task.tags.all()], target_tag=1)
    progress = calculate_progress([task.if_field for task in tasks]) * 100

    context = {
        'task_list': tasks,
        'summary': summary,
        'tagged_count': tagged_count,
        'progress': progress,
    }
    return render(request, 'catalog/index.html', context)


def task_search(request):
    tag = request.GET.get("tag", "")
    tagged_count = Task.objects.filter(tags__name=tag).count()
    return JsonResponse({"tagged_count": tagged_count})


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
