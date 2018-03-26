from django.shortcuts import render, HttpResponse
from .tasks import task_send_mail, export_excel
from .resources import SomeModelResource
from .models import SomeModel
import redis

redis_client = redis.StrictRedis(host='redis', port='6379', db=0)

def send_mail(request):
    subject = 'Hola'
    message = 'hola world'
    from_to = 'someapp@djangodocker.com'
    to = 'jucebridu@gmail.com'
    task_send_mail.delay(subject, message, from_to, to)
    return HttpResponse(status=204)

def export_somemodel(request):
    somemodel_resource = SomeModelResource()
    dataset = somemodel_resource.export()
    response = HttpResponse(dataset.xlsx, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Somemodel.xlsx"'
    return response
