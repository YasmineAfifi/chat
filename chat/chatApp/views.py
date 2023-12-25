from django.shortcuts import render
from .models import ChatRoom , Chat
# Create your views here.

def index(request):
    
    return render(request,'chatApp/index.html')

def Room(request):
    room = request.GET.get('room_name')
    search_room = ChatRoom.objects.filter(name=room)
    chats =[]
    if search_room:
        chats = Chat.objects.filter(room = room)
    else:
        room = ChatRoom(name=room)
        room.save()
    
    return render(request,'chatApp/chatRooms.html',{'room':room,'chats':chats})