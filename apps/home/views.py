from django.shortcuts import render

from apps.home.models import Setting
from apps.portfolio.models import Portfolio
from apps.price.models import Price
from apps.service.models import Service, Help_bus
from apps.team.models import Team, Statistic


def home(request):
    return render(request, 'index.html')


def home(request):
    setting = Setting.objects.get(pk=1)
    service = Service.objects.all().order_by('-id')[:5]
    help_bus = Help_bus.objects.all().order_by('-id')[:8]
    portfolio = Portfolio.objects.all().order_by('-id')[:3]
    context = {
        'setting':setting, 
        'category':category, 
        'slider':slider, 
        'product':product,
        'reviews':reviews,
    }
    return render(request, 'index.html', context)