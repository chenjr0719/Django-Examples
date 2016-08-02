from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.forms.models import model_to_dict

from .models import Article, ArticleForm
import mistune

# Create your views here.

def CMS_home(request):
    article_list = Article.objects.all()[:12]
    return render(request, 'Simple_CMS/home.html', locals())

def CMS_add(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            message = 'Contact success!'
            form.save()
            return HttpResponseRedirect('/Simple_CMS/')

    else:
        form = ArticleForm()

    return render(request, 'Simple_CMS/add.html', locals())

def CMS_edit(request, id):
    article = Article.objects.get(pk = id)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance = article)
        if form.is_valid():
            cd = form.cleaned_data
            message = 'Contact success!'
            form.save()
            return HttpResponseRedirect('/Simple_CMS/')

    else:
        form = ArticleForm(initial = model_to_dict(article))

    return render(request, 'Simple_CMS/edit.html', locals())

def CMS_detail(request, id):
    article = Article.objects.get(pk = id)

    return render(request, 'Simple_CMS/article.html', locals())
