from django.contrib import admin
from .models import property,property_image,Card
# Register your models here.

admin.site.register(property)
admin.site.register(property_image)
admin.site.register(Card)