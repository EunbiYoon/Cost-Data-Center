from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
@login_required(login_url='login_url')
def homeView(request):
    return render(request, 'quality_home.html')