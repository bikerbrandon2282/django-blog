from django.shortcuts import get_object_or_404, render
from .models import Aboutme
# Create your views here.

def about_view(request, slug):
    queryset = Aboutme.objects.all(order_by='-updated_on').first()
    about = get_object_or_404(queryset, slug=slug)
    return render(request, 'about/about.html', {'about': about})
