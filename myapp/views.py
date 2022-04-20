from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from myapp.models import Resume
from .forms import ResumeForm
from django.views import View



def Homeview(request):
    
    if request.method == 'POST':
        form = ResumeForm(request.POST , request.FILES)
        if form.is_valid():
          form.save() 
          return HttpResponseRedirect('/')
      
    else:
      
      form = ResumeForm()
      candidates = Resume.objects.all()
    return render( request ,'myapp/form.html',{'form':form , 'candidates':candidates})
  
def Resumeprofile(request,pk):
  
  candidate = Resume.objects.get(pk=pk)  
  return render(request,'myapp/candidate.html',{'candidate':candidate})
