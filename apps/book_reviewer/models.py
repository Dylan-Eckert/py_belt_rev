# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..login_registration.models import User

# Create your models here.
class BookManager(models.Manager):

    def reviewIsValid(self, post):
        title = post['title'].lower()
        author = post['author'].lower()
        review = post['review']
        rating = post['rating']

        errors = []
        if len(title) < 2 :
             errors.append('Please enter a valid title')
        if len(author) < 2:
             errors.append('Please enter a valid author')
        # do all the email stuff like REGEX and shit IN THIS IF STATEMENT BELOW!!!!
        if len(review) < 10 or len(review) > 500:
             errors.append('Review has to be between 10-500 characters')
        if not errors:
            review_author = self.filter(author=author)
            if review_author:
                errors.append('Author already exists!')
            review_book = self.filter(book=book)
            if review_book:
                errors.append('Book already exists!')

        return {'status': len(errors) == 0, 'errors':errors}

    def bookIsValid(self, post):
        title= post['title'].lower()
        author= post['author'].lower()

        errors = []
        if len(title) < 2 :
             errors.append('Please enter a valid title')
        if len(author) < 2:
             errors.append('Please enter a valid author')

        return {'status': len(errors) == 0, 'errors':errors}

    def newBook(self, post):
        title = post['title'].lower()
        author = post['author'].lower()

        return self.create(title=title, author=author)

    def newAuthor(self, post):
        name = post['name'].lower()

        return self.create(name=name)


class Book(models.Model):
    title = models.CharField(max_length=100)

    objects = BookManager()

    def __str__(self):
        return "title: {}".format(self.title)

class Author(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book, related_name="authors")

    objects = BookManager()

    def __str__(self):
        return "name: {}".format(self.name)

class Review(models.Model):
    content = models.TextField()
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
    user = models.ForeignKey(User, related_name="user_reviews")
    book = models.ForeignKey(Book, related_name="book_reviews")

    objects = BookManager()
