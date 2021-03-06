# setup a virtual env
python3 -m venv myenv

# start env
source ~/myenv/bin/active

# create a project
django-admin startproject mysite

# runserver
python manage.py runserver 8000

# create app
python manage.py startapp polls

# Write view
from django.http import HttpResponse

def index(request):
  return HttpResponse("Hello world")

# set urls
from django.contrib import admin
from django.conf.urls import include, url

urlpatterns = [
  url(r'^polls/', include('polls.urls')),
  url(r'^admin/', admin.site.urls),
]

# setup db
# settings.py

# migrate
# models

from django.db import models

class Question(models.Model):
  question_text = models.CharField(max_length=200)
  pub_date = models.DateTimeField('date published')

# INSTALLED_APPS
python manage.py makemigrations polls

python manage.py sqlmigrate polls 0001

python manage.py migrate

# shell
python manage.py shell

# create an admin user
python manage.py createsuperuser

# admin.py
from django.contrib import admin
from .models import Question

admin.site.register(Question)

# urls

url(r'^(?P<question_id>[0-9]+)$', views.detail, name='detail')

# views

def index(request):
  latest_question_list = Question.objects.order_by("-pub_date")[:5]

  return HttpResponse(html)

# html templates
polls/templates/polls/index.html

{{ }}
{% %}

# use template

from django.shortcuts import render
from .models import Question

  return render(request, "polls/index.html", {'question': question})

from django.shortcuts import render

  question = get_object_or_404(Question, pk=question_id)

# forloop
{% for choice in question.choice_set.all %}
  <li>{{ choice.choice_text }}</li>
{% endfor %}


# update to url

{% url 'detail' question.id %}

# namespacing

app_name = 'polls'

{% url 'polls:detail' question.id %}

# write a simple form

<h1>{{ question.question_text }}</h1>

{% if error_message %}<p><strong>{{ error_message }}</strong></p>{% endif %}

<form action="{% url 'polls:vote' question.id %}" method="post">
{% csrf_token %}
{% for choice in question.choice_set.all %}
    <input type="radio" name="choice" id="choice{{ forloop.counter }}" value="{{ choice.id }}" />
    <label for="choice{{ forloop.counter }}">{{ choice.choice_text }}</label><br />
{% endfor %}
<input type="submit" value="Vote" />
</form>



# HttpResponseRedicrect
# You should always return an HttpResponseRedirect after successfully dealing with POST data

from django.core.urlresolvers import reverse
HttpResponseRedirect(reverse('polls:results', args=(question.id, )))

# use generic views : less code is better

url(r'^(?P<pk>[0-9]+)$', views.DetailView.as_view(), name='detail')

from django.views import generic

class IndexView(generic.ListView):
  template_name = 'polls/index.html'
  context_object_name = 'latest_question_list'

  def get_queryset(self):
    return Question.objects.order_by("-pub_date")[:5]

class DetailView(generic.DetailView):
  model = Question
  template_name = 'polls/detail.html'

# Test
# tests.py

from django.test import TestCase
import datetime
from django.utils import timezone
from .models import Question

class QuestionMethodTests(TestCase):
  def test_was_published_recently_with_future_question(self):
    time = timezone.now() + datetime.timedelta(days= 30)

    question = Question(pub_date = time)

    self.assertEqual(question.was_published_recently(), False)

# run tests
python manage.py test polls

# css static

polls/static/polls/style.css

{% load staticfiles %}
<link rel='stylesheet' type='text/css' herf={% static 'polls/style.css' %}>


# base html
[DjangoGirls](http://tutorial.djangogirls.org/zh/template_extending/)

{% block content %}
{% endblock %}


# post_list.html
{% extends 'blog/base.html' %}
{% extends 'blog/base.html' %}

    {% block content %}
        {% for post in posts %}
            <div class="post">
                <div class="date">
                    {{ post.published_date }}
                </div>
                <h1><a href="">{{ post.title }}</a></h1>
                <p>{{ post.text|linebreaksbr }}</p>
            </div>
        {% endfor %}
    {% endblock content %}



# static 

./manage.py collectstatic

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')


# forms

/blog/forms.py

from django import forms
from .models import Post

class PostForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = ('title', 'text',)

# post_edit.html
 {% extends 'blog/base.html' %}

 {% block content %}
 <h1>New post</h1>
 <form method="POST" class="post-form">{% csrf_token %}
  {{ form.as_p }}
  <button type="submit" class="save btn btn-default">Save</button>
</form>
 {% endblock %}


# post_new view

from django.shortcuts import redirect
from .forms import PostForm

def post_new(request):
  if request.method == 'POST':
    form = PostForm(request.POST)
    if form.is_valid():
      post = form.save(commit=False)
      post.author = request.user
      post.published_date = timezone.now()
      post.save()
      return redirect('blog.views.post_detail',pk=post.pk)
  else:
    form = PostForm()
  
  return render(request, 'blog/post_edit.html', {'form':form})


# edit post
# post detail page
<a class="btn btn-default" href="{% url 'post_edit' pk=post.pk %}"><span class="glyphicon glyphicon-pencil"></span></a>


# views
def post_new(request):
  almost the same with above

form = PostForm(request.POST, instance = post)

form = PostForm(instance = post)

# security
{% if user.is_authenticated  %}

{% endif %}
























