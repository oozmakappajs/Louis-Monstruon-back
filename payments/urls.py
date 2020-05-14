from django.urls import path

from . import views

urlpatterns = [
    path('charge/', views.charge, name='charge'), # new
    path('payment/', views.HomePageView.as_view(), name='payment'),
]