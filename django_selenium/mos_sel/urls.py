from django.urls import path
from mos_sel.views import *
from django.contrib.auth.views import LogoutView,PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView


urlpatterns= [
    path('',Home.as_view(),name='Home'),
    path('password_reset/', PasswordResetView.as_view(template_name='mos_sel/password_reset.html', form_class=MyResetPasswordForm),name="password_reset"),
    path('password_reset/done/', PasswordResetDoneView.as_view(template_name='mos_sel/password_reset_done.html'),name="password_reset_done"),
    path('password_reset/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='mos_sel/password_reset_confirm.html', form_class=MySetPasswordForm),name="password_reset_confirm"),
    path('password_reset/complete/', PasswordResetCompleteView.as_view(template_name='mos_sel/password_reset_complete.html'),name="password_reset_complete"),
    path('register/',Register.as_view(),name='Register'),
    path('cat_uslug/',Cat_uslug.as_view(),name="Cat_uslug"),
    path('choose_flats/',Get_epd.as_view(),name="Get_epd"),
    path('get_list_epd/',Get_List_Epd.as_view(),name="Get_List_Epd"),
    
    path('create_flat/',CreateNewFlat.as_view(),name='CreateFlat'),
    path('list_flats/',ListCreatedFlats.as_view(),name='ListCreatedFlats'),
    path('success_message/', SuccessMessage.as_view(),name='SuccessMessage'),
    path('login/',Login.as_view(),name='Login'),
    path('logout/',LogoutView.as_view(next_page="/"),name='Logout'),
    
    path('success/',SuccessView.as_view(),name='SuccessView'),
    #path('list/',LstView.as_view(),name='LstView'),
    path('parse_list/', PaymentListView.as_view(),name="PaymentListView"),
    path('show_more_payments/',ShowMorePayments.as_view(),name="show_more_payments"),
    path('add_payment/<int:pk>/',AddPayment.as_view(),name="AddPayment")
]
