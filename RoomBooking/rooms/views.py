from django.shortcuts import render, redirect
from .models import Room, Building, ReservingPerson, Reservation
from .forms import BuildingForm, RoomForm, ReservingPersonForm, ReservationForm


# Create your views here.


def rooms(request):
    all_rooms = Room.objects.distinct()
    context = {'rooms': all_rooms}
    return render(request, 'rooms/rooms.html', context)


def room(request, pk):
    room_obj = Room.objects.get(id=pk)
    reservations = Reservation.objects.filter(room=room_obj)
    context = {'room': room_obj, 'reservations': reservations}
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


def reservingPerson(request, pk):
    reserving_person_obj = ReservingPerson.objects.get(id=pk)
    context = {'reserving_person': reserving_person_obj}
    return render(request, 'rooms/reserving_person_view.html', context)


def reservingPersons(request):
    all_reserving_persons = ReservingPerson.objects.distinct()
    context = {'reserving_persons': all_reserving_persons}
    return render(request, 'rooms/reserving_persons.html', context)


def createReservingPerson(request):
    form = ReservingPersonForm()
    if request.method == 'POST':
        form = ReservingPersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reserving-persons')
    context = {'form': form}
    return render(request, 'rooms/reserving_person_form.html', context)


def deleteReservingPerson(request, pk):
    reserving_person_to_delete = ReservingPerson.objects.get(id=pk)
    if request.method == 'POST':
        reserving_person_to_delete.delete()
        return redirect('reserving-persons')
    context = {'object': reserving_person_to_delete, 'redirection': 'reserving-persons'}
    return render(request, 'rooms/delete_template.html', context=context)


def reservation(request, pk):
    reservation_obj = Reservation.objects.get(id=pk)
    context = {'reservation': reservation_obj}
    return render(request, 'rooms/reservation_view.html', context)


def reservations(request):
    all_reservations = Reservation.objects.distinct()
    context = {'reservations': all_reservations}
    return render(request, 'rooms/reservations.html', context)


def createReservation(request):
    form = ReservationForm()
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reservations')
    context = {'form': form}
    return render(request, 'rooms/reservation_form.html', context)


def deleteReservation(request, pk):
    reservation_to_delete = Reservation.objects.get(id=pk)
    if request.method == 'POST':
        reservation_to_delete.delete()
        return redirect('reservations')
    context = {'object': reservation_to_delete, 'redirection': 'reservations'}
    return render(request, 'rooms/delete_template.html', context=context)


def updateReservation(request, pk):
    reservation_obj = Reservation.objects.get(id=pk)
    form = ReservationForm(instance=reservation_obj)
    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=reservation_obj)
        if form.is_valid():
            form.save()
            return redirect('reservations')
    context = {'form': form}
    return render(request, 'rooms/reservation_form.html', context)
