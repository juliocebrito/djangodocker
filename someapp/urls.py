from django.urls import path
from .views import send_mail, export_somemodel

app_name = 'someapp'
urlpatterns = [
    path('send_mail/', send_mail, name='send_mail'),
    path('export/somemodel/', export_somemodel, name='export_somemodel'),
]
