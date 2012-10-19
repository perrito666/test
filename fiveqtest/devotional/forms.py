# -*- coding: utf-8 *-*
from django import forms
from devotional.models import Devotional


class DevotionalForm(forms.Form):
    month = forms.IntegerField()
    day = forms.IntegerField()

    def clean(self, *args, **kwargs):
        month = self.cleaned_data.get("month")
        day = self.cleaned_data.get("day")
        dobjects = Devotional.objects.filter(day=day, month=month)
        if not dobjects.exists():
            raise forms.ValidationError("There is no Devotional matching"
                                        " your request")
        return self.cleaned_data