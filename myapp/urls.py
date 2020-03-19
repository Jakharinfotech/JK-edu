from django.urls import path,include
from . import views
from django.contrib.auth.views import LoginView
from django.contrib.auth import login,logout


app_name='myapp'
urlpatterns = [
    path('',views.index,name='index'),
    path('login/',LoginView.as_view(),name='login'),
    path('panel/',views.panel,name='home'),
    path('create/',views.createManager,name='createManager'),
    path('managers/',views.managers,name='managers'),
    path('logout/',views.log_out,name='logout'),
    #path('panel/',views.panel,name='panel'),
    #path('teacher/register/',views.teacherRegistration,name='teacher-dashboard'),
    #path('signup/', SignUpView.as_view(), name='signup'),
    
]