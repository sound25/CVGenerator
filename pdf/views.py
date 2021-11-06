import pdfkit
from django.http import HttpResponse
from django.template import loader
import io
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
    template=loader.get_template('pdf/resume.html')
    html=template.render({'user_profile':user_profile})
    pdf=pdfkit.from_string(html,False,options={
        'page-size':'Letter',
        'encoding':'UTF-8',
    })
    response=HttpResponse(pdf,content_type='application/pdf')
    response['Content-Disposition']='attachment'
    filename="Resume.pdf"
    return response
    #return render(request,'pdf/resume.html',{'user_profile':user_profile})

def list(request):
    profile=Profile.objects.all()
    return render(request,'pdf/list.html',{'profile':profile})