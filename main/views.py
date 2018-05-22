from django.views.generic import TemplateView, DetailView, ListView
from .models import Restaurant, Salad, Shashlik, Sushi, Desert, Burger, Pyrog, Pizza


class HomeView(TemplateView):
    template_name = 'index.html'


class RestaurantsListView(ListView):
    model = Restaurant
    template_name = 'page2.html'

    def get_queryset(self):
        food = self.request.GET.get('food', 'all')

        queryset = super().get_queryset()
        if not food == 'all':
            queryset = queryset.filter(food__id=food)
            