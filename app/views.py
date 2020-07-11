from django.shortcuts import render,redirect
from django.contrib import messages
from django.views.generic import View
from django.http import HttpResponse
import json
from django.core.exceptions import ObjectDoesNotExist
from .models import adminModel
from django.core import serializers

# Create your views here.
class adminLogin(View):
    def post(self, request):
        mail=request.POST.get('adminemail')
        pwd=request.POST.get('adminpwd')
        data={"email":mail,"password":pwd}
        try:
            data=adminModel.objects.get(email=mail , password=pwd)
            request.session['admin']=mail
            messages.success(request, "Account is Logined")
            redirectpage="admindashboard"
        except ObjectDoesNotExist:
            messages.error(request, "Invalid Account Details")
            redirectpage="admin"
        except:
            messages.error(request, "Account Not Found")
            redirectpage = "admin"


        return redirect(redirectpage)

def adminLogout(request):
    return HttpResponse('Logout Successfully')