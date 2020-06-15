from django.contrib import admin

from carApp.models import Car


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    pass
