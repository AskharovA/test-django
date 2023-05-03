from django.shortcuts import render, get_object_or_404
from .models import ZodiacModel
from django.http import HttpResponseRedirect


def main(request):
    zodiacs = ZodiacModel.objects.all()
    return render(request, 'zodiac_app/main.html', context={'zodiacs': zodiacs})


def info(request, name_zodiac):
    zodiacs = ZodiacModel.objects.all()
    zodiac = get_object_or_404(ZodiacModel, slug=name_zodiac)
    return render(request, 'zodiac_app/info.html', context={'zodiac': zodiac, 'zodiacs': zodiacs})


def date(request):
    from datetime import date
    try:
        d, m, _ = map(int, request.GET['date'].split('.'))
        date(1991, m, d)
    except:
        return HttpResponseRedirect('/')
    zd = ''
    if m == 3 and d >= 21 or m == 4 and d <= 20:
        zd = 'oven'
    elif m == 4 and d >= 21 or m == 5 and d <= 20:
        zd = 'telec'
    elif m == 5 and d >= 21 or m == 6 and d <= 21:
        zd = 'blizneci'
    elif m == 6 and d >= 22 or m == 7 and d <= 22:
        zd = 'rak'
    elif m == 7 and d >= 23 or m == 8 and d <= 22:
        zd = 'lev'
    elif m == 8 and d >= 23 or m == 9 and d <= 23:
        zd = 'deva'
    elif m == 9 and d >= 24 or m == 10 and d <= 23:
        zd = 'vesi'
    elif m == 10 and d >= 24 or m == 11 and d <= 22:
        zd = 'scorpion'
    elif m == 11 and d >= 23 or m == 12 and d <= 21:
        zd = 'strelec'
    elif m == 12 and d >= 22 or m == 1 and d <= 20:
        zd = 'kozerog'
    elif m == 1 and d >= 21 or m == 2 and d <= 18:
        zd = 'vodolei'
    elif m == 2 and d >= 19 or m == 3 and d <= 20:
        zd = 'ribi'
    if zd:
        return HttpResponseRedirect(f'horoscope/{zd}')
    return HttpResponseRedirect('/')


def profile_view(request):
    return render(request, 'zodiac_app/profile.html')