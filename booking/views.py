from django.shortcuts import render, get_object_or_404

from booking.models import Room, Booking


# Create your views here.
def main_page(request):
    rooms = Room.objects.all()

    context = {
        "data": "куку",
        'room_list': rooms
    }

    return render(request, "booking/room_list.html", context) 


def booking_page(request):
    room = get_object_or_404(Room, id=room_id)

    contex = {
        'room': room
    }

    
