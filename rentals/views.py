import django
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import Permission, User
from django.shortcuts import render
from django.templatetags.static import static
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Property, PropertyPhoto
from django.urls import reverse_lazy

class RentalListView(LoginRequiredMixin, ListView):
    model = Property
    template_name = 'rental_list.html'
    login_url = 'login'

class RentalDetailView(LoginRequiredMixin, DetailView):
    model = Property
    template_name = 'rental_detail.html'
    login_url = 'login'

class RentalNewView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Property
    template_name = 'rental_new.html'
    fields = [
        'property_id',
        'rent',
        'num_bed',
        'num_bath',
        'address',
        'p_type',
        'desc',
        'photo',
    ]
    login_url = ('login')
    permission_required = ('rentals.add_property')


class RentalEditView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Property
    template_name = 'rental_edit.html'
    fields = [
        'property_id',
        'rent',
        'num_bed',
        'num_bath',
        'address',
        'p_type',
        'desc',
        'photo',
    ]
    login_url = 'login'
    permission_required = ('rentals.change_property')

class RentalDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Property
    template_name = 'rental_delete.html'
    success_url = reverse_lazy('home')
    login_url = 'login'
    permission_required = ('rentals.delete_property')


# Create your views here.
