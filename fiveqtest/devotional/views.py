# Create your views here.
from django.shortcuts import redirect
from django.views.generic.edit import FormView
from django.views.generic.detail import DetailView
from devotional.forms import DevotionalForm
from devotional.models import Devotional


class DevotionalFormView(FormView):
    success_url = ""
    form_class = DevotionalForm
    template_name = "devotional/form.html"

    def form_valid(self, form):
        month = form.cleaned_data["month"]
        day = form.cleaned_data["day"]
        dobject = Devotional.objects.get(day=day, month=month)
        return redirect("detail_view", pk=dobject.pk)


detail_form = DevotionalFormView.as_view()


class DevotionalView(DetailView):
    model = Devotional
    template_name = "devotional/detail.html"

detail = DevotionalView.as_view()


class DevotionalWordcountView(DetailView):
    model = Devotional
    template_name = "devotional/wordcount.html"

wordcount = DevotionalWordcountView.as_view()