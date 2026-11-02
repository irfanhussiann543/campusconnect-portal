import os
from datetime import date, datetime
from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app
from werkzeug.utils import secure_filename
from backend.database import db
from backend.auth import login_required
from backend.models import (
    Department, Faculty, Announcement, Event, EventRegistration,
    PlacementRecord, Recruiter, AdmissionEnquiry, AdmissionApplication,
    Document, Grievance
)

admin_bp = Blueprint("admin", __name__, url_prefix="/admin")

# Apply @login_required to all routes in admin_bp
@admin_bp.before_request
@login_required
def require_admin_login():
    pass


# 1. Admin Dashboard Overview
@admin_bp.route("/dashboard")
def dashboard():
    stats = {
        "enquiries_count": AdmissionEnquiry.query.count(),
        "applications_count": AdmissionApplication.query.count(),
        "faculty_count": Faculty.query.count(),
        "announcements_count": Announcement.query.count(),
        "events_count": Event.query.count(),
        "documents_count": Document.query.count(),
        "active_engine": current_app.config.get("ACTIVE_DB_ENGINE", "MySQL")
    }

    recent_enquiries = AdmissionEnquiry.query.order_by(AdmissionEnquiry.created_at.desc()).limit(5).all()
    recent_applications = AdmissionApplication.query.order_by(AdmissionApplication.created_at.desc()).limit(5).all()
    upcoming_events = Event.query.order_by(Event.event_date.asc()).limit(4).all()

    return render_template(
        "admin/dashboard.html",
        stats=stats,
        recent_enquiries=recent_enquiries,
        recent_applications=recent_applications,
        upcoming_events=upcoming_events
    )


# 2. Announcements CRUD
@admin_bp.route("/announcements")
def announcements():
    announcements_list = Announcement.query.order_by(Announcement.publish_date.desc()).all()
    return render_template("admin/announcements.html", announcements=announcements_list)


@admin_bp.route("/announcements/add", methods=["POST"])
def add_announcement():
    title = request.form.get("title", "").strip()
    category = request.form.get("category", "General")
    summary = request.form.get("summary", "").strip()
    content = request.form.get("content", "").strip()
    is_important = "is_important" in request.form
    is_active = "is_active" in request.form
    pub_date_str = request.form.get("publish_date")
    pub_date = date.fromisoformat(pub_date_str) if pub_date_str else date.today()

    # File attachment
    attachment_url = ""
    file = request.files.get("attachment")
    if file and file.filename:
        filename = secure_filename(file.filename)
        os.makedirs(current_app.config["UPLOAD_FOLDER"], exist_ok=True)
        file.save(os.path.join(current_app.config["UPLOAD_FOLDER"], filename))
        attachment_url = f"/static/uploads/{filename}"

    ann = Announcement(
        title=title,
        category=category,
        summary=summary,
        content=content,
        attachment_url=attachment_url,
        is_important=is_important,
        is_active=is_active,
        publish_date=pub_date
    )
    db.session.add(ann)
    db.session.commit()
    flash("Announcement published successfully!", "success")
    return redirect(url_for("admin.announcements"))


@admin_bp.route("/announcements/edit/<int:id>", methods=["POST"])
def edit_announcement(id):
    ann = Announcement.query.get_or_404(id)
    ann.title = request.form.get("title", ann.title).strip()
    ann.category = request.form.get("category", ann.category)
    ann.summary = request.form.get("summary", ann.summary).strip()
    ann.content = request.form.get("content", ann.content).strip()
    ann.is_important = "is_important" in request.form
    ann.is_active = "is_active" in request.form
    pub_date_str = request.form.get("publish_date")
    if pub_date_str:
        ann.publish_date = date.fromisoformat(pub_date_str)

    file = request.files.get("attachment")
    if file and file.filename:
        filename = secure_filename(file.filename)
        os.makedirs(current_app.config["UPLOAD_FOLDER"], exist_ok=True)
        file.save(os.path.join(current_app.config["UPLOAD_FOLDER"], filename))
        ann.attachment_url = f"/static/uploads/{filename}"

    db.session.commit()
    flash("Announcement updated successfully!", "success")
    return redirect(url_for("admin.announcements"))


@admin_bp.route("/announcements/delete/<int:id>", methods=["POST"])
def delete_announcement(id):
    ann = Announcement.query.get_or_404(id)
    db.session.delete(ann)
    db.session.commit()
    flash("Announcement removed.", "info")
    return redirect(url_for("admin.announcements"))


# 3. Events CRUD
@admin_bp.route("/events")
def events():
    events_list = Event.query.order_by(Event.event_date.desc()).all()
    return render_template("admin/events.html", events=events_list)


@admin_bp.route("/events/add", methods=["POST"])
def add_event():
    title = request.form.get("title", "").strip()
    category = request.form.get("category", "Workshop")
    description = request.form.get("description", "").strip()
    event_date_str = request.form.get("event_date")
    event_date = date.fromisoformat(event_date_str) if event_date_str else date.today()
    event_time = request.form.get("event_time", "10:00 AM - 01:00 PM")
    venue = request.form.get("venue", "Main Campus Auditorium")
    organizer = request.form.get("organizer", "CampusConnect Administration")
    max_seats = int(request.form.get("max_seats", 150))
    image_url = request.form.get("image_url", "").strip() or "https://images.unsplash.com/photo-1504384308090-c894fdcc538d?auto=format&fit=crop&w=800&q=80"
    is_featured = "is_featured" in request.form

    event = Event(
        title=title,
        category=category,
        description=description,
        event_date=event_date,
        event_time=event_time,
        venue=venue,
        organizer=organizer,
        max_seats=max_seats,
        image_url=image_url,
        is_featured=is_featured
    )
    db.session.add(event)
    db.session.commit()
    flash("Event created successfully!", "success")
    return redirect(url_for("admin.events"))


@admin_bp.route("/events/edit/<int:id>", methods=["POST"])
def edit_event(id):
    event = Event.query.get_or_404(id)
    event.title = request.form.get("title", event.title).strip()
    event.category = request.form.get("category", event.category)
    event.description = request.form.get("description", event.description).strip()
    event_date_str = request.form.get("event_date")
    if event_date_str:
        event.event_date = date.fromisoformat(event_date_str)
    event.event_time = request.form.get("event_time", event.event_time)
    event.venue = request.form.get("venue", event.venue)
    event.organizer = request.form.get("organizer", event.organizer)
    event.max_seats = int(request.form.get("max_seats", event.max_seats))
    img = request.form.get("image_url", "").strip()
    if img:
        event.image_url = img
    event.is_featured = "is_featured" in request.form

    db.session.commit()
    flash("Event updated successfully!", "success")
    return redirect(url_for("admin.events"))


@admin_bp.route("/events/delete/<int:id>", methods=["POST"])
def delete_event(id):
    event = Event.query.get_or_404(id)
    db.session.delete(event)
    db.session.commit()
    flash("Event deleted successfully.", "info")
    return redirect(url_for("admin.events"))


# 4. Faculty Management CRUD
@admin_bp.route("/faculty")
def faculty():
    faculty_list = Faculty.query.join(Department).order_by(Faculty.name.asc()).all()
    departments = Department.query.order_by(Department.name.asc()).all()
    return render_template("admin/faculty.html", faculty_list=faculty_list, departments=departments)


@admin_bp.route("/faculty/add", methods=["POST"])
def add_faculty():
    name = request.form.get("name", "").strip()
    dept_id = int(request.form.get("department_id"))
    designation = request.form.get("designation", "").strip()
    qualification = request.form.get("qualification", "").strip()
    specialization = request.form.get("specialization", "").strip()
    email = request.form.get("email", "").strip()
    phone = request.form.get("phone", "").strip()
    exp = int(request.form.get("experience_years", 1))
    photo_url = request.form.get("photo_url", "").strip() or "https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=400&q=80"
    bio = request.form.get("bio", "").strip()
    research_areas = request.form.get("research_areas", "").strip()

    fac = Faculty(
        name=name,
        department_id=dept_id,
        designation=designation,
        qualification=qualification,
        specialization=specialization,
        email=email,
        phone=phone,
        experience_years=exp,
        photo_url=photo_url,
        bio=bio,
        research_areas=research_areas
    )
    db.session.add(fac)
    db.session.commit()
    flash(f"Faculty member {name} added successfully!", "success")
    return redirect(url_for("admin.faculty"))


@admin_bp.route("/faculty/edit/<int:id>", methods=["POST"])
def edit_faculty(id):
    fac = Faculty.query.get_or_404(id)
    fac.name = request.form.get("name", fac.name).strip()
    fac.department_id = int(request.form.get("department_id", fac.department_id))
    fac.designation = request.form.get("designation", fac.designation).strip()
    fac.qualification = request.form.get("qualification", fac.qualification).strip()
    fac.specialization = request.form.get("specialization", fac.specialization).strip()
    fac.email = request.form.get("email", fac.email).strip()
    fac.phone = request.form.get("phone", fac.phone).strip()
    fac.experience_years = int(request.form.get("experience_years", fac.experience_years))
    photo = request.form.get("photo_url", "").strip()
    if photo:
        fac.photo_url = photo
    fac.bio = request.form.get("bio", fac.bio).strip()
    fac.research_areas = request.form.get("research_areas", fac.research_areas).strip()

    db.session.commit()
    flash(f"Profile for {fac.name} updated.", "success")
    return redirect(url_for("admin.faculty"))


@admin_bp.route("/faculty/delete/<int:id>", methods=["POST"])
def delete_faculty(id):
    fac = Faculty.query.get_or_404(id)
    name = fac.name
    db.session.delete(fac)
    db.session.commit()
    flash(f"Faculty member {name} has been removed.", "info")
    return redirect(url_for("admin.faculty"))


# 5. Department Information Management
@admin_bp.route("/departments")
def departments():
    dept_list = Department.query.order_by(Department.id.asc()).all()
    return render_template("admin/departments.html", departments=dept_list)


@admin_bp.route("/departments/edit/<int:id>", methods=["POST"])
def edit_department(id):
    dept = Department.query.get_or_404(id)
    dept.name = request.form.get("name", dept.name).strip()
    dept.short_intro = request.form.get("short_intro", dept.short_intro).strip()
    dept.description = request.form.get("description", dept.description).strip()
    dept.hod_name = request.form.get("hod_name", dept.hod_name).strip()
    dept.hod_email = request.form.get("hod_email", dept.hod_email).strip()
    dept.hod_qualification = request.form.get("hod_qualification", dept.hod_qualification).strip()
    dept.intake = int(request.form.get("intake", dept.intake))
    dept.labs_count = int(request.form.get("labs_count", dept.labs_count))
    dept.icon = request.form.get("icon", dept.icon).strip()

    db.session.commit()
    flash(f"Department of {dept.name} updated successfully!", "success")
    return redirect(url_for("admin.departments"))


# 6. Placement Details & Recruiters
@admin_bp.route("/placements")
def placements():
    placement_records = PlacementRecord.query.order_by(PlacementRecord.academic_year.desc()).all()
    recruiters = Recruiter.query.order_by(Recruiter.highest_pkg_offered.desc()).all()
    return render_template("admin/placements.html", records=placement_records, recruiters=recruiters)


@admin_bp.route("/placements/update-record/<int:id>", methods=["POST"])
def update_placement_record(id):
    rec = PlacementRecord.query.get_or_404(id)
    rec.total_offers = int(request.form.get("total_offers", rec.total_offers))
    rec.placed_percentage = float(request.form.get("placed_percentage", rec.placed_percentage))
    rec.highest_package_lpa = float(request.form.get("highest_package_lpa", rec.highest_package_lpa))
    rec.avg_package_lpa = float(request.form.get("avg_package_lpa", rec.avg_package_lpa))
    rec.companies_visited = int(request.form.get("companies_visited", rec.companies_visited))

    db.session.commit()
    flash(f"Placement statistics for {rec.academic_year} updated successfully!", "success")
    return redirect(url_for("admin.placements"))


@admin_bp.route("/placements/add-recruiter", methods=["POST"])
def add_recruiter():
    company = request.form.get("company_name", "").strip()
    tier = request.form.get("tier", "Tier-1")
    logo = request.form.get("logo_url", "").strip()
    roles = request.form.get("roles_offered", "").strip()
    pkg = float(request.form.get("highest_pkg_offered", 0))

    rec = Recruiter(
        company_name=company,
        tier=tier,
        logo_url=logo,
        roles_offered=roles,
        highest_pkg_offered=pkg,
        featured=True
    )
    db.session.add(rec)
    db.session.commit()
    flash(f"Recruiting partner {company} added!", "success")
    return redirect(url_for("admin.placements"))


@admin_bp.route("/placements/delete-recruiter/<int:id>", methods=["POST"])
def delete_recruiter(id):
    rec = Recruiter.query.get_or_404(id)
    name = rec.company_name
    db.session.delete(rec)
    db.session.commit()
    flash(f"Recruiter {name} removed.", "info")
    return redirect(url_for("admin.placements"))


# 7. Admission Enquiries & Applications
@admin_bp.route("/admissions")
def admissions():
    enquiries = AdmissionEnquiry.query.order_by(AdmissionEnquiry.created_at.desc()).all()
    applications = AdmissionApplication.query.order_by(AdmissionApplication.created_at.desc()).all()
    return render_template("admin/admissions.html", enquiries=enquiries, applications=applications)


@admin_bp.route("/admissions/update-enquiry/<int:id>", methods=["POST"])
def update_enquiry_status(id):
    enq = AdmissionEnquiry.query.get_or_404(id)
    enq.status = request.form.get("status", enq.status)
    enq.admin_notes = request.form.get("admin_notes", enq.admin_notes)
    db.session.commit()
    flash("Enquiry status updated.", "success")
    return redirect(url_for("admin.admissions"))


@admin_bp.route("/admissions/update-application/<int:id>", methods=["POST"])
def update_application_status(id):
    app = AdmissionApplication.query.get_or_404(id)
    app.status = request.form.get("status", app.status)
    db.session.commit()
    flash(f"Application {app.application_no} status changed to {app.status}.", "success")
    return redirect(url_for("admin.admissions"))


# 8. Document Management
@admin_bp.route("/documents")
def documents():
    docs = Document.query.order_by(Document.upload_date.desc()).all()
    return render_template("admin/documents.html", documents=docs)


@admin_bp.route("/documents/add", methods=["POST"])
def add_document():
    title = request.form.get("title", "").strip()
    category = request.form.get("category", "Syllabus")
    file_path = request.form.get("file_path", "").strip()
    file_size = request.form.get("file_size", "1.5 MB").strip()
    file_type = request.form.get("file_type", "PDF").strip()
    dept = request.form.get("department_code", "ALL").strip()
    semester = request.form.get("semester", "All").strip()

    file = request.files.get("doc_file")
    if file and file.filename:
        filename = secure_filename(file.filename)
        os.makedirs(current_app.config["UPLOAD_FOLDER"], exist_ok=True)
        file.save(os.path.join(current_app.config["UPLOAD_FOLDER"], filename))
        file_path = f"/static/uploads/{filename}"

    if not file_path:
        file_path = "/static/uploads/sample_academic_document.pdf"

    doc = Document(
        title=title,
        category=category,
        file_path=file_path,
        file_size=file_size,
        file_type=file_type,
        department_code=dept,
        semester=semester,
        upload_date=date.today()
    )
    db.session.add(doc)
    db.session.commit()
    flash(f"Document '{title}' added to repository.", "success")
    return redirect(url_for("admin.documents"))


@admin_bp.route("/documents/delete/<int:id>", methods=["POST"])
def delete_document(id):
    doc = Document.query.get_or_404(id)
    db.session.delete(doc)
    db.session.commit()
    flash("Document removed.", "info")
    return redirect(url_for("admin.documents"))
