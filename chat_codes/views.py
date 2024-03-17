from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render
from datetime import datetime
from .models import *
from ipware import get_client_ip


# Create your views here.

# front views
def index(request):
    ip_client, _ = get_client_ip(request)
    room, _ = ChatRoom.objects.get_or_create(user=request.user, ip_client=ip_client)
    chats = ChatMessage.objects.filter(room_id=room.pk)
    return render(request, 'index.html', {'room': room, 'chats': chats})


def add_message(request):
    # This function creates a new chat, it creates a chat room and the first message
    if request.method == 'POST':
        message = request.POST.get('message')  # It gets the message
        ip_client, _ = get_client_ip(request)  # get ip client
        room, _ = ChatRoom.objects.get_or_create(user=request.user, ip_client=ip_client)
        chat_message = ChatMessage.objects.create(room_id=room.pk, text=message,
                                                  type='client',
                                                  date=str(datetime.now())[10:19])  # Creating a message model
        data = serializers.serialize('json', [chat_message])
        return JsonResponse({'data': data})


def update_message(request):
    # This function creates a new chat, it creates a chat room and the first message
    if request.method == 'POST':
        ip_client, _ = get_client_ip(request)
        chatroom = ChatRoom.objects.get(ip_client=ip_client,
                                        user=request.user)  # get a room with ip_client=ip_client  user=request.user
        messages = ChatMessage.objects.filter(room_id=chatroom.pk, status=False, type='admin')  # Get messages
        for i in messages:
            i.status = True
            i.save()
        data = serializers.serialize('json', messages)  # Convert message models to json file
        return JsonResponse({'data': data})


# panel views


def panel_index(request):
    rooms = ChatRoom.objects.order_by('date')
    chats = ChatMessage.objects.all()
    return render(request, 'panel_index.html', {'chats': chats, 'rooms': rooms})


def panel_add_message(request):
    # This function for answer messages
    if request.method == 'POST':
        room_id = request.POST.get('room_id')
        message = request.POST.get('message')
        chat_message = ChatMessage.objects.create(room_id=room_id, status=False, text=message,
                                                  date=str(datetime.now())[10:19],
                                                  type='admin')
        data = serializers.serialize('json', [chat_message, ])  # Convert message models to json file
        return JsonResponse({'data': data})


def panel_update_message(request):
    # for update rooms
    if request.method == 'POST':
        ip_client, _ = get_client_ip(request)
        messages = ChatMessage.objects.filter(status=False, type='client')  # Get messages
        for i in messages:
            i.status = True
            i.save()
        data = serializers.serialize('json', messages)  # Convert message models to json file
        return JsonResponse({'data': data})
