from django.shortcuts import render,HttpResponsePermanentRedirect
from django.urls import reverse



def index(request):
    return HttpResponsePermanentRedirect(reverse("blog_list"))