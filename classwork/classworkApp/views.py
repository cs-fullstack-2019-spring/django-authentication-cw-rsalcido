from django.shortcuts import render
from django.http import HttpResponse
from.forms import CalTrackForm
from django.contrib.auth.models import User
# function for index path
def index(request):
    return render(request, 'classworkApp/index.html')

# function for callory tracker
def CalTrack(request):
    form = CalTrackForm(request.POST or None)
    context = {
        "form": form
    }

 # new user function for new entries
def newuser(request):
    form =CalTrackForm(request.POST or None)
    context = {
        "form": form
    }
    return render(request, "classworkApp/newuser.html",context)
# function for last page verification for entry created
def verifieduser(request):
    User.objects.create_user(request.POST['Username'], request.POST["Calories"],request.POST["Date"]),
    return render(request, "classworkApp/verifieduser.html")

