from django.shortcuts import render
from .models import Profile
# Create your views here.
def index(request):
    if request.method=='POST':
        name=request.POST.get('name',"")
        email=request.POST.get('email',"")
        phone=request.POST.get('phone',"")
        summary=request.POST.get('summary',"")
        skills=request.POST.get('skills',"")
        previous_work=request.POST.get('previous_Work',"")
        degree=request.POST.get('degree',"")
        school=request.POST.get('school',"")
        university=request.POST.get('university',"")
        profile=Profile(name=name,email=email,skills=skills,phone=phone,degree=degree,univesity=university,previous_work=previous_work,summary=summary,school=school)
        profile.save()
    return render(request,'pdf/index.html')

def resume(request,id):
    user_profile=Profile.objects.get(pk=id)
    return render(request,'pdf/resume.html',{'user_profile':user_profile})
