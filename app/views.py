from django.shortcuts import redirect, render
from .models import Article
from .forms import ArticleForm, ContactForm
from django.contrib import messages

# Create your views here.
def index(request):
    articles = Article.objects.all()
    ctx = {'arts' : articles}
    return render(request,"index.html",ctx)

def article_add(request):
    
    if request.method == "POST":
        form = ArticleForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'Article saved to database')
            return redirect('article_add')
        else:
            messages.error(request,'Article could not be saved')
    else:
        form = ArticleForm()
    ctx = {
        "form":form,
        "title":"Add new article"
    }
    return render(request,"article_add.html",ctx)

def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"contact message submitted")
            return redirect("contact")
        else:
            messages.error(request,"contact message submission error")
    ctx = {
        'form':form,
        'title':'contact page',
    }
    return render(request,"contact.html",ctx)

