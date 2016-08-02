from django.shortcuts import render
from .models import Post

# Create your views here.



def trips_home(request):
    post_list = Post.objects.all()
    return render(request, 'trips/home.html', {
        'post_list': post_list,
    })

def trips_post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'trips/post.html', {'post': post})
