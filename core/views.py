from django.views import View
from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest, HttpResponseBase, HttpResponseServerError, HttpResponseNotFound

from rest_framework.decorators import api_view

from .models import Student
from .forms import StudentForm
from .serializers import StudentSerializer

@api_view(['GET'])
def home(request):
    return render(request, 'index.html')

@api_view(['GET'])
def health(request):
    return HttpResponseBase("hola ok", 200)

@api_view(['POST'])
def create(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid() == False:
        return HttpResponseBadRequest('invalid data')

    try:
        serializer.save()
        return HttpResponseBase('student registered successfully')
    except Exception as e:
        return HttpResponseServerError('internal server error', 500)

@api_view(['GET'])
def get(request, sid):
    try:
        student = Student.objects.get(id=sid)
        serializer = StudentSerializer(student, many=False)
        return HttpResponseBase(serializer.data, 200)
    
    except student.DoesNotExist:
        return HttpResponseNotFound('Student does not exists')

    except Exception as e:
        return HttpResponseServerError('internal server error', 500)

@api_view(['GET'])
def get_all(request):
    try:
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return HttpResponseBase(serializer.data, 200)
    except Exception as e:
        print(e)
        return HttpResponseServerError('internal server error', 500)
    
@api_view(['POST'])
def student_form(request):
    try:
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            redirect_url = f'{settings.BASE_URL}/students'
            return redirect(redirect_url) 
        return render(request, 'student.html', {'form': form})
    
    except Exception as e:
        return HttpResponseServerError('internal server error', 500)

# Just for jun - Class Based View
class ClassCreateUser(View):
    def get(self, request):
        students = Student.objects.all()
        serialized = StudentSerializer(students, many=True)
        return HttpResponseBase(serialized, 200)
    
    def post(self, request):
        if request.method == 'POST':
            name = request.POST.get("name")
            full_name = request.POST.get("full_name")
            contact_phone = request.POST.get("contact_phone")
            contact_mail = request.POST.get("contact_mail")
            obj = Student.objects.create(name=name, full_name=full_name, contact_mail=contact_mail, contact_phone= contact_phone)
            obj.save()
