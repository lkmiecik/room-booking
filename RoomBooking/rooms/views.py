from django.shortcuts import render, redirect
from .models import Room, Building
from django.contrib.auth.models import User
from .forms import BuildingForm

# Create your views here.


def rooms(request):
    all_rooms = Room.objects.distinct()
    all_users = User.objects.distinct()
    context = {'rooms': all_rooms, 'users': all_users}
    return render(request, 'rooms/rooms.html', context)


def buildings(request):
    print("BUILDINGS")
    all_buildings = Building.objects.distinct()
    print(len(all_buildings))
    context = {'buildings': all_buildings}
    return render(request, 'rooms/buildings.html', context)

def createBuilding(request):
    form = BuildingForm()
    if request.method == 'POST':
        form = BuildingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('buildings')
    context = {'form': form}
    return render(request, 'rooms/building_form.html', context)


def updateBuilding(request, pk):
    building_obj = Building.objects.get(id=pk)
    form = BuildingForm(instance=building_obj)
    if request.method == 'POST':
        form = BuildingForm(request.POST, instance=building_obj)
        if form.is_valid():
            form.save()
            return redirect('buildings')
    context = {'form': form}
    return render(request, 'rooms/building_form.html', context)


def deleteBuilding(request, pk):
    building_to_delete = Building.objects.get(id=pk)
    if request.method == 'POST':
        building_to_delete.delete()
        return redirect('buildings')
    context = {'object': building_to_delete}
    return render(request, 'rooms/delete_template.html', context=context)


def building(request, pk):
    building_obj = Building.objects.get(id=pk)
    context = {'building': building_obj}
    return render(request, 'rooms/building_view.html', context)