from django.contrib import admin

from .models import Person, Species
admin.site.register(Species)
admin.site.register(Person)

# Register your models here.
