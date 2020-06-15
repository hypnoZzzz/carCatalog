from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from carApp import views
from carApp.views import (IndexPageView, CarListView,
                          CarView, MercedesListView,
                          VolkswagenListView, BMWListView,
                          AudiListView, HomePageView,)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view()),
    path('search/', views.Search.as_view(), name='search'),
    path('car_list/', CarListView.as_view()),
    path('mercedes/', MercedesListView.as_view()),
    path('volkswagen/', VolkswagenListView.as_view()),
    path('bmw/', BMWListView.as_view()),
    path('audi/', AudiListView.as_view()),
    path('cars/<str:pk>/', CarView.as_view()),
    path('car_list/cars/<str:pk>/', CarView.as_view()),
    path('about_us/', IndexPageView.as_view()),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
