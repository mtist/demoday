from django.contrib import admin
from .models import Restaurant, Food, Kitchens, Foods, RestFood


class RestAdmin(admin.ModelAdmin):
    filter_horizontal = ('foods', 'kitchens')
    prepopulated_fields = {'slug': ('title',)}


class FoodAdmin(admin.ModelAdmin):
    filter_horizontal = ('restaurants',)


admin.site.register(Restaurant, RestAdmin)
admin.site.register(Food, FoodAdmin)
admin.site.register(Foods)
admin.site.register(Kitchens)
admin.site.register(RestFood)
