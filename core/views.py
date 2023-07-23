from django.shortcuts import render

from core import services


def index(request):
    return render(request, 'core/index.html')


def search(request):
    records = None

    if query := request.GET.get('q'):
        page = request.GET.get('page', '')
        page = int(page) if page.isdigit() else 1

        chunk = 3
        skip = (page - 1) * chunk

        records = services.fetch(query)[skip:skip + chunk]

    return render(request, 'core/parts/results.html', {'records': records})
