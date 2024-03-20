from django.template import loader #用來載入template的套件
from django.http import HttpResponse #import 需要的套件
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