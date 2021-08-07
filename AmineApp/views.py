from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from AmineApp.models import Post
from django.shortcuts import redirect, render
from .models import Post, Video

def myhome(request):
        Posts =  Post.objects.all()
        Videos = Video.objects.all()
        context = {
            'videos' : Videos,
            'posts' : Posts,
            }
        return render(request, 'Home.html', context)

def contact(request):
    if request.method == "POST":
        message_name = request.POST['message_name']
        message_email = request.POST['message_email']
        message = request.POST['message']
        try:
            send_mail(message_name, message, message_email, ['admin@admin.com'])
        except BadHeaderError:
            return HttpResponse('Something went wrong ...')
        return redirect('../')
    else:
        return render(request, 'contact.html',{})