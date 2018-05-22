from django.db import models
from django.template.defaultfilters import slugify


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


class Sushi(models.Model):
    title = models.CharField(max_length=32)
    description = models.CharField(max_length=256)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    @property
    def price(self):
        return "%s₽" % self.price

    def __str__(self):
        return self.title


class Pizza(models.Model):
    title = models.CharField(max_length=32)
    description = models.CharField(max_length=256)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    @property
    def price(self):
        return "%s₽" % self.price

    def __str__(self):
        return self.title


class Burger(models.Model):
    title = models.CharField(max_length=32)
    description = models.CharField(max_length=256)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    @property
    def price(self):
        return "%s₽" % self.price

    def __str__(self):
        return self.title


class Salad(models.Model):
    title = models.CharField(max_length=32)
    description = models.CharField(max_length=256)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    @property
    def price(self):
        return "%s₽" % self.price

    def __str__(self):
        return self.title


class Desert(models.Model):
    title = models.CharField(max_length=32)
    description = models.CharField(max_length=256)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    @property
    def price(self):
        return "%s₽" % self.price

    def __str__(self):
        return self.title


class Shashlik(models.Model):
    title = models.CharField(max_length=32)
    description = models.CharField(max_length=256)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    @property
    def price(self):
        return "%s₽" % self.price

    def __str__(self):
        return self.title


class Pyrog(models.Model):
    title = models.CharField(max_length=32)
    description = models.CharField(max_length=256)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    @property
    def price(self):
        return "%s₽" % self.price

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
