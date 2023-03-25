from django.shortcuts import render, get_object_or_404
from .models import Car, CarGallery
from user_auth import forms

# Create your views here.
def gallery(request):
    """Creates a gallery view
    
    :param obj request: Object containing metadata
    
    :returns: List of car objects
    
    :rtype: list
    """
    # if user is logged in, display full gallery
    # else only display first 3 pictures in the gallery
    if request.user.is_authenticated:
        car_list = Car.objects.all()
    else:
        car_list = Car.objects.order_by('-production_year')[:3]
        
    context = {
        'car_list': car_list,
    }
    return render(request, 'gallery.html', context)

def detail(request, car_id):
    car = get_object_or_404(Car, pk=car_id)
    context = {
        'car': car,
    }
    return render(request, 'detail.html', context)

def about(request):
    return render(request, 'about.html')





























