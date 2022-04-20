from distutils.command.upload import upload
from sre_parse import State
from tokenize import blank_re
from django.db import models
from django.forms import CharField

STATE_CHOICE = (
     
     ('karachi','karachi'),
     ('pindi','pindi'),
     ('islamabad','islamabad')  , 
    
)



# Create your models here.
class Resume(models.Model):
    
    name  = models.CharField(max_length=100)
#     dob = models.DateField(auto_now=False , auto_now_add= False)
    gender = models.CharField(max_length=100)
    locality = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    pin = models.PositiveIntegerField()
    state = models.CharField(choices=STATE_CHOICE , max_length=50)
    mobile = models.PositiveIntegerField()
    email = models.EmailField()
    job_city = models.CharField(max_length=50)
    profile_image = models.ImageField(upload_to='myapp/img',blank=True)
    my_file = models.FileField(upload_to='myapp/doc' ,blank=True)
    