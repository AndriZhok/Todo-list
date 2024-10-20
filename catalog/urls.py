from django.urls import path

from catalog.views import (
    TaskListView,
    TagsListView,
    TagsCreateView,
    TagsUpdateView,
    TagsDeleteView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    ToggleTaskStatusView,
    task_list_view,
    task_search,
)

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("tasksowerview/", task_list_view, name="task-overview"),
    path("task-search/", task_search, name="task-search"),
    path("tags/", TagsListView.as_view(), name="tags-list"),
    path("tags/create/", TagsCreateView.as_view(), name="tags-create"),
    path("tags/update/<int:pk>/", TagsUpdateView.as_view(), name="tags-update"),
    path("tags/delete/<int:pk>/", TagsDeleteView.as_view(), name="tags-delete"),
    path("task/create/", TaskCreateView.as_view(), name="task-create"),
    path("task/update/<int:pk>/", TaskUpdateView.as_view(), name="task-update"),
    path("task/delete/<int:pk>/", TaskDeleteView.as_view(), name="task-delete"),
    path(
        "tasks/toggle-status/<int:pk>/",
        ToggleTaskStatusView.as_view(),
        name="task-toggle-status",
    ),
]

app_name = "catalog"
