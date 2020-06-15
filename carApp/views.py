import logging
from django.views.generic.base import TemplateView
from django.views.generic import (ListView,
                                  DetailView)
from django.db.models import Q

from carApp.models import Car


class Search(ListView):

    paginate_by = 2

    def get_queryset(self):
        return Car.objects.filter(Q(brand__icontains=self.request.GET.get('q')) |
                                  Q(car_model__icontains=self.request.GET.get('q')))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['q'] = self.request.GET.get('q')
        return context


class IndexPageView(TemplateView):
    template_name = 'base/about.html'


class HomePageView(TemplateView):
    template_name = 'base/index.html'


class Mercedes:
    @staticmethod
    def get_mercedes():
        return Car.objects.filter(brand='Mercedes')


class MercedesListView(Mercedes, ListView):
    model = Car
    template_name = 'cars/mercedes_list.html'


class Volkswagen:
    @staticmethod
    def get_volkswagen():
        return Car.objects.filter(brand='Volkswagen')


class VolkswagenListView(Volkswagen, ListView):
    model = Car
    template_name = 'cars/volkswagen_list.html'


class BMW:
    @staticmethod
    def get_bmw():
        return Car.objects.filter(brand='BMW')


class BMWListView(BMW, ListView):
    model = Car
    template_name = 'cars/bmw_list.html'


class Audi:
    @staticmethod
    def get_audi():
        return Car.objects.filter(brand='Audi')


class AudiListView(Audi, ListView):
    model = Car
    template_name = 'cars/audi_list.html'


class CarView(DetailView):
    model = Car
    template_name = 'cars/car_detail.html'


class CarListView(ListView):
    model = Car
    template_name = 'cars/car_list.html'


logger = logging.getLogger(__name__)


class NewsList(ListView):
    model = Car

    def get_queryset(self):
        logger.debug(f"Request to NewsList from user: {self.request.user.id} with params: {self.request.GET}")
        logger.info("NewsList.get_queryset called")
        try:
            news = Car.objects.select_related("region").all()
        except Exception as exc:
            logger.error(str(exc))
            raise
        if not news:
            logger.warning("News list is empty")
        return news
