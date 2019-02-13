from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
# Create your views here.

class Login(View):

    def get(self, request):
        return render(request, 'login_new.html')

    def post(self, request):
        print(request.POST['username'])
        print(request.POST['password'])
        if request.POST['username'] == 'admin' and request.POST['password']  == '123':
        	return HttpResponse('Dang nhap thanh cong')
        else:
        	return HttpResponse ('Sai thong tin Ten dang nhap hoac Mat khau')

class CartView(View):

    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        print(request.POST['username'])
        return HttpResponse('bat du lieu oke')


def homefunc(request):
    return HttpResponse(' xin chao 2')
