from msilib.schema import ListView
from django.views.generic.edit import CreateView
from .models import Post
from django.views.generic.edit import UpdateView

# Create your views here.
class PostListView(ListView):
    model = Post
    
    
class PostCreateView(CreateView):
    model = Post
    fields = "__all__"
    success_url  = reverse_lazy(“blog:all”)
    
class PostDetailView(DetailView):
    model = Post
    
class PostUpdateView(UpdateView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy(“blog:all”)
    
class PostDeleteView(DeleteView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy(“blog:all”)
    
    
