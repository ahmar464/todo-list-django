from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm  # our custom form with email

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # log in right after registration
            return redirect('task_list')  # redirect to your tasks list
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})
