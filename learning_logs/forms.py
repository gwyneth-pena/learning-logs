from django import forms

from learning_logs.models import Entry, Topic


class TopicForm(forms.ModelForm):
    
    class Meta:
        model = Topic
        fields = ["text"]
        labels = {'text': 'Topic'}


class EntryForm(forms.ModelForm):
    
    class Meta:
        model = Entry
        fields = ["text"]
        labels = {'text': 'Entry'}
        widgets = {'text': forms.Textarea(attrs={'cols':80, 'placeholder':'Write your new entry here'})}