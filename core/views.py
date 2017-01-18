from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader

from .models import Article

def index(request):
    articles = Article.objects.order_by('-date')[:5]
    template = loader.get_template('index.html')
    
    return render(request, 'index.html', { 'articles': articles })

def article(request, aid):

    try:
        article = get_object_or_404(Article, pk=aid)
    except Article.DoesNotExist:
        raise Http404("Article does not exist")
    return render(request, 'article.html', {'article': article})

