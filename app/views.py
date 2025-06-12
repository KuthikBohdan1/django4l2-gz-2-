from django.shortcuts import render
# from booking.models import 
# Create your views here.

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