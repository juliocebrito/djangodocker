from django.db import models

class SomeModel(models.Model):
    somefield = models.CharField(max_length=255, blank=True, null=True)

    estado = models.BooleanField(default=True)
    subestado = models.BooleanField(default=False)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-creado',)
        verbose_name = 'somemodel'
        verbose_name_plural = 'somemodels'

    def __str__(self):
        return str(self.id)

    # def get_absolute_url(self):
    #     return reverse(':', kwargs={'pk': self.pk})
