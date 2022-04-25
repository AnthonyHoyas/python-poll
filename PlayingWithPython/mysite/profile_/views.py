from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


@login_required
def profile(request):
    return render(request, 'profile.html')

