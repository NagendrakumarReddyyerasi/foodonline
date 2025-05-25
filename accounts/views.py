from django.shortcuts import render,HttpResponse, redirect
from .forms import UserForm
from .models import User
from django.contrib import messages

# Create your views here.
def registerUser(request):
    if request.method =='POST':
        print(request.POST)
        form = UserForm(request.POST)
        if form.is_valid():
            # password = form.cleaned_data['password']
            # user = form.save(commit=False)
            # user.set_password(password)
            # user.role = User.CUSTOMER
            # user.save()
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user=User.objects.create(first_name=first_name, last_name=last_name, email=email, username=username, password=password)
            user.role = User.CUSTOMER
            user.save()
            messages.success(request, 'Your account has been registered sucessfully!')
            return redirect('registerUser')
        else:
            print("invalid error")
            print(form.errors)
    else:
        form =UserForm()
    context = {
        'form' : form,
    }
    return render(request, 'accounts/registerUser.html',context)