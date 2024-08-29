from django.urls import path

from record.apps import RecordConfig
from record.views import BaseView, RecordCreateView, RecordListView, RecordDetailView, RecordUpdateView, \
    RecordDeleteView, search

app_name = RecordConfig.name

urlpatterns = [
    path('', BaseView.as_view(), name='home', kwargs={'template_name': 'index.html'}),
    path('create', RecordCreateView.as_view(), name='create'),
    path('list', RecordListView.as_view(), name='list'),
    path("detail/<int:pk>/", RecordDetailView.as_view(), name="detail",),
    path("update/<int:pk>/", RecordUpdateView.as_view(), name="update"),
    path("delete/<int:pk>/", RecordDeleteView.as_view(), name="delete"),
    path("search/", search, name="search"),
]
