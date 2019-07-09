from django.shortcuts import render
from .forms import TrainerForm
from .models import Trainer
from django.shortcuts import redirect

def add_trainer(request):	
	if request.method== "POST":
		form = TrainerForm(request.POST)
		if form.is_valid:
			form.save()

	else:
		form = TrainerForm()
	return render(request,"add_trainer.html",{"form":form})


def list_trainers(request):
	trainers =Trainer.objects.all()
	return render(request,"all_trainers.html",{"trainers":trainers})


def trainer_details(request,pk):
	trainer =Trainer.objects.get(pk=pk)
	return render(request,"trainer_details.html",{"trainer":trainer})

def edit_trainer(request,pk):
	trainer=Trainer.objects.get(pk=pk)
	if request.method == "POST":
		form =TrainerForm(request.POST,instance=trainer)
		if form.is_valid:
			form.save()
			return redirect("list_trainers")

	else:
		form = TrainerForm(instance=trainer)
	return render(request,"edit_trainer.html",{"form":form})