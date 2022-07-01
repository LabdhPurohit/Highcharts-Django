import json

from django.db.models import Count, Q
from django.shortcuts import render
from django.http import JsonResponse

from .models import Passenger

def ticket_class_view(request):
    dataset = Passenger.objects \
        .values('Pclass') \
        .annotate(survived_count=Count('Pclass', filter=Q(survived=True)),
                  not_survived_count=Count('Pclass', filter=Q(survived=False))) \
        .order_by('Pclass')
    return render(request, 'charts/index.html', {'dataset': dataset})
