from django.contrib import admin
from .models import Vehiculo, Modelo, Marca, Master, Ubicacion
from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy

# Register your models here.

class Respuesta (admin.StackedInline):
    model = Vehiculo
    extra = 3

class Pregunta (admin.ModelAdmin):
    inlines = [Respuesta]
    #list_display = ('chasis', 'produccion')



admin.site.register(Marca)
admin.site.register(Modelo)
admin.site.register(Master)
admin.site.register(Vehiculo)
admin.site.register(Ubicacion)


class MyAdminSite(AdminSite):
    # Text to put at the end of each page's <title>.
    site_title = ugettext_lazy('My site admin')

    # Text to put in each page's <h1> (and above login form).
    site_header = ugettext_lazy('My administration')

    # Text to put at the top of the admin index page.
    index_title = ugettext_lazy('Site administration')

admin_site = MyAdminSite()