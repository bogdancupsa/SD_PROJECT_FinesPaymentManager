class Payments():
    def __init__(self, request):
        self.session = request.session
        payments = self.session.get('skey')
        if 'skey' not in request.session:
            payments = self.session['skey'] = {'number': 111}
        self.payments = payments

    def get_absolute_url(self):
        return '/payments/summary'

    def add(self, product, qty):
        fine_id = fine.id

        if product_id not in self.payments:
            self.payments[fine_id] = {'cost': fine.cost, 'qty': 1}

        self.session.modified = True

    def __len__(self):
        return 1

