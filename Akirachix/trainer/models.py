from django.db import models

class Trainer(models.Model):
	first_name=models.CharField(max_length = 50)
	second_name=models.CharField(max_length = 50)
	gender=models.CharField(max_length=20)
	id_number=models.CharField(max_length=50, null=True)
	email=models.EmailField(max_length=70)
	phone_number=models.CharField(max_length=70)
	profession=models.CharField(max_length=70)
	date_employed=models.DateField()
	course_teaching=models.CharField(max_length=100)
	working_status=models.CharField(max_length=100)
	others=models.CharField(max_length=100)


	def __str__(self):
		return self.first_name
	
	
	

