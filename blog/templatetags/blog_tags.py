from django import template
from . .models import Post
from django.db.models import Count

register = template.Library()

@register.simple_tag
def total_posts():
    return Post.published_manager.count()

@register.inclusion_tag('blog/post/latest_posts.html')
def show_latest_posts(count=5):
    latest_posts = Post.published_manager.order_by('-published')[:count]
    return {'latest_posts': latest_posts}

@register.simple_tag
def get_most_commented_posts(count=5):
    return Post.published_manager.annotate(total_comments=Count('comments')).order_by('-total_comments')[:count]