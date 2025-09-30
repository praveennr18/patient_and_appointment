from django.urls import path
from .views import doctor_views, profile_views, dashboard_views

urlpatterns = [
    # Doctor endpoints
    path('', doctor_views.DoctorListCreateView.as_view(), name='doctor_list_create'),
    path('<uuid:pk>/', doctor_views.DoctorDetailView.as_view(), name='doctor_detail'),
    path('my-profile/', profile_views.MyDoctorProfileView.as_view(), name='my_doctor_profile'),
    path('search/', doctor_views.search_doctors, name='search_doctors'),
    path('my-statistics/', profile_views.my_statistics, name='my_statistics'),
    path('specializations/', doctor_views.specializations_list, name='specializations_list'),
    
    # Doctor availability endpoints
    path('<uuid:doctor_id>/availability/', profile_views.DoctorAvailabilityView.as_view(), name='doctor_availability'),
    path('availability/<uuid:pk>/', profile_views.AvailabilityDetailView.as_view(), name='availability_detail'),
    
    # Doctor dashboard views (function-based)
    path('dashboard/', dashboard_views.doctor_dashboard, name='doctor-dashboard'),
    path('dashboard/appointments/', dashboard_views.doctor_appointments, name='doctor-appointments'),
    path('dashboard/appointments/schedule/', dashboard_views.schedule_appointment, name='schedule-appointment'),
    path('dashboard/appointments/<uuid:appointment_id>/', dashboard_views.appointment_detail, name='appointment-detail'),
    path('dashboard/patients/', dashboard_views.doctor_patients, name='doctor-patients'),
    path('dashboard/patients/<uuid:patient_id>/', dashboard_views.patient_detail_for_doctor, name='patient-detail-doctor'),
    path('dashboard/availability/', dashboard_views.doctor_availability, name='dashboard-availability'),
    path('dashboard/available-slots/', dashboard_views.available_time_slots, name='available-time-slots'),
]