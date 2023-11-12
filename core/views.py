from functools import reduce

from django.core import paginator
from django.db.models import Q
from django.shortcuts import render

from core.models import Person


def index(request):
    return render(request, 'core/index.html')


def search(request):
    records = None

    fetch = Person.objects.all()

    if query := request.GET.get('q'):
        filters = [Q(first_name__icontains=term) | Q(last_name__icontains=term)
                   for term in query.lower().split()]

        fetch = fetch.filter(reduce(lambda x, y: x | y, filters))

        page = request.GET.get('page', '')
        page = int(page) if page.isdigit() else 1

        chunk = 50

        records = paginator.Paginator(fetch.order_by('id'), chunk).page(page)

    return render(request, 'core/parts/results.html', {'records': records})
