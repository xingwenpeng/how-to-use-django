from django.shortcuts import render
from django.shortcuts import render_to_response

# Create your views here.

def register(req):
    return render_to_response("login.html")

