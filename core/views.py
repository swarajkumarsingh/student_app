from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import Student
from django.views import View
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import StudentSerializer
from django.http import HttpResponseBadRequest, HttpResponse, HttpResponseServerError
from django.views.decorators.debug import sensitive_variables

@api_view(['GET'])
def home(request):
    return render(request, 'index.html')

@api_view(['GET'])
@sensitive_variables('user')
def test(request):
    user = 'me'
    print(user)
    return HttpResponseBadRequest("no internal error")

@api_view(['GET'])
def health(request):
    return Response("hola ok", 200)

@api_view(['POST'])
def create(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid() == False:
        return Response('invalid data', 400)

    try:
        serializer.save()
        return Response('student registered successfully')

    except Exception as e:
        return Response('internal server error', 500)

@api_view(['GET'])
def get(request, sid):
    try:
        student = Student.objects.get(id=sid)
        serializer = StudentSerializer(student, many=False)
        return Response(serializer.data, 200)
    
    except student.DoesNotExist:
        return Response('Student does not exists', 404)

    except Exception as e:
        return Response('internal server error', 500)

@api_view(['GET'])
def get_all(request):
    try:
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data, 200)
    except Exception as e:
        print(e)
        return Response('internal server error', 500)
    
@api_view(['POST'])
def student_form(request):
    form = StudentForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('http://localhost:8000/students') 

    return render(request, 'student.html', {'form': form})


class ClassCreateUser(View):
    def get(self, request):
        students = Student.objects.all()
        serialized = StudentSerializer(students, many=True)
        return Response(serialized, 200)
    
    def post(self, request):
        if request.method == 'POST':
            name = request.POST.get("name")
            full_name = request.POST.get("full_name")
            contact_phone = request.POST.get("contact_phone")
            contact_mail = request.POST.get("contact_mail")
            obj = Student.objects.create(name=name, full_name=full_name, contact_mail=contact_mail, contact_phone= contact_phone)
            obj.save()
