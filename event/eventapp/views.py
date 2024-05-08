from django.shortcuts import render, redirect

from eventapp.models import Event

from eventapp.forms import BookingForm


# Create your views here.

def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def events(request):
    eve = Event.objects.all()
    return render(request, 'events.html', {'eve': eve})


def booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('eventapp:home')

    form = BookingForm()
    return render(request, 'booking.html', {'form': form})


def contacts(request):
    return render(request, 'contacts.html')
