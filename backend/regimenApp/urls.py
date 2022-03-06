from xml.etree.ElementInclude import include
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter



urlpatterns = [
    path('', views.index),
    path('getQuestionOptions', views.getQuestionOptions),
    path('api/iief-questionnaires/', views.IiefQuestionnaire)
]