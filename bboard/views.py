from django.contrib.auth.models import User
from django.db.models import Count
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView
from django.views.generic.base import TemplateView, View
from django.template import loader
from django.template.loader import get_template, render_to_string
from django.views.generic.edit import CreateView

from .forms import BbForm, RubricForm
from .models import Bb, Rubric, Post


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


class AllUsersView(TemplateView):
    template_name = 'all_users.html'

    def get(self, request, **kwargs):
        users = User.objects.all()
        return render(request, 'all.users.html', {'users': users})


class UserDetailsView(TemplateView):
    template_name = 'user_datails.html'

    def get(self, request, **kwargs):
        user = User.objects.get_context_data(**kwargs)
        return render(request, 'user_details.html', {'user': user})


class SinglePostView(TemplateView):
    template_name = 'single_post.html'

    def get(self, request, **kwargs):
        posts = Post.objects.get(pk=Post.pk)
        return render(request, 'single_post.html', {'posts': posts})


class ChronologicalPostsView(TemplateView):
    template_name = 'chron_post.html'

    def get(self, request, **kwargs):
        posts = Post.objects.all().order_by('-pub_date')
        return render(request, 'chronological_posts.html', {'posts': posts})

    def get_queryset(self):
        return Post.objects.all().order_by('-pub_date')

    def get_json(self, request):
        posts = self.get_queryset()
        data = {'posts': [{'id': Post.pk, 'title': Post.title, 'pub_date': Post.put_date} for post in posts]}
        return JsonResponse(data)
