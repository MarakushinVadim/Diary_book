from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    TemplateView,
    UpdateView,
)

from record.forms import RecordForm
from record.models import Record


class BaseView(TemplateView):
    template_name = "record/index.html"


class RecordCreateView(CreateView):
    model = Record
    form_class = RecordForm
    success_url = reverse_lazy("record:list")

    def form_valid(self, form):
        self.object = form.save()
        self.object.author = self.request.user
        self.object.save()

        form.instance.user = self.request.user

        return super().form_valid(form)


class RecordListView(LoginRequiredMixin, ListView):
    model = Record

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        r_user = self.request.user
        queryset = queryset.filter(author=r_user)
        if queryset is not None:
            return queryset
        raise PermissionDenied


class RecordDetailView(LoginRequiredMixin, DetailView):
    model = Record


class RecordUpdateView(LoginRequiredMixin, UpdateView):
    model = Record
    form_class = RecordForm
    success_url = reverse_lazy("record:list")


class RecordDeleteView(LoginRequiredMixin, DeleteView):
    model = Record
    success_url = reverse_lazy("record:list")


@login_required
def search(request):
    results = []
    if request.method == "GET":
        query = request.GET.get("search")
    if query == "":
        query = "None"
    r_user = request.user
    queryset = Record.objects.filter(author=r_user)
    for obj in queryset:
        if query in obj.name or query in obj.description:
            results.append(obj)

    return render(request, "record/search.html", {"query": query, "results": results})
