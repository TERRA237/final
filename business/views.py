from django.shortcuts import render,redirect
from django.urls import reverse
from django.views.generic import CreateView,UpdateView,ListView,DetailView,DeleteView,View,TemplateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from.models import BusinessPlan
from .forms import UserCreationForm, LoginForm
from django.contrib import messages
from .forms import BusinessPlanModelForm


# signup page
def user_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('bussiness:login'))
    else:
        form = UserCreationForm()
    return render(request, 'business/signup.html', {'form': form})

# login page
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)    
                return redirect(reverse('business:homepage'))
            messages.warning(request, "Invalid Credentials.")
    else:
        form = LoginForm()
    return render(request, 'business/login.html', {'form': form})

# logout page
def user_logout(request):
    logout(request)
    return redirect(reverse('business:login'))


class HomePage(LoginRequiredMixin,TemplateView):
    template_name ='business/main.html'


class CreateBusinessPlan(LoginRequiredMixin,CreateView):
    template_name ='business/create_business.html'
    model = BusinessPlan
    form_class = BusinessPlanModelForm

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class UpdateBusinessPlan(LoginRequiredMixin,UpdateView):
    pass

class BusinessPlanDetailView(LoginRequiredMixin, DetailView):
    context_object_name = "business_plan"
    queryset = BusinessPlan.objects.all()

class DeleteBusinessPlanView(LoginRequiredMixin,DeleteView):
    pass

class ListBusinessPlansView(LoginRequiredMixin,ListView):
    model = BusinessPlan
    context_object_name = "business_plans"
    template_name = 'business/create_business.html'
'''
    queryset = BusinessPlan.objects.order_by("-publication_date")
'''



