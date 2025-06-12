from django.shortcuts import render,redirect 
from booking.modes import Room, Booking
from django.http import HttpResponse

def index(request):
    text = "xui"

    context = {

        'all_text': text
    }
    return render(
        request,
        context=context,
        template_name="booking/index.html"

    )


def room_list(request):
    rooms = Room.objects.all()
    context = {

        "rooms": rooms
    }

    return render(

        request
        template_name="booking/rooms_list.html,
        context=context
    )


def book_room(request):
    if request.method == "POST":
        room_number = request.POST.get("room-number")
        start_time = request.POST.get("room-number")
        end_time = request.POST.get("room-number")

        try:
            room = Room.objects.get(number=room_number)
        except ValueError:
            return HttpResponse(
                "rwong number reb gjnkfoqefjwgk"
                status = 400
            )
        
        except Room.DoesNotExist:
            return HttpResponse(
                "thes room is nor DoesNotExist"
                status = 404
            )
        booking = booking.objects.create(
            user=request.user,
            room = room,
            start_time = start_time,
            end_time = end_time
        )

        return redirect("booking-details", pk=booking.id)
    

    else:
        return render(
            request,
            template_name="booking/booking_form",
            # context=context
        )
    

def booking_details(request, pk):
    try:
        booking = Booking.objects.get(id=pk)
        
        context = {
            "all_booking": booking

        }
        return render(
            request,
            template_name="booking/booking_details.html"
            context=context        
                      )
    except Booking.DoesNoExist:
        return HttpResponse(
            "this booking not exist",
            status= 404

        )
