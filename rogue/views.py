from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from rogue.forms import BookingForm, LoginForm
from rogue.models import Bicycle


# Create your views here.
def home(request):
    return render(request, "index.html")


def services(request):
    return render(request, "services.html")


def contact(request):
    return render(request, "contact.html")


@login_required
def book_bicycle(request, bicycle_id):
    bicycle = Bicycle.objects.get(pk=bicycle_id)

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.bicycle = bicycle
            booking.save()
            bicycle.is_available = False
            bicycle.save()
            return redirect('home')
    else:
        form = BookingForm()

    return render(request, 'book_bicycle.html', {'form': form, 'bicycle': bicycle})


@login_required
def return_bicycle(request, booking_id):
    booking = Booking.objects.get(pk=booking_id)

    if request.method == 'POST':
        booking.return_date = request.POST['return_date']
        booking.bicycle.is_available = True
        booking.save()
        booking.bicycle.save()
        return redirect('home')

    return render(request, 'return_bicycle.html', {'booking': booking})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['username'] == 'user' and form.cleaned_data['password'] == 'password':
                return redirect('success')
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def faq(request):
    return render(request, 'faq.html')