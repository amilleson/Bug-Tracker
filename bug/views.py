from django.shortcuts import render, redirect
from .models import User, UserManager, Ticket, TicketManager
from django.contrib import messages
import bcrypt

def index(request):
    return render(request, 'index.html')

def new_ticket(request):
    context = {
        'user' : User.objects.get(id = request.session['userid'])
    }
    return render(request, 'new_ticket.html', context)

def edit_ticket(request, id):
    context = {
        'user' : User.objects.get(id = request.session['userid']),
        'ticket' : Ticket.objects.get(id = id)
    }
    return render(request, 'edit_ticket.html', context)

def dashboard(request):
    context = {
        'user' : User.objects.get(id = request.session['userid']),
        'ticket' : Ticket.objects.filter(creator = request.session['userid']),
    }
    return render(request, 'dashboard.html', context)

def create(request):
    errors = Ticket.objects.ticket_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/new_ticket')
    else:
        Ticket.objects.create(name = request.POST['ticket_name'], app = request.POST['app'], description = request.POST['description'], creator = User.objects.get(id = request.session['userid']))
        return redirect('/dashboard')

def admin(request):
    context = {
        'user' : User.objects.get(id = request.session['userid']),
        'ticket' : Ticket.objects.all(),
    }
    return render(request, 'admin.html', context)

def delete_trip(request, id):
    delete = Ticket.objects.get(id = id)
    delete.delete()
    return redirect('/dashboard')

def edit(request, id):
    print(request.POST)
    edit = Ticket.objects.get(id = id)
    edit.name = request.POST['ticket_name']
    edit.app = request.POST['app']
    edit.description = request.POST['description']
    edit.save()
    return redirect('/dashboard')

def edit2(request, id):
    edit = Ticket.objects.get(id = id)
    edit.action_phase = 2
    edit.save()
    return redirect('/admin')

def edit3(request, id):
    edit = Ticket.objects.get(id = id)
    edit.action_phase = 3
    edit.save()
    return redirect('/admin')

def vote(request, id):
    ticket = Ticket.objects.get(id = id)
    ticket.vote+1
    return redirect('/dashboard')





def register(request):
    password = request.POST['password']
    pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    errors = User.objects.validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        user = User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'], password = pw_hash)
        request.session['userid'] = user.id
        return redirect('/dashboard')

def login(request):
    user = User.objects.filter(email=request.POST['email'])
    if user:
        logged_user = user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session['userid'] = logged_user.id
            print('*'*500, logged_user.first_name)
            if logged_user.admin == 1:
                return redirect('/admin')
            return redirect('/dashboard')
    else:
        print('*'*500, 'email/password incorrect')
        messages.error(request, "Email/password incorrect.")

    return redirect("/")

def logout(request):
    request.session.clear()
    return redirect('/')