from django.urls import path
from . import views


urlpatterns = [
    #Homepage
    path('', views.BioCreateView.as_view(), name='new_bio'),
    path('school/new', views.BioCreateView.as_view(), name='new_school'),
]