from django.contrib import admin
from .models import SomeModel

from import_export.admin import ImportExportModelAdmin
from .resources import SomeModelResource

# @admin.register(SomeModel)
# class SomeModelAdmin(admin.ModelAdmin):
#    pass

@admin.register(SomeModel)
class SomeModelAdmin(ImportExportModelAdmin):
    resource_class = SomeModelResource
    list_display = (
    'id',
    'somefield',
    'estado',
    'subestado',
    'creado',
    'actualizado',
    )
    search_fields = ['id']
