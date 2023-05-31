from .payment import Payments

def payments(request):
    return { 'payments': Payments(request) }