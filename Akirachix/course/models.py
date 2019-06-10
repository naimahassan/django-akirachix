from django.db import models
from trainer.models import Trainer

class Course(models.Model):
	name=models.CharField(max_length =50)
	description=models.TextField()
	start_date=models.DateField(max_length=30)
	end_date=models.DateField(max_length=30)
	course_duration=models.SmallIntegerField(max_length=30)
	trainer=models.ForeignKey(Trainer,null=True,on_delete=models.CASCADE)

	def __str__(self):
		return self.name

