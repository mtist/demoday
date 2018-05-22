from django.contrib import admin
from .models import Restaurant, Salad, Shashlik, Sushi, Desert, Burger, Pizza, Pyrog, Kitchens, Foods


class RestAdmin(admin.ModelAdmin):
    filter_horizontal = ('foods', 'kitchens')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Restaurant, RestAdmin)
admin.site.register(Salad)
admin.site.register(Shashlik)
admin.site.register(Sushi)
admin.site.register(Desert)
admin.site.register(Burger)
admin.site.register(Pyrog)
admin.site.register(Pizza)
admin.site.register(Foods)
admin.site.register(Kitchens)
