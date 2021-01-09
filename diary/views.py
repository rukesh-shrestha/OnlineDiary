from django.shortcuts import render
from django.views.generic import DetailView,TemplateView,ListView
from django.views.generic.edit import UpdateView,DeleteView,CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from .models import Dairy
from django.contrib.messages.views import SuccessMessageMixin


# Create your views here.

class DairyPage(LoginRequiredMixin,ListView):
    model = Dairy
    login_url = 'login'
    template_name = 'dairy.html'


    
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(author=self.request.user)
        return queryset

   
    

class DairyUpdate(SuccessMessageMixin,LoginRequiredMixin,UpdateView):
    model = Dairy
    login_url = 'login'
    fields = ('title','body')
    template_name = 'update.html'

    def dispatch(self,request,*args,**kwargs):

        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request,*args,**kwargs)

    def get_success_message(self,cleaned_data):
        return cleaned_data['title'] + ' Update successfully.'


class DairyDelete(LoginRequiredMixin,DeleteView):
    model = Dairy
    login_url = 'login'
    template_name = 'delete.html'
    success_url = reverse_lazy('dairy')

    def dispatch(self,request,*args,**kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request,*args,**kwargs)

    

 

class DairyDetail(LoginRequiredMixin,DetailView):
    model = Dairy
    login_url = 'login'
    template_name = 'detail.html'

    def dispatch(self,request,*args,**kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request,*args,**kwargs)

    
    


class CreatePage(SuccessMessageMixin,LoginRequiredMixin,CreateView):
    model = Dairy
    fields = ('title','body')
    login_url = 'login'
    template_name = 'create.html'
    success_url = reverse_lazy('dairy')
    
 
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_message(self,cleaned_data):
        return cleaned_data['title'] + ' diary created successfully.'