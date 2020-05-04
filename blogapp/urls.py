from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    # path('',views.index,name='index'),
    path('',views.create,name='createblog'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
]

urlpatterns += staticfiles_urlpatterns()