from django.contrib import admin
from .models import Student


class StudentAdmin(admin.ModelAdmin):
	list_display=("registration_number","first_name","second_name","date_of_birth","email","pic")
	search_feilds=("registration_number","first_name","second_name","date_of_birth","email")
	

admin.site.register(Student,StudentAdmin)
