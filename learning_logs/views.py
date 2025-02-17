from django.http import Http404
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from learning_logs.forms import EntryForm, TopicForm
from learning_logs.models import Entry, Topic

# Create your views here.
def index(request):
    return render(request, 'learning_logs/index.html')

@login_required
def topics(request):
    topics = Topic.objects.filter(user=request.user).order_by('-date_created')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

@login_required
def topic(request, topic_id):
    try:
        topic = Topic.objects.get(id=topic_id, user=request.user)
        entries = topic.entry_set.order_by('-date_created')
        context = {'entries': entries, 'topic': topic}
    except:
        raise Http404
    else:
        return render(request, 'learning_logs/topic.html', context)

@login_required
def new_topic(request):
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.user = request.user
            new_topic.save()
            return redirect('learning_logs:topics') 
    context = {'form' : form}
    return render(request, 'learning_logs/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id=topic_id)
        
    context = {'form': form, 'topic': topic}
    return render(request, 'learning_logs/new_entry.html', context)

@login_required
def edit_entry(request, topic_id, entry_id):
    entry = Entry.objects.get(id=entry_id)

    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id=topic_id)
    context = {'form': form, 'entry': entry}
    return render(request, 'learning_logs/edit_entry.html', context)