from django.urls import path
from . import views

urlpatterns = [
    path('', views.ApiRoot.as_view(), name=views.ApiRoot.name),
    path('leads/', views.SfdcLeadListView.as_view(), name=views.SfdcLeadListView.name),
    path('viz/', views.HomeView.as_view(), name=views.HomeView.name),
]
