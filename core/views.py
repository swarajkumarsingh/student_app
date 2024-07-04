from django.views import View
from django.conf import settings
from django.shortcuts import render, redirect
from rest_framework.response import Response
from django.http import HttpResponseBadRequest, HttpResponseServerError, HttpResponseNotFound

from rest_framework.decorators import api_view

from .models import Student
from .forms import StudentForm
from .serializers import StudentSerializer

@api_view(['GET'])
def home(request):
    return render(request, 'index.html')

@api_view(['GET'])
def health(request):
    return Response("hola ok", 200)

@api_view(['POST'])
def create(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid() == False:
        return HttpResponseBadRequest('invalid data')

    try:
        serializer.save()
        return Response('student registered successfully')
    except Exception as e:
        return HttpResponseServerError('internal server error', 500)

@api_view(['GET'])
def get(request, sid):
    try:
        student = Student.objects.get(id=sid)
        serializer = StudentSerializer(student, many=False)
        return Response(serializer.data, 200)
    
    except student.DoesNotExist:
        return HttpResponseNotFound('Student does not exists')

    except Exception as e:
        return HttpResponseServerError('internal server error', 500)

@api_view(['GET'])
def get_all(request):
    try:
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data, 200)
    except Exception as e:
        print(e)
        return HttpResponseServerError('internal server error', 500)
    
@api_view(['GET', 'POST'])
def student_form(request):
    form = StudentForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('http://localhost:8000/students') 

    return render(request, 'student.html', {'form': form})
