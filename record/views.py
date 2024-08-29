from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  TemplateView, UpdateView)

from record.forms import RecordForm
from record.models import Record


class BaseView(TemplateView):
    template_name = "record/index.html"


def base_view(request):
    return render(request, "record/index.html")


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

    results = Record.objects.filter(
        Q(name__icontains=query) | Q(description__icontains=query)
    )

    return render(request, "record/search.html", {"query": query, "results": results})
