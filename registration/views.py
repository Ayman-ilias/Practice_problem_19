from typing import Any
from django.shortcuts import render, redirect
from .import forms
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from CarName.models import Car
from django.contrib.auth.views import LoginView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.views import PasswordChangeView

def register(request):
    if request.method == 'POST':
        register_form = forms.RegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, 'Registered successfully')
            return redirect('register')
    else:
        register_form = forms.RegistrationForm()
    return render(request, 'register.html', {'form': register_form})

class UserLoginView(LoginView):
    template_name='user_login.html'
    # success_url=reverse_lazy('home')

    def get_success_url(self):
        return reverse_lazy('home')
    

    def form_valid(self, form):
        messages.success(self.request,'Logged In Successfully ツ ')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.success(self.request,' Invalid Information ( ˘︹˘ ) ')
        return super().form_invalid(form)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Login'
        return context    

@login_required
def edit_profile(request):
    if request.method == 'POST':
        profile_form = forms.ChangeuserForm(request.POST, instance=request.user)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Profile Updated successfully')
            return redirect('edit_profile')
    else:
        profile_form = forms.ChangeuserForm(instance=request.user)
    return render(request, 'edit_profile.html', {'form': profile_form})

class EditProfileView(UpdateView):
    template_name = 'edit_profile.html'
    form_class = forms.ChangeuserForm
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        hello = super().form_valid(form)
        messages.success(self.request, 'Profile Updated successfully')
        form = self.form_class(instance=self.object) 
        return hello
    

def pass_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user,data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'PassWord Updated Successfully')
            update_session_auth_hash(request,form.user)
            return redirect('profile')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'pass_change.html', {'form': form})

class newPasswordChangeView(PasswordChangeView):
    template_name = 'pass_change.html'
    success_url = 'home'

    def form_valid(self, form):
        password = super().form_valid(form)
        messages.success(self.request, 'Password Updated Successfully')
        return password

    def form_invalid(self, form):
        messages.error(self.request, 'Invalid')
        return super().form_invalid(form)



def user_logout(request):
    logout(request)
    messages.info(request,"Logged out successfully")
    return redirect('user_login')
    

