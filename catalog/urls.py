from django.urls import path

from catalog.views import (
    index,
    TagsListView,
    TagsCreateView,
    TagsUpdateView,
    TagsDeleteView,
)

urlpatterns = [
    path("", index, name="index"),
    path("tags/", TagsListView.as_view(), name="tags-list"),
    path("tags/create/", TagsCreateView.as_view(), name="tags-create"),
    path("tags/update/<int:pk>/", TagsUpdateView.as_view(), name="tags-update"),
    path("tags/delete/<int:pk>/", TagsDeleteView.as_view(), name="tags-delete"),

]

app_name = "catalog"
