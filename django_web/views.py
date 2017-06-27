from django.shortcuts import render
from django_web.models import ArticleInfo
# Create your views here.
def index(request):
    articleInfo = ArticleInfo.objects[:1]
    context = {
        'title' : articleInfo[0].title,
        'des' : articleInfo[0].des,
        'score' : articleInfo[0].score
        # 'tags' : articleInfo[0].tags
    }
    return render(request, 'index.html', context)
