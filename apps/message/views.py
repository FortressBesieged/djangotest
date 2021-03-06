# coding:utf-8
from django.shortcuts import render
from .models import UserMessage

def getform(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        message = request.POST.get('message', '')
        address = request.POST.get('address', '')
        email = request.POST.get('email', '')

        user_messge = UserMessage()
        user_messge.name = name
        user_messge.message = message
        user_messge.address = address
        user_messge.email = email

        user_messge.save()

    message = None
    all_message = UserMessage.objects.filter(name='test2')

    if all_message:
        message = all_message[0]

    return render(request, 'message_form.html', {"my_message" : message})