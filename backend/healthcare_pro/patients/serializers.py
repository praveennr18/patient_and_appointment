from rest_framework import serializers
from .models import PatientProfile, MedicalHistory
from accounts.serializers import UserSerializer


class PatientProfileSerializer(serializers.ModelSerializer):
    """Serializer for PatientProfile model."""
    
    user = UserSerializer(read_only=True)
    age = serializers.ReadOnlyField()
    bmi = serializers.ReadOnlyField()
    full_name = serializers.SerializerMethodField()
    
    class Meta:
        model = PatientProfile
        fields = [
            'id', 'user', 'full_name', 'phone_number', 'date_of_birth', 'gender', 'age',
            'address', 'city', 'state', 'zip_code', 'blood_group', 'height', 'weight', 'bmi', 
            'allergies', 'chronic_conditions', 'current_medications', 'emergency_contact_name', 
            'emergency_contact_phone', 'relationship', 'insurance_provider', 'policy_number', 
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']
    
    def get_full_name(self, obj):
        return obj.user.get_full_name()


class PatientProfileCreateSerializer(serializers.ModelSerializer):
    """Serializer for creating PatientProfile."""
    
    email = serializers.EmailField(write_only=True)
    first_name = serializers.CharField(write_only=True)
    last_name = serializers.CharField(write_only=True)
    
    class Meta:
        model = PatientProfile
        fields = [
            'email', 'first_name', 'last_name', 'phone_number', 'date_of_birth', 
            'gender', 'address', 'city', 'state', 'zip_code', 'blood_group', 
            'height', 'weight', 'allergies', 'chronic_conditions', 'current_medications', 
            'emergency_contact_name', 'emergency_contact_phone', 'relationship', 
            'insurance_provider', 'policy_number'
        ]


class PatientProfileUpdateSerializer(serializers.ModelSerializer):
    """Serializer for updating PatientProfile."""
    
    class Meta:
        model = PatientProfile
        fields = [
            'phone_number', 'date_of_birth', 'gender', 'address', 'blood_type', 
            'height', 'weight', 'allergies', 'chronic_conditions', 'current_medications',
            'emergency_contact_name', 'emergency_contact_phone', 'emergency_contact_relationship', 
            'insurance_provider', 'insurance_policy_number'
        ]


class PatientProfileListSerializer(serializers.ModelSerializer):
    """Serializer for listing patients."""
    
    user = UserSerializer(read_only=True)
    full_name = serializers.SerializerMethodField()
    age = serializers.ReadOnlyField()
    
    class Meta:
        model = PatientProfile
        fields = [
            'id', 'user', 'full_name', 'phone_number', 'age', 'gender', 
            'blood_type', 'created_at'
        ]
    
    def get_full_name(self, obj):
        return obj.user.get_full_name()


class MedicalHistorySerializer(serializers.ModelSerializer):
    """Serializer for MedicalHistory model."""
    
    patient_name = serializers.SerializerMethodField()
    doctor_name = serializers.SerializerMethodField()
    
    class Meta:
        model = MedicalHistory
        fields = [
            'id', 'patient', 'patient_name', 'date', 'condition',
            'description', 'treatment', 'doctor', 'doctor_name',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']
    
    def get_patient_name(self, obj):
        return obj.patient.user.get_full_name()
    
    def get_doctor_name(self, obj):
        return f"Dr. {obj.doctor.user.get_full_name()}" if obj.doctor else None


class MedicalHistoryCreateSerializer(serializers.ModelSerializer):
    """Serializer for creating MedicalHistory records."""
    
    class Meta:
        model = MedicalHistory
        fields = ['date', 'condition', 'description', 'treatment', 'doctor']