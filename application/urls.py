import django
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import (ApplicationAdminListView,
                    ApplicationUserListView, 
                    ApplicationDetailView, 
                    ApplicaitonNewView,
                    ApplicaitonEditView,)

urlpatterns = [
    path('/<int:pk>/edit/', ApplicaitonEditView.as_view(), name='application_edit'),
    path('<int:pk>/app/new/', ApplicaitonNewView.as_view(), name='application_new'),
    path('', ApplicationAdminListView.as_view(), name='admin_application_list'),
    path('appuser', ApplicationUserListView.as_view(), name='user_application_list'),    
    path('<int:pk>', ApplicationDetailView.as_view(), name='application_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)