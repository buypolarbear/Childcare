from django.shortcuts import render
from app.models import Child, Profile, CheckIn_Log
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse, reverse_lazy
from datetime import datetime


class ChildCreateView(CreateView):
    model = Child
    fields = ('name', 'parent', 'age', 'pin')
    success_url = reverse_lazy('index_view')

    def form_valid(self, form):
        instance = form.save(commit=False)
        


class ChildUpdateView(UpdateView):
    model = Child
    fields = ('name', 'parent', 'age', 'pin')
    success_url = reverse_lazy('child_checkin_log_list_view')


class IndexView(TemplateView):
    template_name = "index.html"


class BlahView(TemplateView):
    template_name = 'blah.html'

    def get(self, request):
        pin = request.GET['pin']
        child = Child.objects.get(pin=pin)
        here = CheckIn_Log.objects.filter(child=child).first()
        if here:
            if not here.in_class:
                return HttpResponseRedirect(reverse('child_status_time_create_view', args=(child.id,)))
            return HttpResponseRedirect(reverse('child_status_update_view', args=(here.id,)))
        return HttpResponseRedirect(reverse('child_status_time_create_view', args=(child.id,)))


class ChildStatusTimeCreateView(CreateView):
    model = CheckIn_Log
    fields = ("in_class",)
    template_name = 'app/child_status_form.html'

    def get_success_url(self):
        return reverse_lazy('index_view')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["child"] = Child.objects.get(id=self.kwargs['pk'])
        return context

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.child = Child.objects.get(id=self.kwargs['pk'])
        return super().form_valid(form)


class ChildStatusUpdateView(UpdateView):
    model = CheckIn_Log
    fields = ("in_class",)
    template_name = 'app/child_status_form.html'
    success_url = reverse_lazy('index_view')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["child"] = CheckIn_Log.objects.get(id=self.kwargs['pk']).child
        return context

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.pick_up = datetime.now()
        return super().form_valid(form)


class ChildListView(ListView):
    model = Child

    def get_context_data(self):
        context = super().get_context_data()
        context['checkin_log'] = CheckIn_Log.objects.all()
        return context


class ChildCheckIn_LogListView(ListView):
    template_name = "child_checkin_log.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['child'] = Child.objects.get(id=self.kwargs['pk'])
        return context

    def get_queryset(self, **kwargs):
        child = Child.objects.get(id=self.kwargs['pk'])
        return CheckIn_Log.objects.filter(child=child)
