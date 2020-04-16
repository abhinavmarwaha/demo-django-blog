from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from .models import Post

class LatestPostsFeed(Feed):
    title = "Demo Blog"
    link = "127.0.0.1:8000"
    desccription = "New posts of demo blog"

    def items(self):
        return Post.objects.filter(status = 1)

    def item_title(self, item)
