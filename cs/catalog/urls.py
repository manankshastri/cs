from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('patients/', views.PatientListView.as_view(), name='patients'),
    path('patient/<int:pk>', views.PatientDetailView.as_view(), name='patient-detail'),

    path('doctors/', views.DoctorListView.as_view(), name='doctors'),
    path('doctor/<int:pk>', views.DoctorDetailView.as_view(), name='doctor-detail'),
    path('doctors/addpres', views.DoctorAddView.as_view(), name='doctor-add')
    path()
]