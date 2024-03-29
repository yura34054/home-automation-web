import json

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from app.internal.models import SensorReading
from app.internal.services import sensor_service

sensor_reading_generator = sensor_service.SensorReadingGenerator()


def index(request):
    context = {"sensor_reading": SensorReading.objects.first()}
    return render(request, "index.html", context)


@csrf_exempt
def create_sensor_reading(request):
    if request.method != "POST":
        return HttpResponse(status=405)

    data = json.loads(request.body)

    status = sensor_reading_generator.update(
        controller_name=data["controller_name"],
        api_key=data["api_key"],
        temperature=data["temperature"],
        humidity=data["humidity"],
        carbon_dioxide=data["carbon_dioxide"],
        raw_voc_data=data["raw_voc_data"],
        raw_nox_data=data["raw_nox_data"],
    )

    if status:
        return HttpResponse(status=201)

    return HttpResponse(status=401)
