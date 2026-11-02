from datetime import datetime, date
from werkzeug.security import generate_password_hash, check_password_hash
from backend.database import db

class AdminUser(db.Model):
    __tablename__ = "admin_users"
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    full_name = db.Column(db.String(120), nullable=False)
    role = db.Column(db.String(32), default="admin")
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Department(db.Model):
    __tablename__ = "departments"
    
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(16), unique=True, nullable=False)  # e.g., CSE, AIDS, ECE
    name = db.Column(db.String(128), nullable=False)
    short_intro = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)
    hod_name = db.Column(db.String(100), nullable=False)
    hod_email = db.Column(db.String(120), nullable=False)
    hod_qualification = db.Column(db.String(120), default="Ph.D.")
    intake = db.Column(db.Integer, default=120)
    established_year = db.Column(db.Integer, default=2005)
    labs_count = db.Column(db.Integer, default=8)
    icon = db.Column(db.String(64), default="fa-laptop-code")
    featured = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    faculty_members = db.relationship("Faculty", backref="department", lazy=True, cascade="all, delete-orphan")


class Faculty(db.Model):
    __tablename__ = "faculty"
    
    id = db.Column(db.Integer, primary_key=True)
    department_id = db.Column(db.Integer, db.ForeignKey("departments.id"), nullable=False)
    name = db.Column(db.String(120), nullable=False)
    designation = db.Column(db.String(100), nullable=False)
    qualification = db.Column(db.String(150), nullable=False)
    specialization = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(32), nullable=True)
    experience_years = db.Column(db.Integer, default=5)
    photo_url = db.Column(db.String(255), default="/static/img/faculty/default.jpg")
    bio = db.Column(db.Text, nullable=True)
    research_areas = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


class Announcement(db.Model):
    __tablename__ = "announcements"
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    category = db.Column(db.String(64), nullable=False, default="General")  # Exam, Academic, Holiday, Circular, Workshop
    summary = db.Column(db.String(500), nullable=False)
    content = db.Column(db.Text, nullable=False)
    attachment_url = db.Column(db.String(255), nullable=True)
    is_important = db.Column(db.Boolean, default=False)
    is_active = db.Column(db.Boolean, default=True)
    publish_date = db.Column(db.Date, default=date.today)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


class Event(db.Model):
    __tablename__ = "events"
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    category = db.Column(db.String(64), nullable=False, default="Workshop")  # Hackathon, Workshop, Seminar, Cultural, Sports
    description = db.Column(db.Text, nullable=False)
    event_date = db.Column(db.Date, nullable=False)
    event_time = db.Column(db.String(64), nullable=False)
    venue = db.Column(db.String(150), nullable=False)
    organizer = db.Column(db.String(150), nullable=False)
    image_url = db.Column(db.String(255), default="/static/img/campus/event-default.jpg")
    max_seats = db.Column(db.Integer, default=150)
    is_featured = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    registrations = db.relationship("EventRegistration", backref="event", lazy=True, cascade="all, delete-orphan")


class EventRegistration(db.Model):
    __tablename__ = "event_registrations"
    
    id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer, db.ForeignKey("events.id"), nullable=False)
    participant_name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(32), nullable=False)
    college_or_dept = db.Column(db.String(150), nullable=False)
    registered_at = db.Column(db.DateTime, default=datetime.utcnow)


class PlacementRecord(db.Model):
    __tablename__ = "placement_records"
    
    id = db.Column(db.Integer, primary_key=True)
    academic_year = db.Column(db.String(32), unique=True, nullable=False)  # e.g., 2025-26
    total_offers = db.Column(db.Integer, nullable=False)
    placed_percentage = db.Column(db.Float, nullable=False)
    highest_package_lpa = db.Column(db.Float, nullable=False)
    avg_package_lpa = db.Column(db.Float, nullable=False)
    companies_visited = db.Column(db.Integer, nullable=False)
    is_current = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


class Recruiter(db.Model):
    __tablename__ = "recruiters"
    
    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(120), nullable=False)
    tier = db.Column(db.String(32), default="Tier-1")
    logo_url = db.Column(db.String(255), nullable=False)
    roles_offered = db.Column(db.String(255), nullable=True)
    highest_pkg_offered = db.Column(db.Float, default=0.0)
    featured = db.Column(db.Boolean, default=True)


class StudentTestimonial(db.Model):
    __tablename__ = "student_testimonials"
    
    id = db.Column(db.Integer, primary_key=True)
    student_name = db.Column(db.String(120), nullable=False)
    department = db.Column(db.String(100), nullable=False)
    graduation_year = db.Column(db.String(16), nullable=False)
    placed_company = db.Column(db.String(120), nullable=False)
    package_lpa = db.Column(db.Float, nullable=False)
    quote = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.String(255), default="/static/img/faculty/default.jpg")


class AdmissionEnquiry(db.Model):
    __tablename__ = "admission_enquiries"
    
    id = db.Column(db.Integer, primary_key=True)
    student_name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(32), nullable=False)
    course_interested = db.Column(db.String(120), nullable=False)
    message = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(32), default="New")  # New, Contacted, In Review, Closed
    admin_notes = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


class AdmissionApplication(db.Model):
    __tablename__ = "admission_applications"
    
    id = db.Column(db.Integer, primary_key=True)
    application_no = db.Column(db.String(32), unique=True, nullable=False)
    full_name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(32), nullable=False)
    dob = db.Column(db.Date, nullable=False)
    gender = db.Column(db.String(16), nullable=False)
    parent_name = db.Column(db.String(120), nullable=False)
    parent_phone = db.Column(db.String(32), nullable=False)
    department_choice = db.Column(db.String(120), nullable=False)
    tenth_percentage = db.Column(db.Float, nullable=False)
    twelfth_percentage = db.Column(db.Float, nullable=False)
    entrance_score = db.Column(db.String(64), nullable=True)
    address = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(32), default="Submitted")  # Submitted, Under Review, Approved, Rejected
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


class Document(db.Model):
    __tablename__ = "documents"
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    category = db.Column(db.String(64), nullable=False)  # Syllabus, Calendar, Regulations, Study Material
    file_path = db.Column(db.String(255), nullable=False)
    file_size = db.Column(db.String(32), default="1.5 MB")
    file_type = db.Column(db.String(16), default="PDF")
    department_code = db.Column(db.String(16), nullable=True)
    semester = db.Column(db.String(16), nullable=True)
    upload_date = db.Column(db.Date, default=date.today)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


class Grievance(db.Model):
    __tablename__ = "grievances"
    
    id = db.Column(db.Integer, primary_key=True)
    student_name = db.Column(db.String(120), nullable=False)
    roll_number = db.Column(db.String(32), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    category = db.Column(db.String(64), nullable=False)
    subject = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(32), default="Pending")  # Pending, In Progress, Resolved
    admin_reply = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
