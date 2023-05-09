from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .models import Ticket

@csrf_exempt
def home(request):
    return render(request, 'home/index.html')

@csrf_exempt
def buy_tickets(request):
    return render(request, 'form/index.html')

@csrf_exempt
def show_ticket(request):
    new_ticket = Ticket()
    new_ticket.name = request.POST.get('name')
    new_ticket.last_name = request.POST.get('last_name')
    new_ticket.years_old = request.POST.get('years_old')
    new_ticket.email = request.POST.get('email')
    new_ticket.cpf = request.POST.get('cpf')
    new_ticket.card_number = request.POST.get('card_number')
    new_ticket.cvv = request.POST.get('cvv')
    new_ticket.save()

    tickets = {
        'tickets': Ticket.objects.all()
    }
    return render(request, 'data/index.html', tickets)
