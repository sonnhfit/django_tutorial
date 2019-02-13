from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
# Create your views here.


class CartView(View):

    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        print(request.POST['username'])
        return HttpResponse('bat du lieu oke')


def homefunc(request):
    return HttpResponse(' xin chao 2')
