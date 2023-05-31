from django.shortcuts import render, get_object_or_404
from .models import Category, Fine

# Create your views here.
def all_fines(request):
    fines = Fine.objects.all()
    return render(request, 'police/home.html', {'fines': fines})

def categories(request):
    return {'categories': Category.objects.all()}

def fine_detail(request, slug):
    fine = get_object_or_404(Fine, slug=slug)
    return render(request, 'police/fines/fine_page.html', {'fine': fine})

def category_list(request, category_slug):
    category = get_object_or_404(Category, slug = category_slug)
    fines = Fine.objects.filter(category = category)
    return render(request, 'police/fines/category.html', {'category': category, 'fines': fines})