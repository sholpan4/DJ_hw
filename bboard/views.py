from django.contrib.auth.models import User
from django.db.models import Count
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView
from django.views.generic.base import TemplateView, View
from django.template import loader
from django.template.loader import get_template, render_to_string
from django.views.generic.edit import CreateView

from .forms import BbForm, RubricForm
from .models import Bb, Rubric


def index(request):
    bbs = Bb.objects.all()
    rubrics = Rubric.objects.annotate(cnt=Count('bb')).filter(cnt__gt=0)
    context = {'bbs': bbs, 'rubrics': rubrics}
    return HttpResponse (
        render_to_string('index.html', context, request)
    )


class BbByRubricView(TemplateView):
    template_name = 'by_rubric.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bbs'] = Bb.objects.filter(rubric=context['rubric_id'])
        context['rubrics'] = Rubric.objects.all()
        context['current_rubric'] = Rubric.objects.get(pk=context['rubric_id'])
        return context


class BbCreateView(CreateView):
    template_name = 'create.html'
    form_class = BbForm
    success_url = reverse_lazy('bboard:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['rubrics'] = Rubric.objects.all()
        # context['rubrics'] = Rubric.objects.filter(bb__isnull=False).distinct()
        context['rubrics'] = Rubric.objects.annotate(cnt=Count('bb')).filter(cnt__gt=0)
        return context


class RubricCreateView(CreateView):
    template_name = 'create_rubric.html'
    form_class = RubricForm
    success_url = reverse_lazy('bboard:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context


class AllUsersView(View):
    def get(self, request):
        users = User.objects.all()
        return render(request, 'all.users.html', {'users': users})


class UserDetailsView(View):
    def get(self, request, user_id=None):
        user = User.objects.get(id=user_id)
        return render(request, 'user_details.html', {'user': user})
