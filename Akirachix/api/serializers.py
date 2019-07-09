from student.models import Student
from course.models import Course
from trainer.models import Trainer
from rest_framework import serializers

class StudentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Student
		fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):
	class Meta:
		model = Course
		fields = "__all__"


class TrainerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Trainer
		fields = "__all__"

