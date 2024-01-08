from django .urls import path
from .import views

urlpatterns=[
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('packages/',views.packages,name='packages'),
    path('gallery/',views.gallery,name='gallery'),
    path('contact/',views.contact,name='contact'),
    path('adminlogin/',views.loginadmin,name='adminlogin')
]