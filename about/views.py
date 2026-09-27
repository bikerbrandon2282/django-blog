from django.shortcuts import render
from .models import Aboutme
# Create your views here.

def about_view(request):
    about = Aboutme.objects.all(order_by='-updated_on').first()

    return render(request, 'about/about.html', {'about': about})
