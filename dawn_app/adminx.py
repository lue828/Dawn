import xadmin
from dawn_app.models import Author, Blog, Tag


class AuthorAdmin(object):
    """docstring for AuthorAdmin"""
    list_display = ('name', 'email', 'website')
    search_fields = ('name',)


class BlogAdmin(object):
    """docstring for BlogAdmin"""
    list_display = ('caption', 'id', 'author', 'publish_time')
    list_filter = ('publish_time',)
    date_hierarchy = 'publish_time'
    ordering = ('-publish_time',)
    filter_horizontal = ('tags',)


xadmin.site.register(Author, AuthorAdmin)
xadmin.site.register(Blog, BlogAdmin)
xadmin.site.register(Tag)