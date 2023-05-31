from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

from .payment import Payments
from police.models import Fine

def payments_summary(request):
    return render(request, 'police/payments/summary.html')

def payments_add(request):
    payments = Payments(request)
    if request.POST.get('action') == 'post':
        fine_id = int(request.POST.get('fineid'))
        fine = get_object_or_404(Fine, id=fine_id)
        payments.add(fine=fine)
        response = JsonResponse({'test':'data'})
        return response