from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from test_app.models import Machines
from test_app.serializers import MachineSerializer

from django.core.files.storage import default_storage

# Create your views here.

@csrf_exempt
def machineApi(request,id=0):
    if request.method=='GET':
        machines = Machines.objects.all()
        machines_serializer=MachineSerializer(machines,many=True)
        return JsonResponse(machines_serializer.data,safe=False)
    elif request.method=='POST':
        machine_data=JSONParser().parse(request)
        machines_serializer=MachineSerializer(data=machine_data)
        if machines_serializer.is_valid():
            machines_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        machine_data=JSONParser().parse(request)
        machine=Machines.objects.get(event_id=machine_data['event_id'])
        machines_serializer=MachineSerializer(machine,data=machine_data)
        if machines_serializer.is_valid():
            machines_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        machine=Machines.objects.get(event_id=id)
        machine.delete()
        return JsonResponse("Deleted Successfully",safe=False)

@csrf_exempt
def SaveFile(request):
    file=request.FILES['file']
    file_name=default_storage.save(file.name,file)
    return JsonResponse(file_name,safe=False)