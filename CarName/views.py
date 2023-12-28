from django.shortcuts import render, redirect
from .import forms,models

def add_car(request):
    if request.method == 'POST':
        car_form = forms.CarForm(request.POST)
        if car_form.is_valid():
            car_form.save()
            return redirect('add_car')
    else:
        car_form = forms.CarForm
    return render(request, 'car.html', {'form': car_form})

def edit_car(request,id):
    c=models.Car.objects.get(pk=id)
    car_form = forms.CarForm(instance=c)
    if request.method == 'POST':
        car_form = forms.CarForm(request.POST,instance=c)
        if car_form.is_valid():
            car_form.save()
            return redirect('home')
    return render(request, 'car.html', {'form': car_form})

def delete_car(request,id):
    c=models.Car.objects.get(pk=id)
    c.delete()
    return redirect('home')


