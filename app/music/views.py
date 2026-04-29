from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Product, Artist
from .forms import CategoryForm, ProductForm, ArtistForm



def category_list_view(request):
    categories = Category.objects.all()
    context = {"title": "Список жанрів", "categories": categories}
    return render(request, 'music/category_list.html', context)

def category_detail_view(request, id):
    category = get_object_or_404(Category, id=id)
    context = {"title": f"Жанр - {category.name}", "category": category}
    return render(request, 'music/category_detail.html', context)

def category_create_view(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list') 
    else:
        form = CategoryForm()
    
    context = {"title": "Створити новий жанр", "form": form}
    return render(request, 'music/category_form.html', context)

def category_update_view(request, id):
    category = get_object_or_404(Category, id=id)
   
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm(instance=category)
        
    context = {"title": f"Редагувати жанр - {category.name}", "form": form}
    return render(request, 'music/category_form.html', context)

def category_delete_view(request, id):
    category = get_object_or_404(Category, id=id)
    if request.method == 'POST':
        category.delete()
        return redirect('category_list')
        
    context = {"title": f"Видалення жанру - {category.name}", "category": category}
    return render(request, 'music/category_confirm_delete.html', context)


def product_list_view(request):
    products = Product.objects.all()
    return render(request, 'music/product_list.html', {"title": "Список треків", "products": products})

def product_detail_view(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'music/product_detail.html', {"title": product.name, "product": product})

def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('product_list')
    return render(request, 'music/product_form.html', {"title": "Додати трек", "form": form})

def product_update_view(request, id):
    product = get_object_or_404(Product, id=id)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid():
        form.save()
        return redirect('product_list')
    return render(request, 'music/product_form.html', {"title": "Редагувати трек", "form": form})

def product_delete_view(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'music/product_confirm_delete.html', {"title": "Видалити трек", "product": product})


def artist_list_view(request):
    artists = Artist.objects.all()
    return render(request, 'music/artist_list.html', {"title": "Список виконавців", "artists": artists})

def artist_detail_view(request, id):
    artist = get_object_or_404(Artist, id=id)
    return render(request, 'music/artist_detail.html', {"title": artist.name, "artist": artist})

def artist_create_view(request):
    form = ArtistForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('artist_list')
    return render(request, 'music/artist_form.html', {"title": "Додати виконавця", "form": form})

def artist_update_view(request, id):
    artist = get_object_or_404(Artist, id=id)
    form = ArtistForm(request.POST or None, instance=artist)
    if form.is_valid():
        form.save()
        return redirect('artist_list')
    return render(request, 'music/artist_form.html', {"title": "Редагувати виконавця", "form": form})

def artist_delete_view(request, id):
    artist = get_object_or_404(Artist, id=id)
    if request.method == 'POST':
        artist.delete()
        return redirect('artist_list')
    return render(request, 'music/artist_confirm_delete.html', {"title": "Видалити виконавця", "artist": artist})