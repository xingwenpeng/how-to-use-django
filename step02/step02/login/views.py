from django.shortcuts import render
from django.shortcuts import render_to_response
from django import forms
from login.models import user_register
from django.http import HttpResponse

# Create your views here.

class ContactForm(forms.Form):
    user_name = forms.CharField(max_length=100, label='用户名')
    user_email = forms.EmailField(label='Email')
    user_passwd = forms.CharField(widget=forms.TextInput(attrs={'type':'password'}), label='密码')
    #user_passwd = forms.CharField()


def register(request):
    if request.method == 'POST':
        form = ContactForm(request.POST);
        if form.is_valid():
            persion = form.cleaned_data
            name = persion['user_name']
            password = persion['user_passwd']
            email = persion['user_email']
            user = user_register(user_name=name, user_passwd=password, user_email=email);
            user.save()
            return HttpResponse('ok')
        else :
            return HttpResponse('form err')
    else :
        form = ContactForm();
    return render_to_response('login.html', {'form': form})
            

