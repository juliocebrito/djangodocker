from import_export import resources

from .models import SomeModel

class SomeModelResource(resources.ModelResource):

    def for_delete(self, row, instance):
        return self.fields['subestado'].clean(row)

    class Meta:
        model = SomeModel
        exclude = ( 'creado', 'actualizado',)
        # export_order = (
        # 'id',
        # )
