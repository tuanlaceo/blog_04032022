from django.shortcuts import render, get_object_or_404  #truy cap duoc hoac la bao loi 404
from .models import Blog

def all_blogs(request):
    blogs = Blog.objects.order_by('-date')  # sap xeo theo thu tu date
    return render(request, 'blog/all_blogs.html', {'blogs':blogs})

def detail(request, blog_id):  # khi click vao tung bai viet 1 thi se click vao ID tuong ung va se di vao detail
    blog = get_object_or_404(Blog, pk=blog_id)  # pk: primary key trong django
    return render(request, 'blog/detail.html',{'blog':blog})
