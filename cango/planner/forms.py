from django import forms
from django.contrib.admin import widgets
from .models import Post


class DatePickerForm(forms.DateTimeInput):
    input_type = 'date'
    # input_type = 'time'


class TimePickerForm(forms.TimeInput):
    input_type = 'time'


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text', 'start_date', 'start_time', 'end_time', 'end_date')

        widgets = {'start_date': DatePickerForm(), 'end_date': DatePickerForm(),
                   'start_time': TimePickerForm(), 'end_time': TimePickerForm()}



