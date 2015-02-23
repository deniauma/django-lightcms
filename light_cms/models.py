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
    def __unicode__(self):
        return self.article_title
    def save(self, *args, **kwargs):
        self.article_slug = slugify(self.article_title)
        super(Article, self).save(*args, **kwargs)

class Calendar(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    calendar_title = models.CharField(max_length=200)

    def __unicode__(self):
        return self.calendar_title

class OpeningHours(models.Model):
    calendar = models.ForeignKey(Calendar)
    is_monday_opened = models.BooleanField(default=False)
    monday_start = models.TimeField(null=True, blank=True)
    monday_end = models.TimeField(null=True, blank=True)
    is_tuesday_opened = models.BooleanField(default=False)
    tuesday_start = models.TimeField(null=True, blank=True)
    tuesday_end = models.TimeField(null=True, blank=True)
    is_wednesday_opened = models.BooleanField(default=False)
    wednesday_start = models.TimeField(null=True, blank=True)
    wednesday_end = models.TimeField(null=True, blank=True)
    is_thursday_opened = models.BooleanField(default=False)
    thursday_start = models.TimeField(null=True, blank=True)
    thursday_end = models.TimeField(null=True, blank=True)
    is_friday_opened = models.BooleanField(default=False)
    friday_start = models.TimeField(null=True, blank=True)
    friday_end = models.TimeField(null=True, blank=True)
    is_saturday_opened = models.BooleanField(default=False)
    saturday_start = models.TimeField(null=True, blank=True)
    saturday_end = models.TimeField(null=True, blank=True)
    is_sunday_opened = models.BooleanField(default=False)
    sunday_start = models.TimeField(null=True, blank=True)
    sunday_end = models.TimeField(null=True, blank=True)

class Unavailabilities(models.Model):
    calendar = models.ForeignKey(Calendar)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    label = models.CharField(max_length=200)

class Appointment(models.Model):
    calendar = models.ForeignKey(Calendar)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    validated = models.BooleanField(default=False)