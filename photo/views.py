from django.shortcuts import render, redirect
from .models import Category,Photo
from .forms import PhotoForm,CategoryForm

# Create your views here.
def index(request):
    if request.GET.get('cat') :
        cat = Category.objects.get(name=request.GET['cat'])
        photo = Photo.objects.filter(category=cat)
    else:
        photo = Photo.objects.all()
    category = Category.objects.all()

    context = {
        'category': category,
        'photos': photo
    }
    return render(request,'photo/index.html',context)

def addphoto(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST,request.FILES)
        if form.is_valid() :
            form.save()
            return redirect('index')
        else:
            form = PhotoForm(request.POST,request.FILES)
    form = PhotoForm()
    formcat = CategoryForm()
    category = Category.objects.all()
    context = {
        'category': category,
        'form': form,
        'formcat': formcat
    }
    return render(request,'photo/addphoto.html',context)

def addcategory(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid() :
            form.save()

    return redirect('addphoto')

def deletephoto(request,pk):
    photo = Photo.objects.get(id=pk)
    photo.delete()
    return redirect('index')

def viewphoto(request,pk):
    photo = Photo.objects.get(id=pk)
    context = {
        'photo':photo
    }
    return render(request,'photo/viewphoto.html',context)