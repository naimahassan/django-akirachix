from django.urls import path
from .views import add_trainer
from .views import list_trainers
from .views import trainer_details
from .views import edit_trainer

urlpatterns = [
	path("add/",add_trainer,name="add_trainer"),
	path("list/",list_trainers,name="list_trainers"),
	path("view/<int:pk>/",trainer_details,name="trainer_details"),
	path("edit/<int:pk>/",edit_trainer,name="edit_trainer"),
]