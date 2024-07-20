from django.shortcuts import render,redirect,get_object_or_404
from .models import Blog
from course.models import Speciality
from .forms import   BlogForm,BlogUpdateForm

def blog_view(request):
    blogs = Blog.objects.all()
    specialitys = Speciality.objects.all()
    return render(request, 'blog.html', {'blogs': blogs, "specialitys": specialitys})


def blog_detail_view(request, id):
    blog = Blog.objects.get(id=id)
    specialitys = Speciality.objects.all()

    return render(request, 'blog-detail.html', {'blog': blog})

def blog_create_view(request):
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog-list')
        else:
            return render(request, 'blog_create.html', {'form': form, "message_error": "check it , there is an error!"})

    form = BlogForm()
    return render(request, 'blog_create.html', {'form': form})

def blog_update_view(request,id):
    blog=get_object_or_404(Blog,id=id)
    if request.method == "POST":
        form=BlogUpdateForm(request.POST,instance=blog)
        if form.is_valid():
            form.save()
            return redirect('blog-detail',id=blog.id)
        else:
            form=BlogUpdateForm(instance=blog)
    blog = Blog.objects.get(id=id)
    return render(request,'blog_update.html',{"blog":blog})
def blog_delete_view(request, id):
    blog = Blog.objects.get(id=id)
    blog.delete()
    return redirect('blog-list')
    return render(request, 'blog_create.html', {'form': form})


















