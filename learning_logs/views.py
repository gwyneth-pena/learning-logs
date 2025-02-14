from django.shortcuts import render

from learning_logs.models import Topic

# Create your views here.
def index(request):
    return render(request, 'learning_logs/index.html')

def topics(request):
    topics = Topic.objects.order_by('-date_created')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_created')
    context = {'entries': entries, 'topic': topic}
    return render(request, 'learning_logs/topic.html', context)