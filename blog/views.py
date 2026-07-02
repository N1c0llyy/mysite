from django.views import generic
from .models import Post

class PostView(generic.ListView):
    model = Post
    template_name = 'blog/index.html'