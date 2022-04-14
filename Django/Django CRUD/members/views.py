from audioop import reverse
from re import template
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Members
from django.urls import reverse
def index(request):
    mymembers = Members.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'mymembers':mymembers,
    }
    return HttpResponse(template.render(context,request))

# Create your views here.
def add(request):
    template = loader.get_template('add.html')
    return HttpResponse(template.render({},request))
def addrecord(request):
    f = request.POST['first']
    l = request.POST['last']
    newMember = Members(firstname=f,lastname=l)
    newMember.save()
    return HttpResponseRedirect(reverse('index'))
def delete(reuquest, id):
    member = Members.objects.get(id=id)
    member.delete()
    return HttpResponseRedirect(reverse('index'))
def update(request, id):
    member = Members.objects.get(id = id)
    template = loader.get_template('update.html')
    context = {
        'selectedMember': member,
    }
    return HttpResponse(template.render(context, request))
def updaterecord(request, id):
    member = Members.objects.get(id= id)
    f = request.POST['first']
    l = request.POST['last']
    member.firstname = f
    member.lastname = l
    member.save()
    return HttpResponseRedirect(reverse('index'))

