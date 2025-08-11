from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.core.mail import send_mail
from django.conf import settings

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            send_mail(
                'Welcome to ToDo App',
                'Thanks for signing up! Start adding your tasks now.',
                settings.DEFAULT_FROM_EMAIL,
                [user.email],
                fail_silently=False,
            )
            return redirect('task_list')  # Adjust this to your task list view name
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})
