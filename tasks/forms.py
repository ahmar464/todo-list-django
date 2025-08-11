from django import forms
from .models import Task
from django.conf import settings
from django.utils import timezone
import datetime

class TaskForm(forms.ModelForm):
    deadline = forms.DateTimeField(
        required=False,
        input_formats=['%Y-%m-%dT%H:%M'],
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
    )

    class Meta:
        model = Task
        fields = ['title', 'description', 'deadline', 'status'] 

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk and self.instance.deadline:
            dt = self.instance.deadline
            if timezone.is_aware(dt):
                dt = timezone.localtime(dt)
            self.initial['deadline'] = dt.strftime('%Y-%m-%dT%H:%M')

    def clean_deadline(self):
        dl = self.cleaned_data.get('deadline')
        if dl:
            if settings.USE_TZ and timezone.is_naive(dl):
                current_tz = timezone.get_current_timezone()
                dl = timezone.make_aware(dl, current_tz)
        return dl
