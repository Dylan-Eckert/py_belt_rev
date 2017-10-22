# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *

# Create your views here.
# ===================================================
#                      RENDER
# ===================================================

def index(req):
    return render(req, 'login_registration/index.html')

# ===================================================
#                    PROCESSES
# ===================================================
def login(req):
    user = User.objects.login(req.POST)
    if user:
        req.session['user_id'] = user.id
        return redirect('/book_reviews')

    messages.error(req, 'Email or Password invalid')
    return redirect('/')

def registration(req):
    res = User.objects.userIsValid(req.POST)
    if res['status']:
        user = User.objects.newUser(req.POST)
        req.session['user_id'] = user.id
        return redirect('/book_reviews')
    else:
        for error in res['errors']:
            messages.error(req, error)

    return redirect('/')

def logout(req):
    req.session.clear()

    return redirect('/')
