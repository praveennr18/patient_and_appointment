from django.urls import path
from .views import patient_views, profile_views, medical_views, dashboard_views, appointment_views

urlpatterns = [
    # Patient profile endpoints
    path('', patient_views.PatientListCreateView.as_view(), name='patient-list-create'),
    path('<uuid:pk>/', patient_views.PatientDetailView.as_view(), name='patient-detail'),
    
    # Patient dashboard and self-service endpoints
    path('my/dashboard/', dashboard_views.patient_dashboard, name='patient-dashboard'),
    path('my/profile/', dashboard_views.my_profile, name='my-patient-profile'),
    path('my/profile/update/', dashboard_views.update_profile, name='update-patient-profile'),
    path('my/appointments/', appointment_views.my_appointments, name='patient-my-appointments'),
    path('my/appointments/<uuid:appointment_id>/', appointment_views.get_appointment_detail, name='patient-appointment-detail'),
    path('my/medical-history/', dashboard_views.my_medical_history, name='my-medical-history'),
    path('my/health-summary/', dashboard_views.health_summary, name='health-summary'),
    
    # Available doctors for appointment booking
    path('doctors/available/', dashboard_views.available_doctors, name='available-doctors'),
    
    # Medical history endpoints (admin/doctor access)
    path('<uuid:patient_id>/medical-history/', medical_views.MedicalHistoryListCreateView.as_view(), name='medical-history-list'),
    path('medical-history/<uuid:pk>/', medical_views.MedicalHistoryDetailView.as_view(), name='medical-history-detail'),
]