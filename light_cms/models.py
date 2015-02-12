from django.db import models
from django.utils.text import slugify

class Article(models.Model):
    article_title=models.CharField(max_length=200)
    article_content=models.TextField()
    creation_date=models.DateTimeField(auto_now_add=True)
    last_modified=models.DateTimeField(auto_now=True)
    is_main_page=models.BooleanField(default=False)
    article_slug=models.CharField(max_length=200, blank=True)
    def get_title(self):
        return self.article_title
    def get_content(self):
        return self.article_content
    def __str__(self):
        return self.article_title
    def save(self, *args, **kwargs):
        self.article_slug = slugify(self.article_title)
        super(Article, self).save(*args, **kwargs)
