from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from catalog.forms import TagsForm
from catalog.models import Tag, Task


def index(request: HttpRequest) -> HttpResponse:
    num_tags = Tag.objects.count()
    num_tasks = Task.objects.count()

    context = {
        "num_tags": num_tags,
        "num_tasks": num_tasks,
    }
    return render(request, "catalog/index.html", context=context)


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
