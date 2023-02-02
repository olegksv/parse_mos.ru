from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views.generic import CreateView,TemplateView,ListView,View,UpdateView
from mos_sel.models import Flat,PaymentsEpd
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from mos_sel.forms import *
from django.contrib.messages.views import SuccessMessageMixin
from mos_sel.scraper12 import *
from mos_sel.utils import *
from .forms import FlatForm, LoginViewForm,CustomRegisterForm,PaymentsEpdForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate
from .credentials import login,passw
import calendar
from datetime import datetime,timezone
from django.forms.models import model_to_dict


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
                #logon=Scraper()
                #auth=logon.log(logon.URL_LOGIN,logon.driver(),username,password)
                #Scraper.x=auth
                #print(logon.__dict__)
                #print(Scraper.__dict__)
                #print(Scraper.__dict__)
                logon=log(URL_LOGIN,username,password)
                #logon=log(URL_LOGIN,driver(),username,password)
                #logon=driver(URL_LOGIN,username,passw)
                #logon=log(URL_LOGIN,driver(),username,password)
                #logon=driver()
                #print(logon)
                
                #pickle.dump(logon.get_cookies(),open("C:/Users/osk88/Desktop/Django_projects/django_selenium/auth.pkl","wb"))
                #logon.get_cookies()
                return self.form_valid(form)
            else:
                #messages.error(self.request,"Пользователь не зарегистрирован на mos.ru")
                form.add_error(None,f"Пользователь с именем {username} не зарегистрирован на сайте mos.ru")               
                return self.form_invalid(form)
        else:
            return self.form_invalid(form)
        
    """ def get_context_data(self, **kwargs):
        
        context= super().get_context_data(**kwargs)
        context['log']=log(URL_LOGIN,browser(),login,passw)
        print(context)
        return context """
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

class Cat_uslug(TemplateView):
    template_name="mos_sel/cat_uslug.html"
    

    def get_context_data(self, **kwargs):
        choose_service(CAT_USLUGI)
        return super().get_context_data(**kwargs)

""" class Get_epd(ListView):
    template_name="mos_sel/get_epd.html"
    model=Flat
    form_class=FlatForm
    context_object_name='flats'
    #success_url=reverse_lazy('Get_List_Epd')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #context.update({
            #self['date_start']:forms.DateInput(format=('%Y-%m-%d'),attrs={"class":"form-control",'placeholder':'Дата счета','type':'date'})
        #}) 
        get_epd(GET_EPD)
        
        return context """

class Get_epd(CreateView):
    template_name="mos_sel/get_epd.html"
    form_class=PaymentsEpdForm
    context_object_name='flats'
    success_url=reverse_lazy('Get_List_Epd')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        #self.kwargs['bla']="foo"
        #print(self.kwargs)
        get_epd(GET_EPD)
        return context

class Get_List_Epd(ListView):
    template_name="mos_sel/get_list_epd.html"
    model=PaymentsEpd
    context_object_name='fields'

    def get_context_data(self, **kwargs):
        fl=self.request.GET.get('name_flat',None)
        flats_id=int(fl)
        per_start=self.request.GET.get('start')
        per_end=self.request.GET.get('end')
        date_now=datetime.now(timezone.utc)
        #print(date_now)
        #print(date_now.month)
        #PaymentsEpd.objects.filter(flats_id=self.request.GET.get('name_flat',None))
        date_db=PaymentsEpd.objects.datetimes('date_pars',kind="second").last()
        #PaymentsEpd.objects.filter(flats_id=fl).values('date_pars')
        print(date_db)
        #print(date_db.first())
        #print(date_db.last()['date_pars'])
        #date_first_bd=date_db[0]
        #date_save_bd=date_first_bd['date_pars']
        exist_object=PaymentsEpd.objects.filter(flats_id=fl)
        """ date_db=[]
        date_first_bd=[]
        date_save_bd=[]
        print(f'вот{date_save_bd}') """
        
        #print(date_first_bd)
        
        #print(date_first_bd['date_pars'].month)
        #print(date_db.month)
        if not exist_object.exists():
            context=super().get_context_data(**kwargs)
            
            #pk=PaymentsEpd.objects.filter(flats_id=fl)
            #name_flat=self.request.GET.get['pk']
            #id=PaymentsEpd.objects.get(self.kwargs['pk'])
            #print(f'queryset={pk}')
            #print(fl)
            #flat_id=self.request.GET.get('id')
            #print(id)
            
            #print(fl)
            #d=Flat.objects.get(pk=fl)
            
            #print(Flat.objects.get(pk=fl)) # сам объект метод __str__ выводит его человеческое название = Войковская
            context['name_flat']=Flat.objects.get(pk=fl).name_flat
            lst=form_fill(GET_EPD,context['name_flat'].upper())
            #path=get_path(lst)
            #print(lst)
            pars_data=parsing(lst)
            print(f'pars_data {pars_data}')
            print(f'Save data {save_data(pars_data,flats_id)}')
            #date_db.append(PaymentsEpd.objects.filter(flats_id=fl).values('date_pars')[0])
            #date_db_all=PaymentsEpd.objects.values('date_pars')
            #print(date_db)
            #print(f'все данные времени{date_db_all}')
            #date_first_bd.append(date_db[0])
            #print(date_first_bd)
            #date_save_bd.append(date_first_bd[0]['date_pars'])
            #print(date_save_bd)
            context['per_start']=per_start
            context['per_end']=per_end
            return context
        elif date_now.day==15:
                context=super().get_context_data(**kwargs)
                context['name_flat']=Flat.objects.get(pk=fl).name_flat
                context['per_start']=per_start
                context['per_end']=per_end
                lst=form_fill(GET_EPD,context['name_flat'].upper())
                #print(lst)
                pars_data=parsing(lst)
                save_data(pars_data,flats_id)
                print(f"Это контекст {context}")
                return context 
        else:
            context=super().get_context_data(**kwargs)
            context['per_start']=per_start
            context['per_end']=per_end
            print(context)
            print(date_now.day)
            print(type(date_now.day))
            return context
        """ elif date_db<date_now and date_db.month==date_now.month:
            context=super().get_context_data(**kwargs)
            context['per_start']=per_start
            context['per_end']=per_end
            print(context)
            print(date_now.day)
            print(type(date_now.day))
            return context  """
        """ elif date_db<date_now and date_db.month!=date_now.month and date_now.day==15:
            context=super().get_context_data(**kwargs)
            context['name_flat']=Flat.objects.get(pk=fl).name_flat
            context['per_start']=per_start
            context['per_end']=per_end
            lst=form_fill(GET_EPD,context['name_flat'].upper())
            #print(lst)
            pars_data=parsing(lst)
            save_data(pars_data,flats_id)

            return context """
   
        """ elif date_save_bd[0]<date_now and date_save_bd[0].month==date_now.month:
            context=super().get_context_data(**kwargs)
            return context 
        elif date_save_bd[0]<date_now and date_save_bd[0].month!=date_now.month:
            context=super().get_context_data(**kwargs)
            context['name_flat']=Flat.objects.get(pk=fl).name_flat
            lst=form_fill(GET_EPD,context['name_flat'].upper())
            #print(lst)
            pars_data=parsing(lst)
            save_data(pars_data,flats_id)
            return context """

    def get_queryset(self) :
        super().get_queryset()
        #x=PaymentsEpd.objects.filter(flats_id=self.request.GET.get('name_flat',None),date_pars__contains=date.today().replace(day=17))
        x=PaymentsEpd.objects.filter(flats_id=self.request.GET.get('name_flat',None))
        print(f'это здесь{x}')
        #date_pars=date.today().replace(day=17)
        #print(f"дата {date_pars}")
        return x
"""     def get_path(self,**kwargs):
        get_path=PaymentsEpd.objects.filter(flats_id=self.request.GET.get('name_flat',None))
        return get_path """


class ListCreatedFlats(CreateView):
    form_class=PaymentsEpdForm
    
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

class PaymentListView(ListView):
    template_name='mos_sel/list_payments.html'
    model=PaymentsEpd
    form_class=PaymentsEpdForm
    context_object_name='fields'

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        print(f'контекст тут {self.object_list}')
        self.form=PaymentsEpdForm()
        context['form']=self.form
        print(context['form'])
        per_start=self.request.GET.get('start')
        per_end=self.request.GET.get('end')
        context["per_start"]=per_start
        context["per_end"]=per_end
        return context

    def get_queryset(self):
        super().get_queryset()
        per_start=self.request.GET.get('start')
        per_start=datetime.strptime(per_start,"%m.%Y")
        per_start=per_start.date()
        per_end=self.request.GET.get('end')
        per_end=datetime.strptime(per_end,"%m.%Y")
        per_end=per_end.date()
        print(f'Начало периода{per_start}')
        print(f'Конец периода{per_end}')
        #date_pars=PaymentsEpd.objects.filter(flats_id=self.request.GET.get('name_flat',None)).datetimes("date_pars",kind="second").last()
        #periody_oplaty=PaymentsEpd.objects.filter(flats_id=self.request.GET.get('name_flat',None)).dates("period_oplaty",kind="month")
        #p=PaymentsEpd.objects.filter(flats_id=self.request.GET.get('name_flat',None)).values('period_oplaty')
        #PaymentsEpd.objects.filter(flats_id=self.request.GET.get('name_flat',None),period_oplaty__range=[per_start,per_end])
        #print(k)
        #print(p)
        #date_pars=date_pars.date()
        #print(f'Периоды оплаты {periody_oplaty}')
        #all_payments=PaymentsEpd.objects.filter(flats_id=self.request.GET.get('name_flat',None))
        queryset=PaymentsEpd.objects.filter(flats_id=self.request.GET.get('name_flat',None),period_oplaty__range=[per_start,per_end])
        return queryset

class ShowMorePayments(View):
    def get(self,request):
        if self.request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            if request.method=="GET":
                all_payments=list(PaymentsEpd.objects.filter(flats_id=self.request.GET.get('name_flat',None)).values())
                #all_payments=PaymentsEpd.objects.filter(flats_id=self.request.GET.get('name_flat',None))
                return JsonResponse({'context':all_payments})

""" class AddPayment(View):
    def get(self,request):
        if self.request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            if request.method=="GET":
                all_payments=list(PaymentsEpd.objects.filter(flats_id=self.request.GET.get('name_flat',None)).values())
                return JsonResponse({'context':all_payments})


    def post(self,request):
        if self.request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            if request.method=="POST":
                all_payments=list(PaymentsEpd.objects.filter(flats_id=self.request.GET.get('name_flat',None)).values())
                return JsonResponse({'context':all_payments}) """

class AddPayment(UpdateView):
    model=PaymentsEpd
    template_name='mos_sel/update_modal.html'
    success_url=reverse_lazy("ListCreatedFlats")

    def form_valid(self, form):
        response = super().form_valid(form)
        is_ajax=self.request.headers.get('X-Requested-With') == 'XMLHttpRequest'
        if self.method=="POST":
            if is_ajax:
                data={
                    'pk':self.object.pk,
                    'name_flat':self.object.name_flat,
                    'amount_of_real':self.object.amount_of_real,
                    'date_of_payment':self.object.date_of_payment
            }
                return JsonResponse(data)
            else:
                return response
    
    """     def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        form.fields["amount_of_real"].widget.attrs["class"] = "form-control"
        form.fields["date_of_payment"].widget.attrs["class"] = "form-control"
        return form """
    
    """ def get_success_url(self):
        data_start=self.request.POST['per_start']
        data_end=self.request.POST['per_end']
        print(self.kwargs)
        print(self.object.pk)
        return reverse('ListCreatedFlats') """




    """ def get_context_data(self, **kwargs):
        #print(PaymentListView.__mro__)
        self.object_list = super().get_queryset()
        print(self.object_list)
        context = super(PaymentListView,self).get_context_data(**kwargs)
        print(context)
        context['name_flat']=Flat.objects.get(pk=self.kwargs['pk']).name_flat 
        print(context)
        #logon=Scraper()
        #print(logon.__dict__)
        #print(Scraper.__dict__)
        #Scraper.auth(self)
        #logon.auth()
        #print(logon.logs)
        #print(Scraper.x)
        #forma_fill=logon.form_fill(logon.GET_USLUGA_URL,logon.drvor,context['name_flat'].upper())
        forma_fill=form_fill(GET_USLUGA_URL,context['name_flat'].upper())
        #print(self.kwargs)
        return context """
