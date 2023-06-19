
from users.models import Profile
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView)
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin)
from django.core.paginator import Paginator



def home(request):

    context = {
        'posts' : Post.objects.all()
    }
    return render(request,'blog/home.html',context)

class PostListView(ListView):
    
    model = Post
    template_name =  'blog/home.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'posts' #{{context_object_name default: object}}
    ordering = ['-date_posted']
    paginate_by = 5

class UserPostListView(ListView):
    
    model = Post
    template_name =  'blog/user_posts.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'posts' #{{context default: objectlist}}
    paginate_by = 5
    
    def get_context_data(self, **kwargs):      
        context = super().get_context_data(**kwargs) 
        user_id = User.objects.get(username = self.kwargs.get('username')).id                    
        context["user_image"] = Profile.objects.get(user = user_id).image.url
        return context

    def get_queryset(self):
        user = get_object_or_404(User, username = self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title','content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title','content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    #for userpassestestmixin check if post which the user is trying to update is his own or not
    

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post 
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    
def about(request):

    return render(request,'blog/about.html',{'title':'About'})

def landing(request):

    return render(request,'blog/landing_page.html')
#https://previews.123rf.com/images/krekdm/krekdm1607/krekdm160700086/59591887-seamless-cinema-pattern-can-be-used-for-wallpaper-website-background-wrapping-paper-cinema-vector-br.jpg
#class based view for home page
#list views, detail views, delete views, update

