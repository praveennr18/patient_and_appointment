# 🏥 HealthCare Pro - Complete Admin API Documentation

## 📋 Admin Dashboard & Management Endpoints

Based on the admin interface design, here are all the comprehensive admin endpoints for managing the healthcare system.

### 🆕 **Recent Updates**
- **Enhanced Appointment Management**: New appointment booking system with department-based scheduling
- **Real-time Analytics**: Updated dashboard with live appointment and user statistics
- **Improved Doctor Management**: Enhanced doctor registration with specialization and department management
- **Advanced Reporting**: New analytics endpoints for system performance monitoring

---

## 🔐 **Authentication**

All admin endpoints require JWT authentication with admin role:

```
Authorization: Bearer <admin_access_token>
```

---

## 📊 **1. Admin Dashboard**

### **Get Dashboard Statistics**
```
GET http://127.0.0.1:8000/api/accounts/admin/dashboard/stats/
Authorization: Bearer admin_access_token
```

**Response:**
```json
{
  "stats": {
    "total_patients": 156,
    "total_doctors": 12,
    "today_appointments": 8,
    "total_appointments": 245
  },
  "todays_schedule": [
    {
      "id": "appointment_uuid",
      "time": "09:00 AM",
      "patient_name": "John Smith",
      "doctor_name": "Dr. Sarah Wilson",
      "reason": "Consultation",
      "status": "scheduled",
      "appointment_type": "consultation"
    }
  ]
}
```

---

## 👥 **2. User Management**

### **List All Users**
```
GET http://127.0.0.1:8000/api/accounts/admin/users/
Authorization: Bearer admin_access_token
```

**Query Parameters:**
- `role`: Filter by role (admin/doctor/patient)
- `is_active`: Filter by active status (true/false)
- `search`: Search by name/email

### **Create User Account Only**
```
POST http://127.0.0.1:8000/api/accounts/admin/users/create/
Authorization: Bearer admin_access_token
Content-Type: application/json

{
    "email": "newuser@hospital.com",
    "first_name": "John",
    "last_name": "Doe",
    "role": "doctor"
}
```

### **Get User Details**
```
GET http://127.0.0.1:8000/api/accounts/admin/users/{user_id}/
Authorization: Bearer admin_access_token
```

### **Update User**
```
PUT http://127.0.0.1:8000/api/accounts/admin/users/{user_id}/
Authorization: Bearer admin_access_token
Content-Type: application/json

{
    "first_name": "Updated Name",
    "is_active": true
}
```

### **Reset User Password**
```
POST http://127.0.0.1:8000/api/accounts/admin/users/{user_id}/reset-password/
Authorization: Bearer admin_access_token
```

---

## 🩺 **3. Doctor Management**

### **Get All Doctors List**
```
GET http://127.0.0.1:8000/api/accounts/admin/doctors/list/
Authorization: Bearer admin_access_token
```

**Response:**
```json
{
  "doctors": [
    {
      "id": "doctor_uuid",
      "doctor_id": "DOC001",
      "name": "Dr. Sarah Wilson",
      "email": "sarah.wilson@hospital.com",
      "phone": "(555) 234-5678",
      "specialization": "Cardiology",
      "department": "Cardiology",
      "experience": "15 years",
      "status": "Active",
      "created_at": "2024-01-15"
    }
  ],
  "total": 12
}
```

### **Register Complete Doctor (User + Profile)**
```
POST http://127.0.0.1:8000/api/accounts/admin/register/doctor/
Authorization: Bearer admin_access_token
Content-Type: application/json

{
    // Personal Information
    "first_name": "John",
    "last_name": "Smith",
    "email": "john.smith@hospital.com",
    "phone": "(555) 123-4567",
    "date_of_birth": "1980-05-15",
    "gender": "M",
    
    // Professional Information
    "specialization": "cardiology",
    "department": "Cardiology Department",
    "years_of_experience": 10,
    "license_number": "MD123456",
    "qualification": "MD, MBBS, Cardiology Specialist",
    
    // Address Information
    "address": "123 Main Street",
    "city": "New York",
    "state": "NY",
    "zip_code": "10001",
    
    // Emergency Contact
    "emergency_contact_name": "Jane Smith",
    "emergency_contact_phone": "(555) 987-6543",
    "relationship": "Spouse",
    
    // Schedule Settings
    "working_days": ["monday", "tuesday", "wednesday", "thursday", "friday"],
    "start_time": "09:00",
    "end_time": "17:00",
    "consultation_fee": 150.00
}
```

**Response:**
```json
{
    "success": true,
    "message": "Doctor registered successfully",
    "user": {
        "id": "user_uuid",
        "email": "john.smith@hospital.com",
        "first_name": "John",
        "last_name": "Smith",
        "role": "doctor"
    },
    "doctor_id": "DOC002",
    "credentials": {
        "email": "john.smith@hospital.com",
        "password": "randomPassword123",
        "role": "doctor"
    }
}
```

---

## 🏥 **4. Patient Management**

### **Get All Patients List**
```
GET http://127.0.0.1:8000/api/accounts/admin/patients/list/
Authorization: Bearer admin_access_token
```

**Response:**
```json
{
  "patients": [
    {
      "id": "patient_uuid",
      "patient_id": "PAT001",
      "name": "Sarah Johnson",
      "email": "sarah.johnson@email.com",
      "phone": "(555) 123-4567",
      "age": "40 years",
      "gender": "Female",
      "blood_group": "A+",
      "last_visit": "3/15/2024",
      "status": "active",
      "created_at": "2024-01-10"
    }
  ],
  "total": 156
}
```

### **Register Complete Patient (User + Profile)**
```
POST http://127.0.0.1:8000/api/accounts/admin/register/patient/
Authorization: Bearer admin_access_token
Content-Type: application/json

{
    // Personal Information
    "first_name": "Sarah",
    "last_name": "Johnson",
    "email": "sarah.johnson@email.com",
    "phone_number": "(555) 123-4567",
    "date_of_birth": "1984-03-20",
    "gender": "F",
    "blood_group": "A+",
    
    // Address Information
    "address": "456 Oak Avenue",
    "city": "Los Angeles",
    "state": "CA",
    "zip_code": "90210",
    
    // Emergency Contact
    "emergency_contact_name": "Michael Johnson",
    "emergency_contact_phone": "(555) 765-4321",
    "relationship": "Husband",
    
    // Insurance Information
    "insurance_provider": "Blue Cross Blue Shield",
    "policy_number": "BC123456789"
}
```

**Response:**
```json
{
    "success": true,
    "message": "Patient registered successfully",
    "user": {
        "id": "user_uuid",
        "email": "sarah.johnson@email.com",
        "first_name": "Sarah",
        "last_name": "Johnson",
        "role": "patient"
    },
    "patient_id": "patient_uuid",
    "credentials": {
        "email": "sarah.johnson@email.com",
        "password": "randomPassword456",
        "role": "patient"
    }
}
```

---

## 📅 **5. Appointment Management**

### **Today's Appointments Overview**
Included in the dashboard stats endpoint.

### **All Appointments Management**
Use the existing appointment endpoints with admin authentication:

```
GET http://127.0.0.1:8000/api/appointments/
Authorization: Bearer admin_access_token
```

---

## 🔄 **6. Admin Workflow**

### **Complete Registration Process:**

1. **Register Patient:**
   ```
   POST /api/accounts/admin/register/patient/
   ```

2. **Register Doctor:**
   ```
   POST /api/accounts/admin/register/doctor/
   ```

3. **View Dashboard:**
   ```
   GET /api/accounts/admin/dashboard/stats/
   ```

4. **Manage Users:**
   ```
   GET /api/accounts/admin/users/
   GET /api/accounts/admin/doctors/list/
   GET /api/accounts/admin/patients/list/
   ```

---

## 📧 **7. Credential Management**

When admin registers a doctor or patient:

1. **Automatic user account creation**
2. **Random secure password generation**
3. **Complete profile creation**
4. **Email credentials delivery** (console backend for development)
5. **Return credentials in API response** for admin reference

### **Password Reset:**
```
POST http://127.0.0.1:8000/api/accounts/admin/users/{user_id}/reset-password/
```

---

## ✅ **8. Field Validation**

### **Required Fields for Doctor Registration:**
- `first_name`, `last_name`, `email`
- `specialization`, `license_number`, `years_of_experience`, `qualification`

### **Required Fields for Patient Registration:**
- `first_name`, `last_name`, `email`
- Other fields are optional but recommended

### **Optional Fields:**
- All address, emergency contact, and insurance fields
- Schedule settings for doctors

---

## 🎯 **9. Key Features**

✅ **Complete Registration Flow**: Single endpoint creates user + profile  
✅ **Automatic Credential Generation**: Secure random passwords  
✅ **Email Integration**: Credentials sent to users  
✅ **Dashboard Statistics**: Real-time overview  
✅ **Comprehensive Management**: Full CRUD operations  
✅ **Role-Based Security**: Admin-only access  
✅ **Field Flexibility**: Optional fields for gradual data entry  

This admin API provides complete backend support for the beautiful admin interface shown in the screenshots! 🚀