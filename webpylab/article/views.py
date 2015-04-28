from django.shortcuts import render_to_response
from article.models import Article
__author__ = 'daniel.anselmo'
# Create your views here.

def articles(request):

    return render_to_response('articles.html',
                             {'articles': Article.objects.all()})


def article(request, article_id=1):
    return render_to_response('article.html',
                             {'article': Article.objects.get(id=article_id)})

def show_tst(request):
    return render_to_response('tst.html',
                             {'user_name': __author__,
                              'user_age': '30',
                              'user_children': '0'},)