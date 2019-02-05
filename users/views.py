from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm

def register(request):
    if request.method == 'POST':
        print("POST")
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            print("VALID")
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome {username}! You can now log in with your new account.')
            return redirect('login')
    else:
        print("NOT")
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form':form})

