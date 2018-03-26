from __future__ import unicode_literals
from ..log_reg.models import User
from django.contrib import messages
from django.shortcuts import render, HttpResponse, redirect   
from models import *

def main(request):
    print "**********MAIN************"
    if 'user_id' not in request.session:
        return redirect ('/main')
    else:
        me = User.objects.get(id=request.session['user_id'])
        all_quotes = Quote.objects.exclude(favorite=me).order_by('-created_at')
        my_fav = Quote.objects.filter(favorite=me)
        context = {
            'user' : me,
            'all_quotes' : all_quotes,
            'my_fav' : my_fav
        }
        return render(request, 'main_templates/index.html', context)

def favorite(request, item_id):
    if 'user_id' not in request.session:
        return redirect ('/main')
    quote = Quote.objects.get(id=item_id)
    print quote
    user = User.objects.get(id=request.session['user_id'])
    print user
    quote.favorite.add(user)
    print quote.favorite.add(user)
    return redirect('/quotes')

def remove(request, item_id):
    if 'user_id' not in request.session:
        return redirect ('/main')
    user = User.objects.get(id=request.session['user_id'])
    quote = Quote.objects.get(id=item_id)
    quote.favorite.remove(user)
    return redirect('/quotes')

def create(request):
    if 'user_id' not in request.session:
        return redirect ('/main')
    errors = []
    if len(request.POST['quoted_by']) < 3:
        errors.append("Quoted By needs to be longer than 3 characters")
    if len(request.POST['message']) < 10:        
        errors.append("Message needs to be longer than 10 characters")
    if len(errors):
        for error in errors:
            messages.error(request, error)
            return redirect('/quotes')
    else:
        user = User.objects.get(id=request.session['user_id'])
        created_quote = Quote.objects.create(
            quoted_by=request.POST['quoted_by'],
            message=request.POST['message'],
            creator=user)
        return redirect ('/quotes')

def user(request, item_id):
    user = User.objects.get(id=item_id)
    quote = Quote.objects.filter(creator=item_id)
    count = Quote.objects.filter(creator=item_id).count()
    context ={
        'user' : user,
        'quote' : quote,
        'count' : count
    }
    return render(request, 'main_templates/user.html', context)
    