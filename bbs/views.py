from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Article


def index(request):
    context = {
        "message": "Welcome my BBS",
        "articles": Article.objects.all()
    }
    return render(request, "bbs/index.html", context)


def detail(request, id):
    article = get_object_or_404(Article, pk=id)
    context = {
        "message": 'Show Article' + str(id),
        "article": article
    }
    return render(request, "bbs/detail.html", context)


def create(request):
    article = Article(content="Hello BBS", user_name="paiza")
    article.save()

    context = {
        "message": "Welcome my BBS",
        "articles": Article.objects.all()
    }
    return render(request, "bbs/index.html", context)


def delete(request, id):
    article = get_object_or_404(Article, pk=id)
    article.delete()
    context = {
        "message": 'Show Article' + str(id),
        "articles": Article.objects.all()
    }
    return render(request, "bbs/index.html", context)
