from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .models import Table, Reservation
from .forms import ReservationForm
from datetime import date, timedelta

def index(request):
    selected_date = request.GET.get('date')
    if not selected_date:
        selected_date = date.today().isoformat()
    tables = Table.objects.all()
    reservations = Reservation.objects.filter(date=selected_date).values_list('table', flat=True)
    form = ReservationForm(initial={'date': selected_date})
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save()
            send_mail(
                'Замовлення столика',
                f'Ви успішно замовили столик {reservation.table} на {reservation.date}',
                'your-email@example.com',
                [reservation.email],
                fail_silently=True,
            )
            return redirect('index')
    context = {
        'selected_date': selected_date,
        'previous_date': (date.fromisoformat(selected_date) - timedelta(days=1)).isoformat(),
        'next_date': (date.fromisoformat(selected_date) + timedelta(days=1)).isoformat(),
        'today': date.today().isoformat(),
        'tables': tables,
        'reservations': reservations,
        'form': form,
    }
    return render(request, 'index.html', context)