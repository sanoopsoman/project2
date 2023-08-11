
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('login/',views.login,name='login'),
    path('create_account/',views.create_account,name='create_account'),
    path('add_user/',views.add_user,name='add_user'),
    path('signup/',views.signup,name='signup'),

]