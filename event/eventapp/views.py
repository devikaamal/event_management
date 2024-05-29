from django.shortcuts import render, redirect

from eventapp.models import Event

from eventapp.forms import BookingForm

from eventapp.models import Booking


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


def list_booking(request):
    l = Booking.objects.all().order_by('booking_date')
    f = BookingForm()
    return render(request, 'list.html', {'l': l, 'f': f})


def update(request, p):
    b = Booking.objects.get(id=p)
    if request.method == "POST":
        form = BookingForm(request.POST, instance=b)
        if form.is_valid():
            form.save()
            return list_booking(request)

    form = BookingForm(instance=b)
    return render(request, 'update.html', {'form': form})


def delete(request, p):
    e = Booking.objects.get(id=p)
    e.delete()
    return list_booking(request)
