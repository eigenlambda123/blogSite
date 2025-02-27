from django import template
from . .models import Post

register = template.Library()

@register.simple_tag
def total_posts():
    return Post.published_manager.count()

@register.inclusion_tag('blog/post/latest_posts.html')
def show_latest_posts(count=5):
    latest_posts = Post.published_manager.order_by('-published')[:count]
    return {'latest_posts': latest_posts}