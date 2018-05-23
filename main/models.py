from django.db import models


class Restaurant(models.Model):
    title = models.CharField(max_length=32)
    slug = models.SlugField(max_length=64)
    description = models.CharField(max_length=256, blank=True)
    adr = models.CharField(max_length=128)
    icon = models.ImageField()
    order_of = models.DecimalField(max_digits=8, decimal_places=2)
    free_delivery = models.BooleanField()
    delivery_time = models.SmallIntegerField()
    card_pay = models.BooleanField()
    foods = models.ManyToManyField('Foods')
    kitchens = models.ManyToManyField('Kitchens')

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title + '_restaurant')
    #     super(Restaurant, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Food(models.Model):
    title = models.CharField(max_length=32)
    description = models.CharField(max_length=256)
    kind = models.ForeignKey('Foods', on_delete='cascade')
    price = models.DecimalField(max_digits=8, decimal_places=2)
    restaurants = models.ManyToManyField(Restaurant)

    def __str__(self):
        return self.title


class Foods(models.Model):
    title = models.CharField(max_length=32)

    def __str__(self):
        return self.title


class Kitchens(models.Model):
    title = models.CharField(max_length=32)

    def __str__(self):
        return self.title


class RestFood(models.Model):
    title = models.CharField(max_length=32)
    rest = models.ForeignKey('Restaurant', on_delete='cascade')
    description = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.title
