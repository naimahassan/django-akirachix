from django.contrib import admin
from .models import Trainer

class TrainerAdmin(admin.ModelAdmin):
	list_display=("first_name","second_name","phone_number","profession","email","pic")
	search_feilds=("first_name","second_name","phone_number","profession","email")

admin.site.register(Trainer,TrainerAdmin)
