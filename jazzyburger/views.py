from django.shortcuts import render, redirect
from .models import Product
from django.views.generic import TemplateView, DetailView, UpdateView, FormView,DeleteView
from .forms import ProductForm, SignUpForm
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit



# Create your views here.
# creating class based view cbv
class ProductView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all().order_by('-id')
        return context


class ProductDetailView(DetailView):
    template_name = "detail.html"
    model = Product


class ProductUpdateView(UpdateView):
    template_name = 'update.html'
    model = Product
    fields = ['title', 'description', 'price', 'image']
    success_url = reverse_lazy('home')
    def form_valid(self, form):
        instance = form.save(commit=False)
        item_name = instance.title  # Retrieve the updated item's name
        instance.save()
        messages.success(self.request, f'"{item_name}" updated by!')
        return super().form_valid(form)
    
    
    
class AddProductView(FormView):
    template_name = 'addproduct.html'
    form_class = ProductForm
    success_url = reverse_lazy('home')
    
    
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        new_object = Product.objects.create(
        title = form.cleaned_data['title'],
        description = form.cleaned_data['description'],
        price = form.cleaned_data['price'],
        image = form.cleaned_data['image']         
        )
        messages.add_message(self.request, messages.SUCCESS, f' {form.cleaned_data["title"]} has been added successfully!.')        
        return super().form_valid(form)
    
# To create a user from FE 
class CreateUserView(FormView):
    template_name = 'adduser.html'
    form_class = SignUpForm
    success_url = reverse_lazy('home')  # This will redirect to home, yo can redirect to any page of your choice after successful registration

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.helper = FormHelper()
        form.helper.add_input(Submit('submit', 'Create User'))
        return form

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password1']

        new_user = User.objects.create_user(username=username)
        new_user.set_password(password)
        new_user.save()
        messages.success(self.request, f'{username} has been created!')
        
        return redirect(self.get_success_url())   
    
    
class ProductDeleteView(SuccessMessageMixin, DeleteView):
    model = Product
    template_name = 'delete.html'
    success_url = reverse_lazy('home')
    
    def get_success_message(self, cleaned_data):
        title = cleaned_data.get('title', '')
        username = self.request.user.username
        return f"Item deleted by {username}"


    

            
def logout_view(request):
     logout(request)
     return redirect('/')      

            
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome, {username}!")
            return redirect("home")
        else:
            messages.error(request, "Login failed. Please check your credentials.")
            return render(request, "login.html")
    else:
        return render(request, "login.html")
