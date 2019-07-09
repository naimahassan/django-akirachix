from django.contrib import admin
from .models import Course


class CourseAdmin(admin.ModelAdmin):

	list_display=("name","course_duration","start_date","end_date","description","trainer")
	search_fields=("name","course_duration","start_date","end_date","description","trainer_first_name")


admin.site.register(Course,CourseAdmin)
