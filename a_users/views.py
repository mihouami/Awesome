from django.shortcuts import render, redirect
from .models import *
from .forms import *

def profile_view(request):
    profile = request.user.profile
    return render(request, 'a_users/profile.html', {'profile' : profile})

def profile_edit_view(request):
    form = ProfileEditForm(request.POST or None, request.FILES or None, instance=request.user.profile)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('profile')
    return render(request, 'a_users/profile_edit.html', {'form' : form})
