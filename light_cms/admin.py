from django.contrib import admin
from light_cms.models import Article
from light_cms.models import Calendar
from light_cms.models import OpeningHours
from light_cms.models import Unavailabilities
from light_cms.models import Appointment

admin.site.register(Article)
admin.site.register(Calendar)
admin.site.register(OpeningHours)
admin.site.register(Unavailabilities)
admin.site.register(Appointment)