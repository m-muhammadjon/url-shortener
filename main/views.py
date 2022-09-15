import json

from django.core.validators import URLValidator, ValidationError
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from main import models
from main.utils import get_valid_shorted_link


def home(request):
    return render(request, 'index.html')


@csrf_exempt
@require_POST
def short_url(request):
    validator = URLValidator()
    data = json.loads(request.body)
    user_id = data.get('user_id')
    link = data.get('link')
    if 'http' not in link:
        link = f'http://{link}'
    try:
        validator(link)

        if user_id is not None:
            user, created = models.User.objects.get_or_create(uid=user_id)
            shorted = get_valid_shorted_link()
            shorted_link = models.ShortedLink.objects.create(user=user, url=link, shorted=shorted)
            return JsonResponse({'status': 'ok',
                                 'shorted': f'{request.META["HTTP_HOST"]}/{shorted}'})
        else:
            shorted = get_valid_shorted_link()
            shorted_link = models.ShortedLink.objects.create(url=link, shorted=shorted)

            return JsonResponse({'status': 'ok',
                                 'shorted': f'{request.META["HTTP_HOST"]}/{shorted}'})
    except ValidationError:
        return JsonResponse({'status': 'error',
                             'message': 'Please enter valid URL'})


def redirect_to_original_link(request, shorted):
    if shorted and shorted != 'favicon.ico':
        link = models.ShortedLink.objects.get(shorted=shorted)
        url = link.url
        if 'http' not in url:
            url = f'http://{url}'
        visitor = models.Visitor.objects.create()
        link.visitors.add(visitor)
        return redirect(url)
    else:
        return HttpResponseRedirect('/')


def history(request):
    user_id = request.GET.get('uid')
    links = None
    try:
        user = models.User.objects.get(uid=user_id)
        links = user.links.all()
    except models.User.DoesNotExist:
        pass
    return render(request, 'history.html', {'links': links})


def shorted_detail(request, shorted):
    link = models.ShortedLink.objects.get(shorted=shorted)
    host = request.get_host()
    return render(request, 'historyDetail.html', {'host': host,
                                                  'link': link})
