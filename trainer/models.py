from django.db import models

# Create your models here.
class Trainer(models.Model):
    def full_name(self):
        return f"{self.first_name}{self.last_name}"
    first_name=models.CharField(max_length=18, null=True)
    last_name=models.CharField(max_length=18, null=True)
    Gender=(
        ('M','Male'),
        ('F','Female'),
        ('O','Other'))
    gender=models.CharField(max_length=1,choices=Gender, default="Male", null=True)
    nationality=(
        ('RWANDAN','Rwandan'),
        ('UGANDAN','Ugandan'),
        ('SOUTH SUDANESE','South Sudanese'),
        ('KENYAN','Kenyan'))
    nationality=models.CharField(max_length=15,choices=nationality, null=True)
    # email=models.EmailField(max_length=40,null=True)
    phone_number=models.CharField(max_length=15,null=True)
    course=models.CharField(max_length=20,null=True)
    contract=models.FileField(upload_to='documents/%y/%m/%d',null=True)
    resume=models.FileField(upload_to='',null=True)
    salary=models.PositiveBigIntegerField(null=True)
    trainer_id=models.CharField(max_length=20, null=True)
    company=models.CharField(max_length=20,null=True)
    picture=models.ImageField(upload_to='images/', null=True)
    date_hired= models.DateField(null=True)

    



    
