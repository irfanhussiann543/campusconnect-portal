import random
from datetime import date
from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from backend.database import db
from backend.models import (
    Department, Faculty, Announcement, Event, EventRegistration,
    PlacementRecord, Recruiter, StudentTestimonial, AdmissionEnquiry,
    AdmissionApplication, Document, Grievance
)

public_bp = Blueprint("public", __name__)

@public_bp.context_processor
def inject_global_data():
    """Injects common university data across all public templates."""
    departments = Department.query.order_by(Department.id).all()
    recent_notices = Announcement.query.filter_by(is_active=True).order_by(Announcement.publish_date.desc()).limit(5).all()
    return {
        "all_departments": departments,
        "ticker_notices": recent_notices,
        "college_name": "CampusConnect Institute of Technology",
        "college_tagline": "Autonomous Institution • Approved by AICTE • NAAC 'A++' Accredited",
        "college_phone": "+91 80 2345 6789",
        "admissions_phone": "+91 80 2345 6790",
        "college_email": "info@campusconnect.edu",
        "admissions_email": "admissions@campusconnect.edu",
        "college_address": "CampusConnect Knowledge City, Innovation Boulevard, Bengaluru, Karnataka - 560100"
    }


@public_bp.route("/")
def index():
    # Statistics
    stats = {
        "students": 12500,
        "faculty": 450,
        "departments": Department.query.count() or 6,
        "placement_pct": 98.4,
        "highest_pkg": 54.5,
        "recruiters_count": 210
    }
    
    # Latest announcements
    announcements = Announcement.query.filter_by(is_active=True).order_by(Announcement.publish_date.desc()).limit(4).all()
    
    # Upcoming events
    upcoming_events = Event.query.order_by(Event.event_date.asc()).limit(3).all()
    
    # Featured departments
    featured_depts = Department.query.filter_by(featured=True).all()
    
    # Placement highlights
    current_placement = PlacementRecord.query.filter_by(is_current=True).first()
    recruiters = Recruiter.query.filter_by(featured=True).limit(8).all()
    
    # Testimonials
    testimonials = StudentTestimonial.query.all()
    
    return render_template(
        "index.html",
        stats=stats,
        announcements=announcements,
        events=upcoming_events,
        departments=featured_depts,
        placement=current_placement,
        recruiters=recruiters,
        testimonials=testimonials
    )


@public_bp.route("/about")
def about():
    departments = Department.query.all()
    return render_template("about.html", departments=departments)


@public_bp.route("/departments")
def departments():
    departments = Department.query.order_by(Department.id).all()
    return render_template("departments.html", departments=departments)


@public_bp.route("/department/<string:code>")
def department_detail(code):
    dept = Department.query.filter_by(code=code.upper()).first_or_404()
    dept_faculty = Faculty.query.filter_by(department_id=dept.id).order_by(Faculty.experience_years.desc()).all()
    return render_template("department_detail.html", department=dept, faculty=dept_faculty)


@public_bp.route("/academics")
def academics():
    syllabus_docs = Document.query.filter_by(category="Syllabus").all()
    regulations_docs = Document.query.filter_by(category="Regulations").all()
    calendar_docs = Document.query.filter_by(category="Academic Calendar").all()
    return render_template(
        "academics.html",
        syllabus_docs=syllabus_docs,
        regulations_docs=regulations_docs,
        calendar_docs=calendar_docs
    )


@public_bp.route("/admissions", methods=["GET", "POST"])
def admissions():
    departments = Department.query.all()
    return render_template("admissions.html", departments=departments)


@public_bp.route("/admission/enquiry", methods=["POST"])
def submit_enquiry():
    name = request.form.get("student_name", "").strip()
    email = request.form.get("email", "").strip()
    phone = request.form.get("phone", "").strip()
    course = request.form.get("course_interested", "").strip()
    message = request.form.get("message", "").strip()

    if not name or not email or not phone:
        flash("Please fill in all required enquiry fields.", "danger")
        return redirect(request.referrer or url_for("public.admissions"))

    enquiry = AdmissionEnquiry(
        student_name=name,
        email=email,
        phone=phone,
        course_interested=course,
        message=message
    )
    db.session.add(enquiry)
    db.session.commit()

    flash("Thank you! Your admission enquiry has been submitted. Our counselors will contact you shortly.", "success")
    return redirect(request.referrer or url_for("public.admissions"))


@public_bp.route("/admission/apply", methods=["POST"])
def submit_application():
    try:
        full_name = request.form.get("full_name", "").strip()
        email = request.form.get("email", "").strip()
        phone = request.form.get("phone", "").strip()
        dob_str = request.form.get("dob")
        gender = request.form.get("gender")
        parent_name = request.form.get("parent_name", "").strip()
        parent_phone = request.form.get("parent_phone", "").strip()
        dept_choice = request.form.get("department_choice")
        tenth_pct = float(request.form.get("tenth_percentage", 0))
        twelfth_pct = float(request.form.get("twelfth_percentage", 0))
        entrance_score = request.form.get("entrance_score", "").strip()
        address = request.form.get("address", "").strip()

        dob = date.fromisoformat(dob_str) if dob_str else date(2005, 1, 1)

        # Generate unique Application Number
        rand_suffix = random.randint(10000, 99999)
        app_no = f"CCIT-2026-{rand_suffix}"

        application = AdmissionApplication(
            application_no=app_no,
            full_name=full_name,
            email=email,
            phone=phone,
            dob=dob,
            gender=gender,
            parent_name=parent_name,
            parent_phone=parent_phone,
            department_choice=dept_choice,
            tenth_percentage=tenth_pct,
            twelfth_percentage=twelfth_pct,
            entrance_score=entrance_score,
            address=address,
            status="Submitted"
        )
        db.session.add(application)
        db.session.commit()

        flash(f"Application Submitted Successfully! Your Application Reference Number is {app_no}. Please save this for future correspondence.", "success")
    except Exception as e:
        db.session.rollback()
        flash(f"Error submitting application: {str(e)}", "danger")

    return redirect(url_for("public.admissions"))


@public_bp.route("/faculty")
def faculty():
    dept_code = request.args.get("dept", "").strip().upper()
    search = request.args.get("q", "").strip().lower()

    query = Faculty.query.join(Department)
    if dept_code and dept_code != "ALL":
        query = query.filter(Department.code == dept_code)
    
    all_faculty = query.order_by(Faculty.name.asc()).all()
    
    if search:
        all_faculty = [
            f for f in all_faculty 
            if search in f.name.lower() or search in f.specialization.lower() or search in f.qualification.lower()
        ]

    departments = Department.query.order_by(Department.name.asc()).all()
    return render_template(
        "faculty.html",
        faculty_list=all_faculty,
        departments=departments,
        selected_dept=dept_code or "ALL",
        search_query=search
    )


@public_bp.route("/events")
def events():
    category = request.args.get("cat", "").strip()
    search = request.args.get("q", "").strip().lower()

    # Announcements query
    ann_query = Announcement.query.filter_by(is_active=True)
    if category and category != "All":
        ann_query = ann_query.filter(Announcement.category.ilike(category))
    announcements = ann_query.order_by(Announcement.publish_date.desc()).all()

    if search:
        announcements = [
            a for a in announcements
            if search in a.title.lower() or search in a.summary.lower()
        ]

    # Events query
    evt_query = Event.query
    if category and category != "All":
        evt_query = evt_query.filter(Event.category.ilike(category))
    events_list = evt_query.order_by(Event.event_date.asc()).all()

    if search:
        events_list = [
            e for e in events_list
            if search in e.title.lower() or search in e.description.lower() or search in e.organizer.lower()
        ]

    categories = ["All", "Examination", "Academic", "Holiday", "Workshop", "Seminar", "Hackathon", "Cultural", "Sports", "Circular"]

    return render_template(
        "events.html",
        announcements=announcements,
        events=events_list,
        categories=categories,
        selected_cat=category or "All",
        search_query=search
    )


@public_bp.route("/event/<int:event_id>")
def event_detail(event_id):
    event = Event.query.get_or_404(event_id)
    reg_count = EventRegistration.query.filter_by(event_id=event.id).count()
    return render_template("event_detail.html", event=event, registered_count=reg_count)


@public_bp.route("/event/<int:event_id>/register", methods=["POST"])
def event_register(event_id):
    event = Event.query.get_or_404(event_id)
    name = request.form.get("participant_name", "").strip()
    email = request.form.get("email", "").strip()
    phone = request.form.get("phone", "").strip()
    college = request.form.get("college_or_dept", "").strip()

    if not name or not email or not phone:
        flash("All fields are required to register.", "danger")
        return redirect(url_for("public.event_detail", event_id=event.id))

    # Check if duplicate email for this event
    existing = EventRegistration.query.filter_by(event_id=event.id, email=email).first()
    if existing:
        flash("You are already registered for this event!", "info")
        return redirect(url_for("public.event_detail", event_id=event.id))

    registration = EventRegistration(
        event_id=event.id,
        participant_name=name,
        email=email,
        phone=phone,
        college_or_dept=college
    )
    db.session.add(registration)
    db.session.commit()

    flash(f"Congratulations {name}! You have successfully registered for {event.title}.", "success")
    return redirect(url_for("public.event_detail", event_id=event.id))


@public_bp.route("/placements")
def placements():
    placement_history = PlacementRecord.query.order_by(PlacementRecord.academic_year.desc()).all()
    current_placement = PlacementRecord.query.filter_by(is_current=True).first()
    recruiters = Recruiter.query.order_by(Recruiter.highest_pkg_offered.desc()).all()
    testimonials = StudentTestimonial.query.all()

    return render_template(
        "placements.html",
        placements=placement_history,
        current_placement=current_placement,
        recruiters=recruiters,
        testimonials=testimonials
    )


@public_bp.route("/student-corner", methods=["GET", "POST"])
def student_corner():
    if request.method == "POST":
        # Grievance / Feedback submission
        name = request.form.get("student_name", "").strip()
        roll = request.form.get("roll_number", "").strip()
        email = request.form.get("email", "").strip()
        cat = request.form.get("category", "").strip()
        subject = request.form.get("subject", "").strip()
        desc = request.form.get("description", "").strip()

        if name and roll and desc:
            grievance = Grievance(
                student_name=name,
                roll_number=roll,
                email=email,
                category=cat,
                subject=subject,
                description=desc
            )
            db.session.add(grievance)
            db.session.commit()
            flash("Your request/feedback has been securely lodged with the Student Affairs cell.", "success")
        else:
            flash("Please fill in all required fields.", "danger")
        return redirect(url_for("public.student_corner"))

    study_materials = Document.query.filter(Document.category.in_(["Study Material", "Syllabus"])).all()
    academic_docs = Document.query.filter(Document.category.in_(["Academic Calendar", "Regulations"])).all()
    return render_template(
        "student_corner.html",
        study_materials=study_materials,
        academic_docs=academic_docs
    )


@public_bp.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        phone = request.form.get("phone", "").strip()
        subject = request.form.get("subject", "").strip()
        message = request.form.get("message", "").strip()

        # Save as enquiry
        enquiry = AdmissionEnquiry(
            student_name=name,
            email=email,
            phone=phone,
            course_interested=subject or "General Contact Inquiry",
            message=message
        )
        db.session.add(enquiry)
        db.session.commit()
        flash("Thank you for reaching out! Our administrative office will respond to your message shortly.", "success")
        return redirect(url_for("public.contact"))

    return render_template("contact.html")
