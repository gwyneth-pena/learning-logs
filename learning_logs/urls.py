"""URLS for Learning Logs"""


from django.urls import path

from . import views

app_name = 'learning_logs'
urlpatterns = [
    path('', views.index, name='index'),
    path('topics', views.topics, name='topics'),
    path('topics/add_new', views.new_topic, name='new_topic'),
    path('topic/<int:topic_id>', views.topic, name='topic'),
    path('topic/<int:topic_id>/add_entry', views.new_entry, name='new_entry'),
]