from django.shortcuts import redirect, render
from .models import ChatRoom , Chat
# Create your views here.








def index(request):
    
    return render(request,'chatApp/index.html')

def Room(request,room_name):
        
        try:
            search_room = ChatRoom.objects.get(name=room_name)
            print('search_room')
            print(search_room)
            print('search_room')
            chats =[]
        except ChatRoom.DoesNotExist:
                search_room = ChatRoom(name=room_name)
                search_room.save()
        chats = Chat.objects.filter(room = search_room)
        print('chats')
        print(chats)
        print('chats')
        return render(request,'chatApp/chatRooms.html',{'room':room_name,'chats':chats})



