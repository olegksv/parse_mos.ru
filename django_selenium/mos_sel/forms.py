from django import forms
from django.forms import ValidationError
from mos_sel.models import Flat,PaymentsEpd
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.validators import ASCIIUsernameValidator
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm

class MyResetPasswordForm(PasswordResetForm): 
    error_messages = {
        'not_registered': ('Пользователя с таким e-mail не существует'),
    }
    email = forms.CharField(
            label=(""),
            widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}),
        )
    def clean_email(self):
        email = self.cleaned_data.get('email')
        users =  self.get_users(email=email)
        flag = False
        for user in users:
            if user:
                flag = True

        if not flag:
            raise forms.ValidationError(
                self.error_messages['not_registered'],
                code='not_registered',
            )
        return email


class MySetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label=(''),
        widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Новый пароль'}),
        strip=False,)
    
    new_password2 = forms.CharField(
        label=(''),
        widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Повторите пароль'}),
        strip=False,)

class CustomRegisterForm(UserCreationForm):
    username_validator = ASCIIUsernameValidator()
    # username_validator.message='Enter a valid username.'
    username=forms.CharField(validators=[username_validator], label=("Имя пользователя"),widget=forms.TextInput(attrs={"class":"form-control",'placeholder':'Имя пользователя','autocomplete':'username'}))
    password1=forms.CharField(label=("Пароль"),widget=forms.PasswordInput(attrs={"class":"form-control",'placeholder':'Придумайте пароль','autocomplete':'new-password'}))
    password2=forms.CharField(label=("Повторите пароль"),widget=forms.PasswordInput(attrs={"class":"form-control",'placeholder':'Повторите пароль','autocomplete':'new-password'}))
    
    class Meta(UserCreationForm.Meta):
        model=User
        fields=['username','email','password1','password2']
        widgets={
           
            'email':forms.EmailInput(attrs={"class":"form-control",'placeholder':'Ваш email','autocomplete':'email',}),
            
        }
        
        labels = {
            'username': ('Имя пользователя'),
            'email': ('Почта'),
            'password1': ('Пароль'),
            'password2': ('Повторите пароль'),
          
        }
    # Убрать autofocus у поля username
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.pop("autofocus", None)
       

    def clean_email(self):
        email= self.cleaned_data['email']
        if self.cleaned_data['email']=="":
            raise ValidationError("Заполните это поле")
        elif User.objects.filter(email=email).exists():
            raise ValidationError("Эта почта уже зарегистрированна")
        return email

class LoginViewForm(AuthenticationForm):
    username=forms.CharField(label="Имя пользователя", widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Логин"}))
    password=forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Пароль"}))
    remember_me = forms.BooleanField(label=('Запомнить меня'),initial=False, required=False,widget=forms.CheckboxInput(attrs={"class":"form-check-input"}))
    error_messages = {
        "invalid_login":(
            "Неправильное %(username)s или пароль."
        ),
        "inactive": ("Этот аккаунт не активен"),
    }

    class Meta:
        model=User
        fields=['username','password','remember_me','error_messages']
  
    def get_invalid_login_error(self):
        return ValidationError(
            self.error_messages["invalid_login"],
            code="invalid_login",
            params={"username": self.username_field.verbose_name},
        )

class FlatForm(forms.ModelForm):
    
    def clean_name_flat(self):
        name_flat = self.cleaned_data['name_flat']
        if Flat.objects.filter(name_flat=name_flat).exists():
            raise ValidationError(f'Квартира {name_flat} уже существует')
        return name_flat
        
    class Meta:
        model=Flat
        fields=['name_flat']
        widgets={
            'name_flat':forms.TextInput(attrs={"class":"form-control",'placeholder':'Добавьте название квартиры','autocomplete': 'off'})
        }
        labels = {
            'name_flat': ('Название услуги'),

        }

class PaymentsEpdForm(forms.ModelForm):
    name_flat=forms.ModelChoiceField(queryset=Flat.objects.all(), empty_label="Выберите квартиру",widget=forms.Select(attrs={'class': 'form-control'}))

    def clean_name_flat(self):
        name_flat = self.cleaned_data['name_flat']
        if Flat.objects.filter(name_flat=name_flat).exists():
            raise ValidationError(f'Квартира {name_flat} уже существует')
        return name_flat
        
    class Meta:
        model=PaymentsEpd
        fields=['name_flat','amount_of_real','date_of_payment']
        
       
        labels = {
            'name_flat': ('Название квартиры'),
            'amount_of_real':("Сумма оплаты"),
            'date_of_payment':('Дата оплаты')

        }

        widgets={
            'amount_of_real':forms.NumberInput(attrs={"class":"form-control",'placeholder':'Оплачено 0.00руб'}),
            'date_of_payment':forms.DateInput(format=('%Y-%m-%d'),attrs={"class":"form-control",
            'placeholder':'Дата оплаты счета','type':'date'}),
        }