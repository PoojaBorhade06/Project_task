from django.urls import path
from .import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login',views.loginView,name='login'),
    path('register', views.registerView, name='register'),
    path('logout', views.logoutView, name='logout'),
    path('changepassword', views.password_change, name='changepassword'),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name = "Reset_pw/reset_password.html"), name ='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name = "Reset_pw/password_reset_sent.html"), name ='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name = "Reset_pw/password_reset_form.html"), name ='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name = "Reset_pw/password_reset_done.html"), name ='password_reset_complete')
]



