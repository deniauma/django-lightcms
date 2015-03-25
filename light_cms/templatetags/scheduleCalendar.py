from calendar import HTMLCalendar
from django import template
from datetime import date
from itertools import groupby

from django.utils.html import conditional_escape as esc


register = template.Library()

def do_schedule_calendar(parser, token):
	"""
	The template tag's syntax is { % schedule_calendar year month schedule_list %}
	"""
	try:
		tag_name, year, month, schedule_list = token.split_contents()
	except ValueError:
		raise template.TemplateSyntaxError, "%r tag requires three arguments" % token.contents.split()[0]
	return ScheduleCalendarNode(year, month, schedule_list)


class ScheduleCalendarNode(template.Node):
  """
 Process a particular node in the template. Fail silently.
 """
  
  def __init__(self, year, month, schedule_list):
      try:
          self.year = template.Variable(year)
          self.month = template.Variable(month)
          self.schedule_list = template.Variable(schedule_list)
      except ValueError:
          raise template.TemplateSyntaxError
      
  def render(self, context):
      try:
          # Get the variables from the context so the method is thread-safe.
          my_schedule_list = self.schedule_list.resolve(context)
          my_year = self.year.resolve(context)
          my_month = self.month.resolve(context)
          cal = ScheduleCalendar(my_schedule_list)
          return cal.formatmonth(int(my_year), int(my_month))
      except ValueError:
          return           
      except template.VariableDoesNotExist:
          return


class ScheduleCalendar(HTMLCalendar):
  """
 Overload Python's calendar.HTMLCalendar to add the appropriate reading events to
 each day's table cell.
 """
  
  def __init__(self, schedules):
      super(ScheduleCalendar, self).__init__()
      self.schedules = self.group_by_day(schedules)

  def formatday(self, day, weekday):
      if day != 0:
          cssclass = self.cssclasses[weekday]
          if date.today() == date(self.year, self.month, day):
              cssclass += ' today'
          if day in self.schedules:
              cssclass += ' filled'
              body = ['<ul>']
              for schedule in self.schedules[day]:
                  body.append('<li>')
                  body.append('<a href="%s">' % schedule.get_absolute_url())
                  body.append(esc(schedule.series.primary_name))
                  body.append('</a></li>')
              body.append('</ul>')
              return self.day_cell(cssclass, '<span class="dayNumber">%d</span> %s' % (day, ''.join(body)))
          return self.day_cell(cssclass, '<span class="dayNumberNoReadings">%d</span>' % (day))
      return self.day_cell('noday', '&nbsp;')

  def formatmonth(self, year, month):
      self.year, self.month = year, month
      return super(ScheduleCalendar, self).formatmonth(year, month)

  def group_by_day(self, schedules):
      field = lambda schedule: schedule.date_and_time.day
      return dict(
          [(day, list(items)) for day, items in groupby(schedules, field)]
      )

  def day_cell(self, cssclass, body):
      return '<td class="%s">%s</td>' % (cssclass, body)

# Register the template tag so it is available to templates
register.tag("schedule_calendar", do_schedule_calendar)
