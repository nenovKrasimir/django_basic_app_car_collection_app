from django.shortcuts import render, redirect

from django_basic_app_car_collection_app.car_collection.forms import CreateProfileForm, CreateCarForm, EditCarForm, \
    DeleteCarForm
from django_basic_app_car_collection_app.car_collection.models import Profile, Car


# Create your views here.


def home_page(request):
    user = Profile.objects.first()
    context = {'user': user}
    return render(request=request, template_name='index.html', context=context)


def create_profile(request):
    form = CreateProfileForm(request.POST or None)
    context = {'form': form}

    if request.method == 'GET':
        return render(request=request, template_name='profile-create.html', context=context)

    if form.is_valid():
        form.save()
        return redirect('catalogue')


def catalogue(request):
    cars = Car.objects.all()
    context = {'cars': cars}
    return render(request=request, template_name='catalogue.html', context=context)


def details_profile(request):
    pass


def edit_profile(request):
    pass


def delete_profile(request):
    pass


def create_car(request):
    form = CreateCarForm(request.POST or None)
    context = {'form': form}

    if form.is_valid():
        form.save()
        return redirect('catalogue')

    return render(request=request, template_name='car-create.html', context=context)


def details_car(request, pk):
    car = Car.objects.first()
    context = {'car': car}

    return render(request=request, template_name='car-details.html', context=context)


def edit_car(request, pk):
    car = Car.objects.first()
    form = EditCarForm(request.POST or None, instance=car)
    context = {'car': car, 'form': form}

    if form.is_valid():
        form.save()
        return redirect('catalogue')

    return render(request=request, template_name='car-edit.html', context=context)


def delete_car(request, pk):
    car = Car.objects.first()
    form = DeleteCarForm(request.POST or None, instance=car)
    context = {'car': car}

    if form.is_valid():
        car.delete()
        return redirect('catalogue')

    return render(request=request, template_name='car-delete.html', context=context)
