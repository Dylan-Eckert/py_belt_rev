# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages
from ..login_registration.models import User
from .models import *

# Create your views here.
def index(req):
    if 'user_id' not in req.session:
        return redirect('/')

    users = User.objects.all()
    data = {'users': users}

    return render(req, 'book_reviewer/home.html', data)

def books(req):
    if 'user_id' not in req.session:
        return redirect('/')

    books = Book.objects.all()
    data = {'books': books}

    return render(req, 'book_reviewer/books.html', data)
