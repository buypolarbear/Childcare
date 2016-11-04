from django.shortcuts import render
from app.models import Child, Profile, CheckIn_Log
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView


class ChildCreateView(CreateView):
    model = Child
    fields = ('name', 'parent', 'age', 'pin')
    success_url = '/'


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self):
        context = super().get_context_data()
        if self.request.GET:
            context['child'] = Child.object.get(code=self.request.GET.get['code'])
        return context


class ChildStatusUpdateView(UpdateView):
    model = Child
    fields = ('in_class',)
    template_name = 'app/child_status_form.html'

    def form_valid(self, form):
        instance = form.save(commit=False)
        if instance.in_class is False:
            instance.in_class = True
        else:
            instance.in_class = False
        return super().form_valid(form)
