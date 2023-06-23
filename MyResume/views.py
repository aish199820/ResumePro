from multiprocessing import context
from django.shortcuts import render

# Create your views here.

def home_view(request):
    return render(request,'MyResume/home.html')


def skills_view(request):
    context={'Skills':{'Python':70,'Javascript':20,'Django':50,"HTML":60,'CSS':70}}
    return render(request,'MyResume/skills.html',context)

# def contact_view(request):
#     if request.method == 'POST':
#         name=request.POST['name']
#         email=request.POST['email']
#         feedback=request.POST['text']
#         print(name)
#         print(email)
#         print(feedback)

#     return render(request,'MyResume/contact.html')



def eduction_view(request):

    context={"course":{
    "SSC":{'sr':1,'study':"SSC",'per':"71.48%",'year':2013,"board":"Kokan Board"},
    "HSc":{'sr':2,'study':"HSC",'per':"52%",'year':2015,"board":"Kokan Board"},
    "BSC":{'sr':3,'study':"BSC(IT)",'per':"C-Grade",'year':2018,"board":"Mumbai University"}
    }}


    return render(request,'MyResume/education.html',context)


def courses_view(request):
    context={'courses':{
        'Python':{'Course':'Python-FullStack Developer','Institute':'Squad Infotech','Year':2022},
        'MS-CIT':{'Course':'MS-CIT','Institute':'Aptech Institute','Year':2013}
    }}
    return render(request,'MyResume/course.html',context)


def experience_view(request):
    return render(request,'MyResume/experience.html')


def project_view(request):
    return render(request,'MyResume/project.html')


def health_view(request):
    return render(request,'MyResume/health.html')

def shop_view(request):
    return render(request,'MyResume/shop.html')

