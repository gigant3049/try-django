from django.shortcuts import render, reverse, get_object_or_404, redirect
from django.contrib import messages

from .models import Article
from .forms import ArticleForm


def index(request):
    article = Article.objects.get(id=1)
    title = article.title
    content = article.content
    context = {
        'title': title,
        'content': content
    }
    return render(request, 'article/index.html', context)


def article_list(request):
    query = request.GET.get('q')
    articles = Article.objects.search(query=query)
    # try:
    #     int(query)
    # except:
    #     lookups = Q(title__icontains=query)
    # else:
    #     lookups = Q(title__icontains=query) | Q(id=query)
    # if query:
    #     # articles = Article.objects.filter(title__exact=query)
    #     articles = Article.objects.filter(title__icontains=query)
    context = {
        'object_list': articles,
    }
    return render(request, 'article/index.html', context)


def article_detail(request, slug):
    article = Article.objects.get(slug=slug)
    context = {
        'object': article
    }
    return render(request, "article/detail.html", context)


def article_create(request):
    context = {
        'created': False
    }
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        obj = Article.objects.create(title=title, content=content)
        context['created'] = True
        context['object'] = obj
        messages.success(request, f'Article {obj.title} successfully created')
    return render(request, 'article/create.html', context)


def article_create_form(request):
    form = ArticleForm()
    if request.method == "POST":
        form = ArticleForm(request.POST, files=request.FILES)
        if form.is_valid():
            obj = form.save()
            messages.success(request, f'Article {obj.title} successfully created')
            reverse_url = reverse('article:detail', args=[obj.id])
            return redirect(reverse_url)
    context = {
        'form': form
    }
    return render(request, 'article/create_form.html', context)


def article_change(request, pk):
    obj = Article.objects.get(id=pk)
    form = ArticleForm(instance=obj)
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=obj, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, f'Article {obj.title} successfully edited')
            reverse_url = reverse('article:change-form', kwargs={'pk': obj.id})
            return redirect(reverse_url)
    context = {
        'form': form,
        'object': obj,
    }
    return render(request, 'article/edit.html', context)


def article_delete(request, pk):
    obj = get_object_or_404(Article, id=pk)
    if request.method == 'POST':
        obj.delete()
        messages.error(request, 'Article successfully deleted')
        return redirect('article:list')
    context = {
        'object': obj
    }
    return render(request, 'article/delete.html', context)
