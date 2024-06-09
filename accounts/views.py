import email
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render

from .models import User

from .forms import UserForm

# Create your views here.


def registerUser(request):
    if request.method == 'POST':
        form =  UserForm(request.POST)
        if form.is_valid():
            # create the user using the form
            # password = form.cleaned_data['password']
            #user = form.save(commit=False)
            #user.role = User.CUSTOMER
            #user.save()
            
            # create the user using create_user method
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password)
            user.role = User.CUSTOMER
            user.save()
            messages.success(request, 'your account has been registered sucessfull!')
            return redirect('registerUser')
        else:
            print('invaild form')
            print(form.errors)
    else:
        form  = UserForm
    context = {
        'form': form
    }
    return render(request, 'accounts/resgisterUser.html', context)