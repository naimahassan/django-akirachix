from django.db import models
from course.models import Course

class Student(models.Model):
	first_name=models.CharField(max_length = 50)
	second_name=models.CharField(max_length = 50)
	date_of_birth=models.DateField()
	gender=models.CharField(max_length=20)
	registration_number=models.CharField(max_length=70)
	email=models.EmailField(max_length=70)
	phone_number=models.CharField(max_length=70)
	date_joined=models.DateField()
	courses=models.ManyToManyField(Course)
	pic=models.ImageField(upload_to="profile_pic",blank=True,null=True)

	def __str__(self):
		return self.first_name



	# def profile_pic(self, obj):
 #        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
 #            url = obj.headshot.url,
 #            width=obj.headshot.width,
 #            height=obj.headshot.height,
 #            )
 #    )	
