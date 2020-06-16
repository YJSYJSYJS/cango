from django import forms
# from django.contrib.admin import widgets
from .models import Post


class DatePickerForm(forms.DateTimeInput):
    input_type = 'datetime-local'

    def __init__(self, **kwargs):
        kwargs["format"] = "%Y-%m-%dT%H:%M"
        super().__init__(**kwargs)
        return


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text', 'start_date', 'end_date')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["start_date"].widget = DatePickerForm()
        self.fields["start_date"].input_formats = ["%Y-%m-%dT%H:%M", "%Y-%m-%d %H:%M"]
        self.fields["end_date"].widget = DatePickerForm()
        self.fields["end_date"].input_formats = ["%Y-%m-%dT%H:%M", "%Y-%m-%d %H:%M"]

