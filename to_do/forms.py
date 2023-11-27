from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone

from to_do.models import Todo, Tag


class TodoCreateForm(forms.ModelForm):
    tag = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Todo
        fields = ["content", "deadline", "tag"]

    def clean_deadline(self):
        data = self.cleaned_data["deadline"]
        if data:
            if data < timezone.now():
                raise ValidationError("Deadline can't be less than now")
        return data
