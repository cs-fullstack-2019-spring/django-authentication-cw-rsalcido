from django.urls import path
from .import views


# paths created for pages
urlpatterns = [
    path("", views.index,name="index"),
    path("newuser/",views.newuser,name='newuser'),
    path("verifieduser/",views.verifieduser,name='verifieduser'),

]
