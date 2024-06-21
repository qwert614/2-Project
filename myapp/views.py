import pygal as pygal
from django.shortcuts import render
from myapp.models import *
# Create your views here.

def index(request):
    all_contact = Contact.objects.all()
    if request.method=="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        Contact(name=name,email=email,subject=subject,message=message).save()
    all_project = Portifolio.objects.all()
    all_service = Service.objects.all()
    all_team = Team.objects.all()
    categories = Category.objects.all()
    data = {}
    for category in categories:
        project_list = Portifolio.objects.filter(category_id=category.id).all()
        data[category.name]=len(project_list)
    pie_chart = pygal.Pie()
    pie_chart.title = 'Total projects statistika korinishi'
    for i in data:
        pie_chart.add(i,data[i])
    pie_chart.render()
    context = {"project": all_project,
               "project1": all_service,
               "project2": all_team,
               "contact":all_contact,
               "pie_chart": pie_chart.render_data_uri()}
    print(data,"dddddddddddddddddddddddddddddddddddddddddddddddddd")
    return render(request,'index.html',context)

def inner(request):
    return render(request,'inner-page.html')

def portfolio(request,id):
    project = Portifolio.objects.get(id=id)
    context = {"project":project}
    return render(request,'portfolio-details.html',context)