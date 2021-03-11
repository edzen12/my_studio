from django.shortcuts import render

from apps.home.models import Setting
from apps.portfolio.models import Portfolio
from apps.price.models import Price
from apps.service.models import Service, Help_bus
from apps.team.models import Team


def home(request):
    return render(request, 'index.html')