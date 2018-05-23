from django.views.generic import TemplateView, DetailView, ListView
from .models import Restaurant, Foods, Kitchens, RestFood


class HomeView(TemplateView):
    template_name = 'index.html'


class RestaurantsListView(ListView):
    model = Restaurant
    template_name = 'page2.html'

    def get_queryset(self):
        food = self.request.GET.get('food', 'all')
        kitchen = self.request.GET.get('kitchen', 'all')

        queryset = super().get_queryset()
        if not food == 'all' and not kitchen == 'all':
            queryset = queryset.filter(food__pk=food, kitchens__pk=kitchen)
        elif not food == 'all':
            queryset = queryset.filter(food__pk=food)
        elif not kitchen == 'all':
            queryset = queryset.filter(kitchens__pk=kitchen)

        return queryset

    def get_context_data(self, **kwargs):
        kwargs['foods'] = Foods.objects.all()
        kwargs['kitchens'] = Kitchens.objects.filter()
        return super().get_context_data(**kwargs)


class RestaurantView(ListView):
    template_name = 'page3.html'
    model = RestFood

    def get_context_data(self, **kwargs):
        kwargs['foods'] = Foods.objects.all()
        return super().get_context_data(**kwargs)
