from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import Permission, User
from django.shortcuts import render
from django.templatetags.static import static
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Property, Application, ApplicationAttachment
from django.urls import reverse_lazy

class ApplicationAdminListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Application
    template_name = 'application_list.html'
    login_url = 'login'
    permission_required = 'rentals.view_application'  

class ApplicationUserListView(LoginRequiredMixin, ListView):
    model = Application
    template_name = 'application_list.html'
    login_url = 'login'  

    def get_queryset(self):
        queryset = Application.objects.filter(applicant = self.request.user)
        return queryset      
    
class ApplicationDetailView(LoginRequiredMixin, DetailView):
    model = Application
    template_name = 'application_detail.html'
    login_url = 'login'    

class ApplicaitonNewView(LoginRequiredMixin, CreateView):
    model = Application
    template_name = 'application_new.html'
    fields = [
        "application_id",
        "property_apply",
        "applicant",      
        "social_Security_Number",
        "date_of_Birth",
        "email",
        "move_in_Date",
        "occupant1",
        "social_Security_Number1",
        "date_of_Birth1",
        "email1",
        "occupant2",
        "social_Security_Number2",
        "date_of_Birth2",
        "email2",
        "cur_employer_name",
        "cur_employer_address",
        "cur_employer_phone",
        "cur_length_of_time",
        "position",
        "supervisor",
        "income",
        "income_Frequency",
        "former_Employer",
        "former_Employer_Address",
        "former_Employer_Phone",
        "pre_position",
        "pre_length_of_time",
        "pre_supervisor",
        "pre_approx_income",
        "former_Income_Frequency",
        "other_Income",
        "income_Source",
        "pets",
        "number_of_Pets",
        "kind_of_Pet",
        "current_Address",
        "current_City",
        "current_State",
        "current_Zip",
        "current_Length_at_Address",
        "currently_Own",
        "currently_Lease",
        "current_Lease_Expiration",
        "current_Payee",
        "current_Payee_Phone",
        "former_Address",
        "former_City",
        "former_State",
        "former_Zip",
        "former_Length_at_Address",
        "former_Own",
        "former_Lease",
        "former_Lease_Expiration",
        "former_Payee",
        "former_Payee_Phone",
        "eviction",
        "foreclosure",
        "explanation",
        "emergency_Contact_Name",
        "relationship",
        "emergency_Contact_Phone",
        "emergency_Contact_Email",
        "emergency_Contact_Address",
        "emergency_Contact_City",
        "emergency_Contact_State",
        "emergency_Contact_Zip",
        "file",
    ]
    login_url = ('login')

class ApplicaitonEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Application
    template_name = 'application_edit.html'
    fields = [
        "application_id",
        "property_apply",
        "applicant",      
        "social_Security_Number",
        "date_of_Birth",
        "email",
        "move_in_Date",
        "occupant1",
        "social_Security_Number1",
        "date_of_Birth1",
        "email1",
        "occupant2",
        "social_Security_Number2",
        "date_of_Birth2",
        "email2",
        "cur_employer_name",
        "cur_employer_address",
        "cur_employer_phone",
        "cur_length_of_time",
        "position",
        "supervisor",
        "income",
        "income_Frequency",
        "former_Employer",
        "former_Employer_Address",
        "former_Employer_Phone",
        "pre_position",
        "pre_length_of_time",
        "pre_supervisor",
        "pre_approx_income",
        "former_Income_Frequency",
        "other_Income",
        "income_Source",
        "pets",
        "number_of_Pets",
        "kind_of_Pet",
        "current_Address",
        "current_City",
        "current_State",
        "current_Zip",
        "current_Length_at_Address",
        "currently_Own",
        "currently_Lease",
        "current_Lease_Expiration",
        "current_Payee",
        "current_Payee_Phone",
        "former_Address",
        "former_City",
        "former_State",
        "former_Zip",
        "former_Length_at_Address",
        "former_Own",
        "former_Lease",
        "former_Lease_Expiration",
        "former_Payee",
        "former_Payee_Phone",
        "eviction",
        "foreclosure",
        "explanation",
        "emergency_Contact_Name",
        "relationship",
        "emergency_Contact_Phone",
        "emergency_Contact_Email",
        "emergency_Contact_Address",
        "emergency_Contact_City",
        "emergency_Contact_State",
        "emergency_Contact_Zip",
        'file',
    ]
    login_url = ('login')

    def test_func(self):
        obj = self.get_object()
        return obj.applicant == self.request.user

# Create your views here.
