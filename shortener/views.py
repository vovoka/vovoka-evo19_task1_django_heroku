import json
import random
import string
from django.http import JsonResponse, Http404
from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic import View
from rest_framework import generics, status
from .models import Url
from .serializers import UrlSerializer


class UrlShortener(View):
    def get(self, request):
        return render(request, 'index.html', {})


class CreateUrl(generics.CreateAPIView):
    def post(self, request):
        short_url = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(7))
        serializer = Url(real_url = request.data['url'], generated_link = short_url, url_views = 0)
        serializer.save()
        return JsonResponse(
                {'status': status.HTTP_201_CREATED,
                'data': f"http://{str(request.META['HTTP_HOST'])}/-/{str(serializer)}"}
            )


def viewUrl(request, generated_link):
        print(generated_link)
        url_obj =  Url.objects.get(generated_link=str(generated_link))
        print(url_obj)
        url_obj.url_views = url_obj.url_views + 1
        url_obj.save()
        return redirect(str(url_obj.real_url))
    

class UrlListView(generic.ListView):
    model = Url

class UrlDetailView(generic.DetailView):
    model = Url