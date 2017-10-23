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
    authors = Author.objects.all()
    data = {
    'books': books,
    'authors': authors
    }

    return render(req, 'book_reviewer/books.html', data)

def addBook(req):
    if 'user_id' not in req.session:
        return redirect('/')
    res = User.objects.bookIsValid(req.POST)
    if res['status']:
        book = Book.objects.newBook(req.POST)
        return redirect('/book_reviews')
    else:
        for error in res['errors']:
            messages.error(req, error)

    return redirect('/')
