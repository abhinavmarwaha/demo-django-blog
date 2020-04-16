from django.shortcuts import render , get_object_or_404
from django.views import generic
from .models import Post
from .forms import CommentForm


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

class Postdetail(requestt):
    model = Post
    template_name = 'post_detail.html'

