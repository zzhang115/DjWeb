from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'title' : 'New Title',
        'des' : 'New Description',
        'score' : '5.0'
    }
    return render(request, 'index.html', context)
