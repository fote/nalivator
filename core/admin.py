from django.contrib import admin
from .models import Beverage, Cocktail, CurrentCoctailSet, CurrentPumpSet
# Register your models here.

class CocktailAdmin(admin.ModelAdmin):
    list_display = ('name', 'ing1', 'ing2', 'ing3')

class BeverageAdmin(admin.ModelAdmin):
    list_display = ('name', 'alc', 'density')

class CurrentPumpSetAdmin(admin.ModelAdmin):
    list_display = ('pump1', 'pump2', 'pump3', 'active')


admin.site.register(Beverage, BeverageAdmin)
admin.site.register(Cocktail, CocktailAdmin)
admin.site.register(CurrentCoctailSet)
admin.site.register(CurrentPumpSet,CurrentPumpSetAdmin)


