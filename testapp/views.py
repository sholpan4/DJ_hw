import json
import logging

from django.contrib.auth.decorators import login_required
from django.core.serializers.json import DjangoJSONEncoder
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.http import StreamingHttpResponse, FileResponse, JsonResponse
from django.urls import resolve
from django.views.decorators.http import require_http_methods, require_GET
from django.views.generic import ListView

from bboard.models import Rubric, Bb
from .models import SMS


# def index(request):
#     resp_content = ('Здесь будет', ' главная', ' страница', ' сайта')
#     resp = StreamingHttpResponse(resp_content, content_type='text/plain; charset=utf-8')
#     return resp

# def index(request):
#     # file_name = r'static/bg.jpg'
#     file_name = r'static/lesson_15.zip'
#     return FileResponse(open(file_name, 'rb'), as_attachment=True, filename='file.zip')   # readbytes

# def index(request):
#     data = {'title': 'Мотоцикл', 'content': 'Старый', 'price': 10000.0}
#     return JsonResponse(data, encoder=DjangoJSONEncoder) # специальные ответы

# если есть решение поделиться

# def index(request):
#     context = {'title': 'Тестовая страница'}
#     return render(request, 'test.html', context)

# def index(request):
#     r = get_object_or_404(Rubric, name="Транспорт")
#     return redirect('bboard:by_rubric', rubric_id=r.id)

# декораторы
# @require_http_methods(['GET', 'POST'])
# @require_GET()
# @require_POST()
# @require_safe() #get, head
# @gzip_page()
def index(request):
    rubric = get_object_or_404(Rubric, name="Транспорт")
    bbs = get_list_or_404(Bb, rubric=rubric)
    res = resolve('/2/')
    context = {'title': 'Test side', 'bbs': bbs, 'res': res}
    return render(request, 'test.html', context)


@login_required
def protected_view(request):
    user = request.user
    tasks = user.tasks.all()
    context = {'user': user, 'tasks': tasks}
    return render(request, 'protected_template.html', context)


logger = logging.getLogger('my_logger')


def log_request_data(request):
    request_data = {
        'path': request.path,
        'method': request.method,
        'user_agent': request.META.get('HTTP_USER_AGENT', 'N/A'),
    }

    logger.info(request_data)

    return render(request, 'template_name.html')


class SMSListView(ListView):
    model = SMS
    template_name = 'sms_list.html'
    context_object_name = 'sms_list'

