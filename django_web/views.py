from django.shortcuts import render
from django_web.models import ArticleInfo
from django.core.paginator import Paginator
# Create your views here.
def index(request):
    limit = 2
    articleInfo = ArticleInfo.objects[:4] #this number 4 seems useless
    paginator = Paginator(articleInfo, limit)
    page = request.GET.get('page', 1) #page number
    print('page:',page)
    loadedPage = paginator.page(page)
    loadedPage.has_previous()
    # loadedPage.has_next()
    # loadedPage.number
    # print(loadedPage.paginator.num_pages)
    # loadedPage.pre
    context = {
        'ArticleInfo' : loadedPage
        # 'title' : articleInfo[0].title,
        # 'des' : articleInfo[0].des,
        # 'score' : articleInfo[0].score
        # 'tags' : articleInfo[0].tags
    }
    return render(request, 'index.html', context)
