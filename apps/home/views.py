from django.shortcuts import render

from apps.home.models import Setting
from apps.portfolio.models import Portfolio
from apps.price.models import Price
from apps.service.models import Service, Help_bus, My_steak
from apps.team.models import Team, Statistic



def home(request):
    setting = Setting.objects.get(pk=1)
    service = Service.objects.all().order_by('-id')[:5]
    help_bus = Help_bus.objects.all().order_by('-id')[:8]
    portfolio = Portfolio.objects.all().order_by('-id')[:3]
    statistic = Statistic.objects.all().order_by('-id')[:4]
    context = {
        'setting':setting, 
        'service':service, 
        'portfolio':portfolio,
        'statistic':statistic,
        'help_bus':help_bus, 
    }
    return render(request, 'index.html', context)


# PAGES
def aboutus(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting':setting,}
    return render(request, 'pages/aboutus.html', context)


def team(request):
    setting = Setting.objects.get(pk=1)
    team = Team.objects.all()
    context = {'setting':setting, 'team':team}
    return render(request, 'pages/teams.html', context)


def portfolio(request):
    setting = Setting.objects.get(pk=1)
    portfolio = Portfolio.objects.all()
    context = {'setting':setting, 'portfolio':portfolio}
    return render(request, 'pages/portfolio.html', context)


def service(request):
    setting = Setting.objects.get(pk=1)
    services = Service.objects.all()
    steak = My_steak.objects.all()
    context = {'setting':setting, 'services':services, 'steak':steak}
    return render(request, 'pages/service.html', context)


def price(request):
    setting = Setting.objects.get(pk=1)
    price = Price.objects.all()
    context = {'setting':setting, 'price':price}
    return render(request, 'pages/price.html', context)

