from django.db.models import Q
from django.shortcuts import render

from eventapp.models import Event


# Create your views here.

def search(request):
    query = ""
    e = None
    if (request.method == "POST"):
        query = request.POST['q']
        if query:
            e = Event.objects.filter(Q(name__icontains=query) | Q(desc__icontains=query))
    return render(request, 'search.html', {'query': query, 'e': e})
