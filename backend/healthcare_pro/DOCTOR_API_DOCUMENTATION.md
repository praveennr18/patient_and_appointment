# 👨‍⚕️ HealthCare Pro - Doctor API Documentation

## 🩺 Complete Doctor Management & Dashboard APIs

This documentation covers all doctor-related endpoints for profile management, dashboard functionality, patient management, and appointment handling.

### 🆕 **Recent Updates**
- **Enhanced Appointment Management**: New appointment status tracking and patient interaction features
- **Availability Management**: Comprehensive schedule management with time slot blocking
- **Patient Communication**: Improved patient messaging and notification system
- **Performance Analytics**: Detailed analytics for appointment completion rates and patient satisfaction

---

## 🔐 **Authentication**

All doctor endpoints require JWT authentication with doctor role:

```
Authorization: Bearer <doctor_access_token>
```

---

## 👨‍⚕️ **1. Doctor Profile Management**

### **Get My Doctor Profile**
```
GET http://127.0.0.1:8000/api/doctors/my-profile/
Authorization: Bearer doctor_access_token
```

**Response:**
```json
{
    "id": "doctor_uuid",
    "doctor_id": "DOC001",
    "user": {
        "id": "user_uuid",
        "email": "dr.smith@hospital.com",
        "first_name": "John",
        "last_name": "Smith",
        "phone_number": "(555) 123-4567"
    },
    "specialization": "cardiology",
    "department": "Cardiology Department",
    "license_number": "LIC123456789",
    "years_of_experience": 15,
    "qualification": "MD, FACC - Harvard Medical School",
    "date_of_birth": "1980-05-15",
    "gender": "M",
    "phone": "(555) 123-4567",
    "address": "123 Medical Center Dr",
    "city": "New York",
    "state": "NY",
    "zip_code": "10001",
    "emergency_contact_name": "Jane Smith",
    "emergency_contact_phone": "(555) 987-6543",
    "relationship": "Spouse",
    "consultation_fee": "250.00",
    "working_days": ["monday", "tuesday", "wednesday", "thursday", "friday"],
    "start_time": "09:00:00",
    "end_time": "17:00:00",
    "is_available": true,
    "created_at": "2025-01-15T08:30:00Z",
    "updated_at": "2025-09-30T10:00:00Z"
}
```

### **Update Doctor Profile**
```
PUT http://127.0.0.1:8000/api/doctors/my-profile/
Authorization: Bearer doctor_access_token
Content-Type: application/json
```

**Request Body:**
```json
{
    "specialization": "neurology",
    "department": "Neurology Department",
    "years_of_experience": 16,
    "qualification": "MD, PhD - Johns Hopkins",
    "phone": "(555) 123-9999",
    "address": "456 Hospital Avenue",
    "city": "Boston",
    "state": "MA",
    "zip_code": "02101",
    "consultation_fee": "300.00",
    "working_days": ["monday", "tuesday", "wednesday", "thursday"],
    "start_time": "08:00:00",
    "end_time": "16:00:00"
}
```

---

## 📊 **2. Doctor Dashboard**

### **Get Dashboard Overview**
```
GET http://127.0.0.1:8000/api/doctors/dashboard/
Authorization: Bearer doctor_access_token
```

**Response:**
```json
{
    "doctor_info": {
        "name": "Dr. John Smith",
        "specialization": "Cardiology",
        "doctor_id": "DOC001",
        "total_patients": 156,
        "experience_years": 15
    },
    "today_stats": {
        "total_appointments": 8,
        "completed_appointments": 3,
        "pending_appointments": 4,
        "cancelled_appointments": 1,
        "next_appointment": {
            "time": "2:30 PM",
            "patient": "Sarah Johnson",
            "type": "Follow-up"
        }
    },
    "weekly_schedule": [
        {
            "day": "Monday",
            "appointments_count": 6,
            "available_slots": 2
        },
        {
            "day": "Tuesday", 
            "appointments_count": 8,
            "available_slots": 0
        }
    ],
    "recent_patients": [
        {
            "id": "patient_uuid",
            "name": "Sarah Johnson",
            "last_visit": "2025-09-29",
            "condition": "Hypertension",
            "next_appointment": "2025-10-05"
        }
    ]
}
```

### **Get Today's Appointments**
```
GET http://127.0.0.1:8000/api/doctors/appointments/today/
Authorization: Bearer doctor_access_token
```

**Response:**
```json
{
    "date": "2025-09-30",
    "total_appointments": 8,
    "appointments": [
        {
            "id": "appointment_uuid",
            "time": "09:00:00",
            "duration": 30,
            "patient": {
                "id": "patient_uuid",
                "name": "Sarah Johnson",
                "age": 35,
                "phone": "(555) 123-4567"
            },
            "status": "scheduled",
            "appointment_type": "consultation",
            "reason": "Regular checkup",
            "notes": "Follow-up for blood pressure"
        },
        {
            "id": "appointment_uuid_2",
            "time": "09:30:00",
            "duration": 30,
            "patient": {
                "id": "patient_uuid_2",
                "name": "Michael Brown",
                "age": 42,
                "phone": "(555) 987-6543"
            },
            "status": "in_progress",
            "appointment_type": "follow_up",
            "reason": "Lab results review",
            "notes": "Review cardiac test results"
        }
    ]
}
```

### **Get Upcoming Appointments**
```
GET http://127.0.0.1:8000/api/doctors/appointments/upcoming/
Authorization: Bearer doctor_access_token
```

**Query Parameters:**
- `days` (optional): Number of days ahead (default: 7)
- `limit` (optional): Maximum appointments to return (default: 20)

**Response:**
```json
{
    "upcoming_appointments": [
        {
            "id": "appointment_uuid",
            "date": "2025-10-01",
            "time": "10:00:00",
            "patient": {
                "name": "John Doe",
                "phone": "(555) 444-5555"
            },
            "status": "scheduled",
            "appointment_type": "consultation",
            "reason": "Initial consultation"
        }
    ],
    "total_count": 15
}
```

---

## 🔍 **3. Patient Management**

### **Get My Patients List**
```
GET http://127.0.0.1:8000/api/doctors/patients/
Authorization: Bearer doctor_access_token
```

**Query Parameters:**
- `search` (optional): Search by patient name or email
- `page` (optional): Page number for pagination
- `page_size` (optional): Number of results per page

**Response:**
```json
{
    "count": 156,
    "next": "http://127.0.0.1:8000/api/doctors/patients/?page=2",
    "previous": null,
    "results": [
        {
            "id": "patient_uuid",
            "user": {
                "first_name": "Sarah",
                "last_name": "Johnson",
                "email": "sarah.j@email.com"
            },
            "phone_number": "(555) 123-4567",
            "age": 35,
            "gender": "F",
            "blood_group": "O+",
            "last_appointment": "2025-09-25",
            "total_appointments": 8,
            "chronic_conditions": "Hypertension"
        }
    ]
}
```

### **Get Patient Details**
```
GET http://127.0.0.1:8000/api/doctors/patients/{patient_id}/
Authorization: Bearer doctor_access_token
```

**Response:**
```json
{
    "id": "patient_uuid",
    "user": {
        "first_name": "Sarah",
        "last_name": "Johnson",
        "email": "sarah.j@email.com",
        "phone_number": "(555) 123-4567"
    },
    "date_of_birth": "1988-03-15",
    "gender": "F",
    "phone_number": "(555) 123-4567",
    "address": "123 Main St, Apt 4B",
    "city": "New York",
    "state": "NY",
    "zip_code": "10001",
    "blood_group": "O+",
    "height": 165.0,
    "weight": 60.0,
    "bmi": 22.04,
    "allergies": "Penicillin, Shellfish",
    "chronic_conditions": "Hypertension",
    "current_medications": "Lisinopril 10mg daily",
    "emergency_contact_name": "Michael Johnson",
    "emergency_contact_phone": "(555) 765-4321",
    "relationship": "Husband",
    "insurance_provider": "Blue Cross Blue Shield",
    "policy_number": "BC123456789",
    "appointment_history": [
        {
            "date": "2025-09-25",
            "reason": "Regular checkup",
            "diagnosis": "Controlled hypertension",
            "notes": "Blood pressure stable"
        }
    ],
    "medical_history": [
        {
            "date": "2025-01-15",
            "diagnosis": "Essential hypertension",
            "treatment": "Lifestyle changes, medication",
            "doctor": "Dr. John Smith"
        }
    ]
}
```

### **Search Patients**
```
GET http://127.0.0.1:8000/api/doctors/patients/search/?q={search_term}
Authorization: Bearer doctor_access_token
```

**Response:**
```json
{
    "results": [
        {
            "id": "patient_uuid",
            "name": "Sarah Johnson",
            "email": "sarah.j@email.com",
            "phone": "(555) 123-4567",
            "age": 35,
            "last_appointment": "2025-09-25"
        }
    ]
}
```

---

## 📅 **4. Appointment Management**

### **Get All My Appointments**
```
GET http://127.0.0.1:8000/api/doctors/appointments/
Authorization: Bearer doctor_access_token
```

**Query Parameters:**
- `status` (optional): Filter by status (scheduled, completed, cancelled)
- `date_from` (optional): Start date filter (YYYY-MM-DD)
- `date_to` (optional): End date filter (YYYY-MM-DD)
- `patient` (optional): Filter by patient ID

### **Update Appointment Status**
```
PATCH http://127.0.0.1:8000/api/appointments/{appointment_id}/
Authorization: Bearer doctor_access_token
Content-Type: application/json
```

**Request Body:**
```json
{
    "status": "completed",
    "notes": "Patient responded well to treatment. Follow-up in 2 weeks.",
    "diagnosis": "Controlled hypertension",
    "prescription": "Continue Lisinopril 10mg daily"
}
```

### **Add Appointment Notes**
```
POST http://127.0.0.1:8000/api/appointments/{appointment_id}/notes/
Authorization: Bearer doctor_access_token
Content-Type: application/json
```

**Request Body:**
```json
{
    "notes": "Patient reports improvement in symptoms. Blood pressure: 120/80.",
    "private_notes": "Consider reducing medication dosage next visit."
}
```

---

## 🗓️ **5. Schedule Management**

### **Get My Schedule**
```
GET http://127.0.0.1:8000/api/doctors/schedule/
Authorization: Bearer doctor_access_token
```

**Query Parameters:**
- `date` (optional): Specific date (YYYY-MM-DD)
- `week` (optional): Week starting date (YYYY-MM-DD)

**Response:**
```json
{
    "working_hours": {
        "start_time": "09:00:00",
        "end_time": "17:00:00",
        "working_days": ["monday", "tuesday", "wednesday", "thursday", "friday"]
    },
    "schedule": [
        {
            "date": "2025-09-30",
            "day": "Monday",
            "slots": [
                {
                    "time": "09:00:00",
                    "status": "booked",
                    "appointment": {
                        "patient_name": "Sarah Johnson",
                        "reason": "Regular checkup"
                    }
                },
                {
                    "time": "09:30:00",
                    "status": "available"
                }
            ]
        }
    ]
}
```

### **Update Working Hours**
```
PUT http://127.0.0.1:8000/api/doctors/schedule/working-hours/
Authorization: Bearer doctor_access_token
Content-Type: application/json
```

**Request Body:**
```json
{
    "working_days": ["monday", "tuesday", "wednesday", "thursday"],
    "start_time": "08:00:00",
    "end_time": "16:00:00"
}
```

### **Block Time Slot**
```
POST http://127.0.0.1:8000/api/doctors/schedule/block/
Authorization: Bearer doctor_access_token
Content-Type: application/json
```

**Request Body:**
```json
{
    "date": "2025-10-01",
    "start_time": "12:00:00",
    "end_time": "13:00:00",
    "reason": "Lunch break"
}
```

---

## 🏥 **6. Medical Records**

### **Get Patient Medical History**
```
GET http://127.0.0.1:8000/api/doctors/patients/{patient_id}/medical-history/
Authorization: Bearer doctor_access_token
```

**Response:**
```json
{
    "patient": {
        "name": "Sarah Johnson",
        "age": 35,
        "blood_group": "O+"
    },
    "medical_history": [
        {
            "id": "history_uuid",
            "date": "2025-09-25",
            "diagnosis": "Essential hypertension",
            "symptoms": "Headache, dizziness",
            "treatment": "Prescribed Lisinopril 10mg",
            "notes": "Patient advised on dietary changes",
            "doctor": "Dr. John Smith",
            "appointment_id": "appointment_uuid"
        }
    ]
}
```

### **Add Medical Record**
```
POST http://127.0.0.1:8000/api/doctors/patients/{patient_id}/medical-history/
Authorization: Bearer doctor_access_token
Content-Type: application/json
```

**Request Body:**
```json
{
    "date": "2025-09-30",
    "diagnosis": "Controlled hypertension",
    "symptoms": "No symptoms reported",
    "treatment": "Continue current medication",
    "notes": "Blood pressure stable. Next follow-up in 3 months.",
    "prescription": "Lisinopril 10mg daily",
    "appointment_id": "appointment_uuid"
}
```

---

## 📊 **7. Analytics & Reports**

### **Get Performance Analytics**
```
GET http://127.0.0.1:8000/api/doctors/analytics/
Authorization: Bearer doctor_access_token
```

**Query Parameters:**
- `period` (optional): time period (week, month, year)
- `start_date` (optional): Custom start date
- `end_date` (optional): Custom end date

**Response:**
```json
{
    "period": "month",
    "total_appointments": 156,
    "completed_appointments": 142,
    "cancelled_appointments": 14,
    "average_rating": 4.8,
    "total_patients_treated": 89,
    "revenue": "39000.00",
    "daily_breakdown": [
        {
            "date": "2025-09-01",
            "appointments": 8,
            "revenue": "2000.00"
        }
    ],
    "top_diagnoses": [
        {
            "diagnosis": "Hypertension",
            "count": 45
        },
        {
            "diagnosis": "Diabetes",
            "count": 32
        }
    ]
}
```

### **Get Patient Statistics**
```
GET http://127.0.0.1:8000/api/doctors/patients/statistics/
Authorization: Bearer doctor_access_token
```

**Response:**
```json
{
    "total_patients": 156,
    "new_patients_this_month": 12,
    "returning_patients": 144,
    "age_distribution": {
        "0-18": 8,
        "19-35": 45,
        "36-50": 67,
        "51-65": 28,
        "65+": 8
    },
    "gender_distribution": {
        "male": 72,
        "female": 84
    },
    "most_common_conditions": [
        "Hypertension",
        "Diabetes",
        "Asthma"
    ]
}
```

---

## 🔔 **8. Notifications**

### **Get My Notifications**
```
GET http://127.0.0.1:8000/api/doctors/notifications/
Authorization: Bearer doctor_access_token
```

**Response:**
```json
{
    "unread_count": 3,
    "notifications": [
        {
            "id": "notification_uuid",
            "type": "appointment_reminder",
            "title": "Upcoming Appointment",
            "message": "Appointment with Sarah Johnson in 30 minutes",
            "created_at": "2025-09-30T09:30:00Z",
            "read": false,
            "data": {
                "appointment_id": "appointment_uuid"
            }
        },
        {
            "id": "notification_uuid_2",
            "type": "new_patient",
            "title": "New Patient Registered",
            "message": "Michael Brown has booked an appointment",
            "created_at": "2025-09-30T08:00:00Z",
            "read": true
        }
    ]
}
```

### **Mark Notification as Read**
```
PATCH http://127.0.0.1:8000/api/doctors/notifications/{notification_id}/
Authorization: Bearer doctor_access_token
Content-Type: application/json
```

**Request Body:**
```json
{
    "read": true
}
```

---

## ⚙️ **9. Settings & Preferences**

### **Get Doctor Settings**
```
GET http://127.0.0.1:8000/api/doctors/settings/
Authorization: Bearer doctor_access_token
```

**Response:**
```json
{
    "consultation_fee": "250.00",
    "appointment_duration": 30,
    "working_hours": {
        "start_time": "09:00:00",
        "end_time": "17:00:00"
    },
    "working_days": ["monday", "tuesday", "wednesday", "thursday", "friday"],
    "notifications": {
        "email_reminders": true,
        "sms_notifications": false,
        "appointment_confirmations": true
    },
    "auto_accept_appointments": false,
    "max_appointments_per_day": 16
}
```

### **Update Doctor Settings**
```
PUT http://127.0.0.1:8000/api/doctors/settings/
Authorization: Bearer doctor_access_token
Content-Type: application/json
```

**Request Body:**
```json
{
    "consultation_fee": "300.00",
    "appointment_duration": 45,
    "working_hours": {
        "start_time": "08:00:00",
        "end_time": "16:00:00"
    },
    "working_days": ["monday", "tuesday", "wednesday", "thursday"],
    "notifications": {
        "email_reminders": true,
        "sms_notifications": true,
        "appointment_confirmations": true
    },
    "auto_accept_appointments": true,
    "max_appointments_per_day": 12
}
```

---

## 🔄 **10. Common Workflows**

### **Complete Patient Consultation Flow:**

1. **Check Today's Schedule:**
   ```
   GET /api/doctors/appointments/today/
   ```

2. **Get Patient Details:**
   ```
   GET /api/doctors/patients/{patient_id}/
   ```

3. **Review Medical History:**
   ```
   GET /api/doctors/patients/{patient_id}/medical-history/
   ```

4. **Add Consultation Notes:**
   ```
   POST /api/appointments/{appointment_id}/notes/
   ```

5. **Add Medical Record:**
   ```
   POST /api/doctors/patients/{patient_id}/medical-history/
   ```

6. **Update Appointment Status:**
   ```
   PATCH /api/appointments/{appointment_id}/
   ```

### **Weekly Schedule Management:**

1. **View Weekly Schedule:**
   ```
   GET /api/doctors/schedule/?week=2025-09-30
   ```

2. **Block Time for Break:**
   ```
   POST /api/doctors/schedule/block/
   ```

3. **Update Working Hours:**
   ```
   PUT /api/doctors/schedule/working-hours/
   ```

---

## 📱 **11. Error Handling**

### **Common Error Responses:**

**401 Unauthorized:**
```json
{
    "detail": "Authentication credentials were not provided."
}
```

**403 Forbidden:**
```json
{
    "detail": "You do not have permission to perform this action."
}
```

**404 Not Found:**
```json
{
    "detail": "Patient not found."
}
```

**400 Bad Request:**
```json
{
    "field_name": ["This field is required."],
    "consultation_fee": ["Ensure this value is greater than or equal to 0."]
}
```

---

## ✅ **12. Key Features**

✅ **Complete Profile Management**: Full doctor profile CRUD operations  
✅ **Comprehensive Dashboard**: Real-time statistics and overview  
✅ **Patient Management**: Access to all patients and medical records  
✅ **Schedule Control**: Working hours, availability, and time blocking  
✅ **Appointment Handling**: Full appointment lifecycle management  
✅ **Medical Records**: Complete patient history and consultation notes  
✅ **Analytics**: Performance metrics and patient statistics  
✅ **Notifications**: Real-time alerts and reminders  
✅ **Settings**: Customizable preferences and configurations  
✅ **Role-Based Security**: Doctor-specific access control  

This comprehensive API provides complete backend support for all doctor functionality! 🩺👨‍⚕️

---

## 📚 **Usage Examples**

For testing these endpoints, you can use tools like Postman or curl. Make sure to:

1. Obtain a JWT token by logging in as a doctor
2. Include the token in the Authorization header
3. Use the correct Content-Type for POST/PUT requests
4. Handle pagination for list endpoints

**Example curl command:**
```bash
curl -X GET "http://127.0.0.1:8000/api/doctors/dashboard/" \
  -H "Authorization: Bearer your_jwt_token_here" \
  -H "Content-Type: application/json"
```