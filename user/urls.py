from django.urls import path, include
from . import views

app_name = 'user'
urlpatterns = [
    path('signup/',views.SignupFormView.as_view(), name='signup' ),
    path('login/', views.LoginFormView.as_view(), name= 'login' ),
    path('logout/', views.logout_view, name = 'logout'),
    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',views.activate, name='activate'),
    path('', include('user_profile.urls'))

]