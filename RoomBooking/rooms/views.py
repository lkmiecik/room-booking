from django.shortcuts import render, redirect
from .models import Room, Building, Reservation
from django.contrib.auth.models import User
from .forms import BuildingForm, RoomForm, ReservationForm


# Create your views here.
def reservations(request):
    all_res = Reservation.objects.distinct()
    context = {'reservations': all_res}
    return render(request, 'rooms/booked_rooms.html', context)

def bookRoom(request):
    form = ReservationForm
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('booked-rooms')
    context = {'form': form}

    return render(request, 'rooms/room_book.html', context)

def deleteReservation(request, pk):
    res_to_delete = Reservation.objects.get(id=pk)
    if request.method == 'POST':
        res_to_delete.delete()
        return redirect('booked-rooms')
    obj_str = f'Usunięto rezerwacje {res_to_delete.rezerwujacy}'
    context = {'object': obj_str, 'redirection': 'booked-rooms'}
    return render(request, 'rooms/delete_template.html', context=context)


def updateReservation(request, pk):
    res_obj = Reservation.objects.get(id=pk)
    form = ReservationForm(instance=res_obj)
    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=res_obj)
        if form.is_valid():
            form.save()
            return redirect('booked-rooms')
    context = {'form': form}
    return render(request, 'rooms/room_book.html', context)

def rooms(request):
    all_rooms = Room.objects.distinct()
    context = {'rooms': all_rooms}
    return render(request, 'rooms/rooms.html', context)


def room(request, pk):
    room_obj = Room.objects.get(id=pk)
    context = {'room': room_obj}
    return render(request, 'rooms/room_view.html', context)


def createRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('rooms')
    context = {'form': form}
    return render(request, 'rooms/room_form.html', context)


def updateRoom(request, pk):
    room_obj = Room.objects.get(id=pk)
    form = RoomForm(instance=room_obj)
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room_obj)
        if form.is_valid():
            form.save()
            return redirect('rooms')
    context = {'form': form}
    return render(request, 'rooms/room_form.html', context)


def deleteRoom(request, pk):
    room_to_delete = Room.objects.get(id=pk)
    if request.method == 'POST':
        room_to_delete.delete()
        return redirect('rooms')
    obj_str = f'Salę o numerze {room_to_delete.number}'
    context = {'object': obj_str, 'redirection': 'rooms'}
    return render(request, 'rooms/delete_template.html', context=context)


def buildings(request):
    all_buildings = Building.objects.distinct()
    context = {'buildings': all_buildings}
    return render(request, 'rooms/buildings.html', context)


def building(request, pk):
    building_obj = Building.objects.get(id=pk)
    context = {'building': building_obj}
    return render(request, 'rooms/building_view.html', context)


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
    context = {'object': building_to_delete, 'redirection': 'buildings'}
    return render(request, 'rooms/delete_template.html', context=context)

