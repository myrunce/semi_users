# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import *
from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return redirect('/users')

def users(request):
    context = {
        'users': user.objects.all()
    }
    return render(request, 'semi_users_app/users.html', context)

def new_user(request):
    return render(request, 'semi_users_app/new.html')

def create(request):
    user.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'])
    return redirect('/users')

def edit(request, user_id):
    context = {
        'the_user': user.objects.get(id = user_id)
    }
    return render(request, 'semi_users_app/edit.html', context)

def show(request, user_id):
    if request.method == 'POST':
        the_user = user.objects.get(id = user_id)
        the_user.first_name = request.POST['first_name']
        the_user.last_name = request.POST['last_name']
        the_user.email = request.POST['email']
        the_user.save()
        return redirect('/users')
    else:
        context = {
            'the_user': user.objects.get(id = user_id)
        }
        return render(request, 'semi_users_app/info.html', context)

def delete(request, user_id):
    user.objects.get(id = user_id).delete()
    return redirect('/users')
