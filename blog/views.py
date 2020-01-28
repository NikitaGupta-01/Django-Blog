from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse , JsonResponse
from rest_framework.parsers import JSONParser
from .models import Post
from .serializers import PostSerializer 
from django.views.generic import ListView , DetailView , CreateView , UpdateView , DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin , UserPassesTestMixin
from django.contrib.auth.models import User

# Create your views here.

# posts = [
# {
# 	'author':'Nikita',
# 	'title': 'Post 1',
# 	'content': 'First post content',
# 	'date_posted': 'July,98',
# },
# {
# 	'author':'Nishant',
# 	'title': 'Post 2',
# 	'content': 'Second post content',
# 	'date_posted': 'January,93',
# }
# ]

def home(request):
	context = { 'posts' : Post.objects.all() }
	return render(request , 'blog/home.html' , context)
	# return HttpResponse('<h1>HOME</h1>')


class PostDetailViews(DetailView):
	model = Post


class PostCreateViews(LoginRequiredMixin , CreateView):
	model = Post
	fields = ['title' ,'content'] #fiels of the entries of the form in html template
	def form_valid(self,form):
		form.instance.author = self.request.user
		return super().form_valid(form)


class PostUpdateViews(LoginRequiredMixin , UserPassesTestMixin , UpdateView):
	model = Post
	fields = ['title' ,'content'] #fiels of the entries of the form in html template
	def form_valid(self,form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False


class PostDeleteViews(LoginRequiredMixin , UserPassesTestMixin ,DeleteView):
	model = Post
	success_url = '/' # redirects to home page

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False




class PostListViews(ListView):  
	model = Post     
	template_name = 'blog/home.html'
	context_object_name = 'posts'
	# ordering = ['-date_posted']
	paginate_by = 2


class UserPostListViews(ListView):
	model = Post    #only gets post from certain user
	template_name = 'blog/user_posts.html'
	context_object_name = 'posts'
	ordering = ['-date_posted']
	paginate_by = 2

	def get_quesryset(self):
		user = get_object_or_404(User , username = self.kwargs.get('username'))
		return Post.objects.filter(author=user).order_by('-date_posted')


	 
def about(request):
	return render(request , 'blog/about.html' , {'title':'About'})
	# return HttpResponse('<h1>ABOUT</h1>')



 