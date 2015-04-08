from django.shortcuts import render, render_to_response
from django.views import generic
from light_cms.models import Article, Appointment

class IndexView(generic.ListView):
    template_name = 'light_cms/index.html'
    context_object_name = 'article'
    def get_queryset(self):
		return Article.objects.filter(is_main_page=True).first()
        
class PageView(generic.DetailView):
    model = Article
    slug_field = 'article_slug'
    slug_url_kwarg = 'article_slug'
    template_name = 'light_cms/index.html'
    def get_context_data(self, **kwargs):
        context = super(PageView, self).get_context_data(**kwargs)
        schedule_events = Appointment.objects.filter(calendar=2).filter(validated=True)
        schedule_events_momentjs = []
        for event in schedule_events:
            #'2015-02-12T20:00:00'
            start_date = event.start_date.strftime('%Y-%m-%dT%H:%M:%S')
            end_date = event.end_date.strftime('%Y-%m-%dT%H:%M:%S')
            title = "Rendez-vous"
            schedule_events_momentjs.append({'start_date': start_date, 'end_date': end_date, 'title': title})
        context['schedule_events'] = schedule_events_momentjs
        return context
    
def calendar(request):
    schedule_events = Appointment.objects.filter(calendar=2).filter(validated=True)
    schedule_events_momentjs = []
    for event in schedule_events:
        #'2015-02-12T20:00:00'
        start_date = event.start_date.strftime('%Y-%m-%dT%H:%M:%S')
        end_date = event.end_date.strftime('%Y-%m-%dT%H:%M:%S')
        title = "Rendez-vous"
        schedule_events_momentjs.append({'start_date': start_date, 'end_date': end_date, 'title': title})

    return render(request, 'light_cms/calendar.html', {
        'schedule_events': schedule_events_momentjs
    })
