from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect   
from django.contrib import messages
from models import User
	
def index(request):     
	return render(request, 'logReg_templates/login_reg.html') 

def register(request):
  results = User.objects.register_validation(request.POST)

  if results[0]:
    request.session['user_id'] = results[1].id
    print "******* You registered! ******"
    return redirect('/quotes')
  
  else:
    for err in results[1]:
      messages.error(request, err)
    return redirect('/main')

def login(request):
  results = User.objects.login_validation(request.POST)

  if results[0]:
    request.session['user_id'] = results[1].id 
    print "******* logged in yo! ******"
    return redirect('/quotes')
  else:
    for err in results[1]:
      messages.error(request, err)
  return redirect('/main')

def logout(request):
  request.session.flush()
  print "++++++++ You logged out ++++++++++"
  return redirect('/main')
