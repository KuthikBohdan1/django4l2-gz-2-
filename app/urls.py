
# from django.urls import path, include

# from . import views

# urlpatterns = [
#     path()
# ]

from django.urls import path
from app import views

urlpatterns = [
    path("", views.index, name="index"),
    path("room", views.room_list, name="rooms_list"),
    path("book-room/", views.book_room, name="book-room"),
    path("booking-details/<int:pk>", views.booking_details, name="rooms_list"),
    
    

]
