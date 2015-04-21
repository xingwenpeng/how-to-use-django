from django.shortcuts import render
from django.shortcuts import render_to_response
from django import forms
from login.models import user_register
from django.http import HttpResponse
from django.http import HttpResponseRedirect

# Create your views here.

class ContactForm(forms.Form):
    user_name = forms.CharField(max_length=100, label='用户名')
    user_email = forms.EmailField(label='Email')
    user_passwd = forms.CharField(widget=forms.TextInput(attrs={'type':'password'}), label='密码')
    #user_passwd = forms.CharField()

class PhotoForm(forms.Form):
    photo_path = forms.FileField(label='上传图片')
    #photo_name = forms.CharField(max_length=100, label='上传图片')

def register(request):
    if request.method == 'POST' :
        form = ContactForm(request.POST)
        if form.is_valid() :
            persion = form.cleaned_data
            name = persion['user_name']
            password = persion['user_passwd']
            email = persion['user_email']
            user = user_register(user_name=name, user_passwd=password, user_email=email);
            user.save()
            return HttpResponseRedirect('/login/upload')
        else :
            return HttpResponse('form err')
    else :
        form = ContactForm();
    return render_to_response('login.html', {'form': form})
            

def upload(request):
    user = {'name':'zhangsan'}
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data['photo_path'].name)
            print(form.cleaned_data['photo_path'].size)
            fp = open('./uploaddir/' + form.cleaned_data['photo_path'].name, 'wb')
            f = form.cleaned_data['photo_path'].read()
            fp.write(f)
            fp.close()
            return HttpResponse('upload ok')
        else :
            return HttpResponse('upload form err')
    else :
        form = PhotoForm()
    return render_to_response('upload.html', {'form': form, 'user': user})

