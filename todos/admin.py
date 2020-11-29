from django.contrib import admin
from .models import Departamento,Provincia,Distrito,TipoInstitucion,Institucion

# Register your models here.
admin.site.register(Departamento)
admin.site.register(Provincia)
admin.site.register(Distrito)
admin.site.register(TipoInstitucion)
admin.site.register(Institucion)
