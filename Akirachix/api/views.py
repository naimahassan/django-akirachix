from django.shortcuts import render
from rest_framework import viewsets
from .serializers import StudentSerializer
from student.models import Student
from .serializers import TrainerSerializer
from trainer.models import Trainer
from .serializers import CourseSerializer
from course.models import Course


class  StudentViewSet(viewsets.ModelViewSet):
	queryset = Student.objects.all()
	serializer_class = StudentSerializer

class  TrainerViewSet(viewsets.ModelViewSet):
	queryset = Trainer.objects.all()
	serializer_class = TrainerSerializer

class  CourseViewSet(viewsets.ModelViewSet):
	queryset = Course.objects.all()
	serializer_class = CourseSerializer

