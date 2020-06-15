from django.urls import path

from .views import (IndexPageView, CarListView, CarView, HomePageView)

urlpatterns = [
    path('', HomePageView.as_view()),
    path('about/', IndexPageView.as_view()),
    path('car_list/', CarListView.as_view()),
    path('carApp/<str:pk>/', CarView.as_view()),
]