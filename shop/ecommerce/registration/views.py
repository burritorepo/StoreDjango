from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.views import View

# Create your views here.

class MySignUpView(View):
    form_class = UserCreationForm
    template_name = 'registration/sign_up.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():

            u = User.objects.create_user(
                form.cleaned_data.get('username'),
                '',form.cleaned_data.get('password1'),
                is_active = True
            )
            return HttpResponseRedirect('/accounts/login/?next=/')
        return render(request, self.template_name, {'form': form})

