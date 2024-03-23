from django.template import loader #用來載入template的套件
from django.http import HttpResponse, HttpResponseRedirect #import 需要的套件
from django.urls import reverse
from .models import Members

# Create your views here.
def index(request):
    mymembers = Members.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'mymembers': mymembers
    }
    # output=""

    # for x in mymembers:
    #     output += x["firstname"]
    # return HttpResponse(output)
    # template = loader.get_template('first.html')
    # return HttpResponse(template.render()) #回傳字串到前端
    # return HttpResponse("Hello World!") #回傳字串到前端

    return HttpResponse(template.render(context, request))

def add(request):
  template = loader.get_template('add.html') 
  return HttpResponse(template.render({}, request)) 

def addrecord(request):
  x = request.POST['first'] 
  y = request.POST['last'] 
  member = Members(firstname=x, lastname=y) 
  member.save() 
  return HttpResponseRedirect(reverse('index')) 

def delete(request, id): 
  member = Members.objects.get(id=id) 
  member.delete()
  return HttpResponseRedirect(reverse('index'))

def testing(request):
  mydata = Members.objects.values_list('firstname')
  mydata2 = Members.objects.filter(firstname='BBB').values()
  QuerySet_Simple = Members.objects.all()
  QuerySet_Detail = Members.objects.all().values()
  template = loader.get_template('test.html') 
  context = {
    'mymembers': mydata,
    'mymembers2': mydata2,
    'QuerySet_Simple': QuerySet_Simple, 
    'QuerySet_Detail': QuerySet_Detail, 
    'emptyObject': [], 
  }
  return HttpResponse(template.render(context, request)) 

def block(request):
  template = loader.get_template('block.html')
  return HttpResponse(template.render()) 

def page(request):
  template = loader.get_template('page.html')
  return HttpResponse(template.render()) 
  