from django.shortcuts import render, HttpResponse
from firstapp.models import People,Ariticle
from django.template import Context, Template

# Create your views here.
def first_try(request):
    person = People(name='skiptomylou',job='CEO')
    html_string = '''
        <html>
            <head>
                <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/semantic-ui/2.2.4/semantic.css">
            </head>
            <body>
                <h1 class="ui center aligned icon header">
                    <i class="hand spock icon"></i>
                    Hello, {{ person.name }}
                    job is {{ person.job }}
            </body>
        </html> 
    '''
    t = Template(html_string)
    c = Context({'person':person})
    web_page = t.render(c)

    return HttpResponse(web_page)

def index(request):

    print(request)
    print('##'*30)
    print(dir(request))
    print('##'*30)
    print(type(request))
    queryset = request.GET.get('tag')
    #如果queryset不为空，按照过滤器进行查询，如果为空则全部查找
    if queryset :
        article_list = Ariticle.objects.filter(tag=queryset)
    else:
        article_list = Ariticle.objects.all()
    context = {}
    #objects.all 方法是取出这个表中的所有数据装载到article_list里面

    context['article_list'] = article_list
    index_page = render(request,'first_web_2.html',context)
    return index_page