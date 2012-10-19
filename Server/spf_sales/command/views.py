# Create your views here.
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from order.models import Order, OrderForm
from django.utils import timezone

def command(request):
        if request.method == 'POST':
            form = OrderForm(request.POST)
            if form.is_valid():
                _command  =   form.cleaned_data['command']

                command = Command(command=_command, statusTimeStamp=timezone.now(), status='queued', commandTimeStamp=timezone.now())
                command.save()

                return HttpResponse("thank you!")
            
            
