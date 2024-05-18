from django.shortcuts import render, HttpResponse,redirect
from . import converters
from django.contrib import messages

def index(request):
    return render(request, 'home.html')


def convert(request):
    if request.method == 'GET':
        return render(request, 'convert.html' )



def withdraw(request):
    if request.method == 'POST':
        try:
            amount = request.POST['amount']
            currency = request.POST['currency']
            currency_to_exchange = request.POST['currency_to_exchange']
            withdraw = request.POST['withdraw']

            received_money = float(amount) * converters.CURRENCY[currency][currency_to_exchange]

            if withdraw == 'true':
                comission = received_money * 0.01
                received_money -= comission

            context = {
                'amount': amount, 
                'currency': currency, 
                'currency_to_exchange': currency_to_exchange, 
                'received_money': received_money,
                'withdraw': withdraw,
            }
            return render(request, 'withdraw.html',context)

        except KeyError :
            messages.error(request, "You must choose currency to continue ")
            return redirect('convert')
            

