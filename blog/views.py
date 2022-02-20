from django.views.generic import ListView, DetailView 

from blog.models import Post

# Create your views here.

class PostList(ListView):
    model = Post
    context_object_name = 'posts' #追加

class PostDetail(DetailView):
    model = Post
    context_object_name = 'post' #追加
