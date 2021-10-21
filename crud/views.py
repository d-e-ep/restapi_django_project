from re import S
from django.shortcuts import render
from django.views.decorators import csrf
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from crud.models import Employee
from crud.serializers import Employeeserializer


# Create your views here.

@csrf_exempt
def Employeeapi(request,id=0):
    if request.method=='GET':
        employee = Employee.objects.all
        employee_serializer = Employeeserializer(Employee,many=True)
        return JsonResponse(employee_serializer.data,safe=False)
    elif request.method =='POST':
        employee_data = JSONParser().parse(request)
        employee_serializer = Employeeserializer(data=employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method == "PUT":
        employee_data = JSONParser().parse(request)
        employee=Employee.objects.get(EmployeeID=employee_data['Employee'])
        employee_serializer=Employeeserializer(employee,data=employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse("Update Successfully",safe=False)
        return JsonResponse("Failed To Update")
    elif request.method == "DELETE":
        employee=Employee.objects.get(EmployeeID=id)
        employee.delete()
        return JsonResponse("Deleted successfully",safe=False)
