from django.shortcuts import render
from django.shortcuts import redirect,render
from .models import Trainer

# Create your views here.

from .forms import TrainerRegistrationForm


def register_trainer(request):
    if request.method=="POST":
        form= TrainerRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('register_trainer')
        else:
            print(form.errors)
    else:            
       form= TrainerRegistrationForm()
    return render(request,"register_trainer.htm",{"form":form})

def trainer_list(request):
    trainers = Trainer.objects.all()    
    return render(request,"trainer_list.htm",{"trainers":trainers}) 


def trainer_profile(request,id):
    trainers= Trainer.objects.get(id=id)
    return render(request,"trainer_profile.htm",{"trainer":trainer})

def edit_trainer(request,id):
    trainer= Trainer.objects.get(id=id)
    if request.method=="POST":
        form= TrainerRegistrationForm(request.post,instance= trainer)
        if form.is_valid():
            form.save()
            return redirect("trainer_profile",id=trainer.id)
        else:
            form= TrainerRegistrationForm(instance=trainer)
            return render(request,"edit_trainer.htm",{"form":form})  
    
