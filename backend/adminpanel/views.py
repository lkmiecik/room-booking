from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect

from adminpanel.forms import RoomForm, BuildingForm
from reservation.models import Sala, Building, Wynajem


@permission_required('adminpanel')
@login_required
def home(request):
    return render(request, "adminpanel/home.html")


@permission_required('adminpanel')
@login_required
def rooms(request):
    all_rooms = Sala.objects.distinct()
    context = {'rooms': all_rooms}
    return render(request, 'adminpanel/rooms.html', context)


@permission_required('adminpanel ')
@login_required
def room(request, pk):
    room_obj = Sala.objects.get(id=pk)
    context = {'room': room_obj}
    return render(request, 'adminpanel/room_view.html', context)


@permission_required('adminpanel')
def createRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('rooms')
    context = {'form': form}
    return render(request, 'adminpanel/room_form.html', context)


@permission_required('adminpanel')
def updateRoom(request, pk):
    room_obj = Sala.objects.get(id=pk)
    form = RoomForm(instance=room_obj)
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room_obj)
        if form.is_valid():
            form.save()
            return redirect('rooms')
    context = {'form': form}
    return render(request, 'adminpanel/room_form.html', context)


@permission_required('adminpanel')
def deleteRoom(request, pk):
    room_to_delete = Sala.objects.get(id=pk)
    if request.method == 'POST':
        room_to_delete.delete()
        return redirect('rooms')
    obj_str = f'Salę o numerze {room_to_delete.nazwa_sali}'
    context = {'object': obj_str, 'redirection': 'rooms'}
    return render(request, 'adminpanel/delete_template.html', context=context)


@permission_required('adminpanel')
def buildings(request):
    all_buildings = Building.objects.distinct()
    context = {'buildings': all_buildings}
    return render(request, 'adminpanel/buildings.html', context)


@permission_required('adminpanel')
def building(request, pk):
    building_obj = Building.objects.get(id=pk)
    context = {'building': building_obj}
    return render(request, 'adminpanel/building_view.html', context)


@permission_required('adminpanel')
def createBuilding(request):
    form = BuildingForm()
    if request.method == 'POST':
        form = BuildingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('buildings')
    context = {'form': form}
    return render(request, 'adminpanel/building_form.html', context)


@permission_required('adminpanel')
def updateBuilding(request, pk):
    building_obj = Building.objects.get(id=pk)
    form = BuildingForm(instance=building_obj)
    if request.method == 'POST':
        form = BuildingForm(request.POST, instance=building_obj)
        if form.is_valid():
            form.save()
            return redirect('buildings')
    context = {'form': form}
    return render(request, 'adminpanel/building_form.html', context)


@permission_required('adminpanel')
def deleteBuilding(request, pk):
    building_to_delete = Building.objects.get(id=pk)
    if request.method == 'POST':
        building_to_delete.delete()
        return redirect('buildings')
    context = {'object': building_to_delete, 'redirection': 'buildings'}
    return render(request, 'adminpanel/delete_template.html', context=context)


@permission_required('adminpanel')
def reservations(request):
    all_reservations = Wynajem.objects.distinct()
    context = {'reservations': all_reservations}
    return render(request, 'adminpanel/reservations.html', context)


@permission_required('adminpanel')
def deleteReservation(request, pk):
    reservation_to_delete = Wynajem.objects.get(id=pk)
    if request.method == 'POST':
        reservation_to_delete.delete()
        return redirect('reservations')
    context = {'object': reservation_to_delete, 'redirection': 'reservations'}
    return render(request, 'adminpanel/delete_template.html', context=context)