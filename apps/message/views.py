# coding:utf-8
from django.shortcuts import render


def getform(request):
    return render(request, 'message_form.html')