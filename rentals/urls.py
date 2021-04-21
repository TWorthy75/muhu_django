import django
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import (RentalListView, 
                    RentalDetailView, 
                    RentalNewView, 
                    RentalEditView, 
                    RentalDeleteView, 
)

urlpatterns = [ 
    path('<int:pk>/delete/', RentalDeleteView.as_view(), name='rental_delete'),
    path('<int:pk>/edit/', RentalEditView.as_view(), name='rental_edit'),
    path('new/', RentalNewView.as_view(), name='rental_new'),
    path('<int:pk>', RentalDetailView.as_view(), name='rental_detail'),
    path('', RentalListView.as_view(), name='rental_list'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)