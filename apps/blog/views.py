from django.shortcuts import render
from django.views.generic import ListView

class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'