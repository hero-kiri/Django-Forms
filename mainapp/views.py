from django.shortcuts import render
from .forms import PostForm, PostModelForm
from .models import Post

# Вариант 1
def index(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            Post.objects.create(**form.cleaned_data)
    form = PostForm()
    return render(request, 'index.html', {'form': form})

# Вариант 2
def index2(request):
    if request.method == 'POST':
        form = PostModelForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            Post.objects.create(**form.cleaned_data)
    form = PostModelForm()
    return render(request, 'index2.html', {'form': form})

# Вариант 3
def index3(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        is_published = request.POST.get('is_published')
        category = request.POST.get('category')
        if is_published == 'on':
            is_published = True
        else:
            is_published = False     
        print(title, content, is_published, category)  
        
        # Сохраняем данные 
        Post.objects.create(
            title=title, 
            content=content, 
            is_published=is_published, 
            category=category) 
           
    return render(request, 'index3.html')
