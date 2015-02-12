from django.shortcuts import render
from django.views import generic
from light_cms.models import Article

class IndexView(generic.ListView):
    template_name = 'light_cms/index.html'
    context_object_name = 'main_page'
    def get_queryset(self):
		return Article.objects.filter(is_main_page=True).first()
        
class PageView(generic.DetailView):
    model = Article
    slug_field = 'article_slug'
    slug_url_kwarg = 'article_slug'
    template_name = 'light_cms/article.html'
    
