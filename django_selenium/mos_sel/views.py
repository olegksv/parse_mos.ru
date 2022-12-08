from django.shortcuts import redirect, render
from django.views.generic import CreateView,TemplateView,ListView,View
from mos_sel.models import Flat
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from mos_sel.forms import *
from django.contrib.messages.views import SuccessMessageMixin
from mos_sel.scraper1 import *
from mos_sel.utils import *
from .forms import FlatForm, LoginViewForm,CustomRegisterForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate
from .credentials import login,passw

class Home(TemplateView):
    template_name='mos_sel/home.html'

class Register(SuccessMessageMixin,CreateView):
    template_name='mos_sel/register.html' 
    form_class=CustomRegisterForm
    success_message="Пользователь %(username)s был успешно создан"
    success_url=reverse_lazy('SuccessMessage')

class SuccessMessage(TemplateView):
    template_name='mos_sel/success_message.html'
    """ success_url=reverse_lazy('Login') """

class Login(LoginView):
    template_name='mos_sel/login.html' 
    form_class=LoginViewForm
    
    def form_valid(self, form):
       
        remember_me = form.cleaned_data['remember_me']  # get remember me data from cleaned_data of form
        #print(remember_me)
        #print(self.request.session.get_expiry_age())
        if not remember_me:
            self.request.session.set_expiry(0)  # if remember me is 
            #print(self.request.session.get_expiry_age())
            #print(self.request.session.set_expiry(0))
            self.request.session.modified = True
        return super().form_valid(form)
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["request"] = self.request
        #print(kwargs)
        return(kwargs)

    def post(self, request, *args, **kwargs):

        form = self.get_form()
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            if username==login and password==passw: 
                #self.kwargs=log(URL_LOGIN,username,password)
                #logon=log(URL_LOGIN,browser(),username,password)
                return self.form_valid(form)
            else:
                #messages.error(self.request,"Пользователь не зарегистрирован на mos.ru")
                form.add_error(None,f"Пользователь с именем {username} не зарегистрирован на сайте mos.ru")               
                return self.form_invalid(form)
        else:
            return self.form_invalid(form)
        
    def get_context_data(self, **kwargs):
        
        context= super().get_context_data(**kwargs)
        context['log']=log(URL_LOGIN,browser(),login,passw)
        print(context)
        return context
    """     def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.username=form.cleaned_data.get('username')
        self.object.password=form.changed_data.get('password')
        login(URL_LOGIN,self.object.username,self.object.password)
        self.object.save()
        return super().form_valid(form) """

    """     def get_context_data(self, **kwargs):
        
        form=LoginViewForm()
        username=form.cleaned_data.get('username')
        password=form.cleaned_data.get('password')
        log(URL_LOGIN,username,password)
        return super().get_context_data(**kwargs) """


    def get_success_url(self):
        url = self.get_redirect_url()
        if url:

            return url
        elif self.request.user.is_superuser:
            return reverse("Home")
        else:
            return reverse("Home")

""" class Login(View):
    template_name='mos_sel/login.html' 
    form_class=LoginViewForm

    def get(self, request):
        form = self.form_class()
        message = 'gdfgd'
        return render(request, self.template_name, context={'form': form, 'message': message})
        
    def post(self, request):
        form = self.form_class()
        if form.is_valid():
            #username=form.cleaned_data.get('username')
            #password=form.cleaned_data.get('password')
        
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                log(URL_LOGIN,username,password)
                return redirect('Home')
        message = 'Login failed!'
        return render(request, self.template_name, context={'form': form, 'message': message}) """


class ListCreatedFlats(ListView):
    model=Flat
    template_name='mos_sel/list_flats.html'
    context_object_name='flats'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        """ context['payments']=Payments.objects.all() """
        return context

""" class AuthView(TemplateView):
    template_name="mos_sel/login.html"
   
 
    def get_context_data(self, **kwargs) :
        # get_context_data это метод AuthView
        # kwargs - пуст
        print(kwargs)
        # вызываем super() у TemplateView чтобы вернуть его словарь с контекстом для шаблона
        # он возвращает {'view': <mos_sel.views.AuthView object at 0x000001FE82705D00>}
        context=super().get_context_data(**kwargs)
        print(kwargs)
        print(context)
        # context["login"] добавляет в контекст уже моего класса AuthView
        context['login']=login(URL_LOGIN)
        # context уже содержит 
        # {'view': <mos_sel.views.AuthView object at 0x000001FE82705D00>, 
        # 'login': <selenium.webdriver.chrome.webdriver.WebDriver (session="b574939f2d33731fc0dcc512d97ee894")>}
        print(context)
        print(kwargs)
        return context """
    
""" def auth(request):
    if request.method=='GET':
        login_auth=login(URL_LOGIN)
        return render(request,'mos_sel/login.html',context={'login':login_auth}) """  


""" class SuccessView(TemplateView):
    template_name="mos_sel/success.html" """

class SuccessView(TemplateView):
    template_name="mos_sel/success_message.html"

class CreateNewFlat(LoginRequiredMixin,SuccessMessageMixin,CreateView):
        form_class=FlatForm
        template_name='mos_sel/add_flat.html'
        success_message="Квартира %(name_flat)s была успешно добавлена"
        success_url=reverse_lazy('CreateFlat')
        context_object_name='name_flat'
        """ login_url = '/403/' """
        
        raise_exception=True
        # при атрибуте raise_exception и атрибуте permission_denied_message - ошибка в виде строки отображается в консоли!
        permission_denied_message = 'You are not allowed this transaction'

        def form_invalid(self, form):
            super().form_invalid(form)
            #print(response)
            #print(form.cleaned_data)
            #print(form.fields.get(self.request.POST['name_flat']))
            #print(form.fields['name_flat'])
            #print(self.request.POST['name_flat'])
            name_flat=self.request.POST['name_flat']
            #Flat.objects.values('name_flat')
            #name_flat=Flat.objects.filter(name_flat=name_flat) 
            messages.error(self.request, f'Квартира {name_flat} уже существует')
            return self.render_to_response(self.get_context_data(request=self.request, form=form))
         
        def get_context_data(self, **kwargs):
            context=super().get_context_data(**kwargs)
            return context

""" class LstView(ListView):
    model=Flat
    template_name='mos_sel/list_flats.html'
    context_object_name='flats' """

class PaymentListView(Login,ListView):
    template_name='mos_sel/parse_list.html'
    model=Flat
    context_object_name='fields'

    def get_context_data(self, **kwargs):
        print(PaymentListView.__mro__)
        self.object_list = super().get_queryset()
        print(self.object_list)
        context = super(PaymentListView,self).get_context_data(**kwargs)
        print(context)
        context['name_flat']=Flat.objects.get(pk=self.kwargs['pk']).name_flat 
        print(context)
    
        forma_fill=form_fill(GET_USLUGA_URL,context['log'],context['name_flat'].upper())
        print(self.kwargs)
        return context
