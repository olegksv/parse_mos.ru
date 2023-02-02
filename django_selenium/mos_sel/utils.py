""" from django.shortcuts import render
from .scraper.scraper1   import *

class DataMixin:
    def get_login(self) :
        self.auth=log(URL_LOGIN)
        return self.auth

class AuthView:
    template_name="mos_sel/login.html"

    def get_auth(self,request):
        self.auth=log(URL_LOGIN)
        return render(request,template_name=self.template_name,) """