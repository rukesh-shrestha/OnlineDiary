from django.shortcuts import render
from django.views.generic import CreateView
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.views import View
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.contrib import messages
# Create your views here.

class SignUpPage(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
   
    # context_name_object = 'object'

    # def register(self,request):
    #     if request.method == "POST":
    #         form_class = CustomUserCreationForm(request.POST)
    #         email = request.POST.email
    #         print(email)
    #         if form_class.is_valid():
    #             form_class.save()
    #             return render(self.success_url)
    #         else:
    #             return render(request,'nav.html',{'form':form_class})



# inn = SignUpPage
# inn.register