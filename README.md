# 🎓 CampusConnect — Modern College Information Portal

CampusConnect is a full-featured, responsive, and modern web portal designed for educational institutions. It provides a centralized digital gateway for students, faculty, prospective applicants, alumni, and administrators.

---

## 🌟 Key Features

### 🏛️ Public Portal
1. **Dynamic Homepage**:
   - High-resolution campus hero showcase with tagline and direct action buttons.
   - Breaking news and circulars ticker.
   - Animated statistics counters (Total Students, Faculty, Departments, Placement Percentage).
   - Latest announcements with category pill badges.
   - Upcoming events hub with date blocks and registration triggers.
   - Featured cards for all 6 engineering departments.
   - Corporate placement stats and Fortune 500 recruiter logos.
   - Student testimonials with alumni quotes and packages.
   - Full institutional footer with address, emails, phone numbers, and social links.

2. **About College**:
   - Institutional overview and Chancellor's message.
   - Vision & Mission statements.
   - 24-year milestone history timeline (2002 to 2026).
   - High-tech infrastructure & campus facilities (Digital Library, GPU Research Labs, Smart Classrooms, Olympic Sports Complex, Hostels, Startup Incubation Center).
   - National accreditations: NAAC 'A++' Grade (Score 3.72/4.0), NBA Tier-1, NIRF Top 30.

3. **Academic Departments (All 6 Core Disciplines)**:
   - **CSE**: Computer Science and Engineering
   - **AIDS**: Artificial Intelligence and Data Science
   - **ECE**: Electronics and Communication Engineering
   - **MECH**: Mechanical Engineering
   - **CIVIL**: Civil Engineering
   - **EEE**: Electrical and Electronics Engineering
   - Each department features:
     - Overview, vision, and HOD message with photo and direct contact.
     - Courses offered (B.Tech, M.Tech, Ph.D.) with intake details.
     - Specialized research laboratories with equipment specs.
     - Dedicated department faculty roster.
     - Student hackathon and research achievements.

4. **Academics**:
   - Undergraduate (4-Year B.Tech) and Postgraduate (2-Year M.Tech & Ph.D.) program catalogs.
   - Choice Based Credit System (CBCS) and NEP 2020 alignment.
   - 160-credit course distribution breakdown.
   - Official Academic Calendar for Odd & Even Semesters.
   - 10-point absolute grading scale and examination regulations.
   - Downloadable curriculum syllabi and academic regulations.

5. **Admissions**:
   - Transparent 4-step admission roadmap (Application ➔ Merit ➔ Counseling ➔ Enrollment).
   - Eligibility criteria for 10+2 PCM and entrance examinations.
   - Approved seat matrix for all 6 branches (780 total seats).
   - Complete annual fee structure table.
   - Chancellor's Merit Scholarships (up to 75% tuition waiver).
   - **Interactive Online Application Form**: Submits applicant data and generates unique application numbers (e.g., `CCIT-2026-XXXXX`).
   - **Quick Enquiry Form**: Real-time enquiry submission for prospective students.

6. **Faculty Directory**:
   - Interactive search bar (filters by name, specialization, or qualification).
   - Department filter pills (All, CSE, AIDS, ECE, MECH, CIVIL, EEE).
   - Faculty cards with photo, academic credentials, research focus, and contact button.
   - Modal popup displaying complete bio, experience, and research areas.

7. **Notice Board & Events Hub**:
   - Interactive category filters: *Examination, Academic, Holiday, Workshop, Seminar, Hackathon, Cultural, Sports, Circular*.
   - Keyword search across notices and events.
   - Event details page with live attendee counts and online registration form.

8. **Placements & Career Center**:
   - Year-wise placement record table (offers, %, max CTC, avg CTC, companies).
   - Recruiter directory (Google, Microsoft, Amazon, Cisco, Goldman Sachs, etc.).
   - Campus-to-Corporate 300+ hour skill training framework.
   - Placement cell contact directory.

9. **Student Corner**:
   - Quick access cards to University Portals: Student ERP, Moodle LMS, Digital Library (OPAC), Fee Payment.
   - Downloadable study materials and lecture notes organized by semester.
   - Frequently asked questions (FAQ) accordion.
   - Grievance & Suggestion Redressal Cell form.

10. **Contact & Campus Transit**:
    - Campus address, department phone lines, and email directories.
    - Embedded interactive Google Map.
    - Transit accessibility details and message dispatch form.

---

### 🔐 Admin Management Dashboard
- **Authentication**: Secure password hashing (`werkzeug.security`) with protected session cookies.
- **Default Credentials**:
  - **Username**: `admin`
  - **Password**: `admin123`
- **Dashboard Telemetry**: Real-time counter metrics for enquiries, applications, faculty, notices, events, and documents.
- **Active Engine Badge**: Displays active database engine (`MySQL` or `SQLite Mode`).
- **Announcements CRUD**: Add, edit, delete, and toggle urgent/active status.
- **Events CRUD**: Create, edit, and delete events with venue, max capacity, and registered attendee tracking.
- **Faculty Management**: Add, update credentials, change departments, and remove faculty profiles.
- **Department Manager**: Update department intro, descriptions, HOD info, intake, and lab counts.
- **Placement Manager**: Update year-wise stats and add/remove corporate recruiting partner profiles.
- **Admissions Manager**: Review incoming applications and enquiries with status workflow (*New*, *In Review*, *Approved*, *Rejected*).
- **Document Manager**: Upload and manage academic circulars, syllabus PDFs, and study materials.

---

## 🛠️ Technology Stack

- **Frontend**: HTML5, CSS3, JavaScript (ES6+), Bootstrap 5.3, FontAwesome 6, Google Fonts (`Plus Jakarta Sans`).
- **Backend**: Python 3.11, Flask 3.1, Flask-SQLAlchemy, Werkzeug, Jinja2.
- **Database**:
  - **MySQL**: Native MySQL database schema provided (`database/schema.sql` and `database/seed.sql`).
  - **PyMySQL**: High-performance pure-Python MySQL driver.
  - **Smart Fallback Engine**: If MySQL server is unreachable, the system automatically runs on local SQLite (`campusconnect.db`) with identical schema and rich seed data.

---

## 📁 Project Architecture

```
campusconnect/
├── run.py                      # Application launcher
├── requirements.txt            # Python dependencies
├── campusconnect.db            # Local SQLite database (when MySQL is not running)
│
├── backend/
│   ├── __init__.py             # Flask application factory
│   ├── config.py               # Configuration & DB connection resolver
│   ├── database.py             # Database engine & fallback handler
│   ├── models.py               # SQLAlchemy ORM models
│   ├── auth.py                 # Admin authentication routes & session protection
│   ├── routes_public.py        # Public portal routes (Home, About, Depts, Faculty, etc.)
│   ├── routes_admin.py         # Admin management CRUD controllers
│   └── seed_data.py            # Pre-populated realistic university seed dataset
│
├── database/
│   ├── schema.sql              # Pure MySQL DDL schema script
│   └── seed.sql                # Pure MySQL initial data insert script
│
├── static/
│   ├── css/
│   │   ├── style.css           # Public university stylesheet
│   │   └── admin.css           # Admin dashboard stylesheet
│   ├── js/
│   │   ├── main.js             # Public interactivity (counter, search, filters)
│   │   └── admin.js            # Admin modal handlers & table filters
│   ├── img/
│   │   └── logo.svg            # Collegiate crest SVG logo
│   └── uploads/                # Repository for PDF circulars and syllabi
│
└── templates/
    ├── base.html               # Master layout with topbar, navbar, and footer
    ├── index.html              # Homepage
    ├── about.html              # About College
    ├── departments.html        # Departments Hub
    ├── department_detail.html  # Dedicated Department View (CSE, AIDS, ECE, etc.)
    ├── academics.html          # Academics & Syllabi
    ├── admissions.html         # Admissions & Application Form
    ├── faculty.html            # Faculty Directory
    ├── events.html             # Notice Board & Events Hub
    ├── event_detail.html       # Event Details & Registration
    ├── placements.html         # Placements & Recruiters
    ├── student_corner.html     # Student Corner & FAQs
    ├── contact.html            # Contact & Location
    ├── login.html              # Admin Sign In
    └── admin/
        ├── layout.html         # Admin sidebar layout
        ├── dashboard.html      # Admin overview metrics
        ├── announcements.html  # Announcements CRUD
        ├── events.html         # Events CRUD
        ├── faculty.html        # Faculty profiles CRUD
        ├── departments.html    # Department info management
        ├── placements.html     # Placement statistics & recruiters
        ├── admissions.html     # Applications & enquiries review
        └── documents.html      # Curricular documents repository
```

---

## 🚀 Getting Started

### 1. Quick Start (Runs immediately out-of-the-box)
From the workspace root, run:
```bash
python run_campusconnect.py
```
Or navigate into `campusconnect/` and run:
```bash
python run.py
```

Open your browser at:
- **Public Website**: [http://127.0.0.1:5000](http://127.0.0.1:5000)
- **Admin Dashboard**: [http://127.0.0.1:5000/admin/login](http://127.0.0.1:5000/admin/login)
  - Username: `admin`
  - Password: `admin123`

---

### 2. Connecting to MySQL (Optional)
If you have MySQL or XAMPP/WAMP installed:
1. Ensure your MySQL service is running.
2. Create the database:
   ```bash
   mysql -u root -p < database/schema.sql
   mysql -u root -p < database/seed.sql
   ```
3. Set your environment variables (or create a `.env` file in `campusconnect/`):
   ```env
   MYSQL_HOST=localhost
   MYSQL_PORT=3306
   MYSQL_USER=root
   MYSQL_PASSWORD=your_mysql_password
   MYSQL_DB=campusconnect
   ```
4. Start the application:
   ```bash
   python run.py
   ```
   CampusConnect will detect your MySQL server and connect automatically.

---

## 📄 License
CampusConnect is an open-source educational portal project. Built with ❤️ for universities and academic institutions.
