"""
🎓 CampusConnect — Modern College Information Portal
Built for Streamlit Community Cloud Deployment
"""

import streamlit as st
import sqlite3
import os
import random
from datetime import date, datetime

# --- Page Configuration ---
st.set_page_config(
    page_title="CampusConnect — Premier Institute of Technology",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Path to Database ---
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DB_PATH = os.path.join(BASE_DIR, "campusconnect", "campusconnect.db")
if not os.path.exists(os.path.dirname(DB_PATH)):
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)

def get_db():
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn

# --- Custom University Styling ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif;
    }
    
    .main {
        background-color: #f8fafc;
    }
    
    /* Brand Header Banner */
    .brand-banner {
        background: linear-gradient(135deg, #07162c 0%, #1a488e 100%);
        color: white;
        padding: 24px 30px;
        border-radius: 16px;
        margin-bottom: 25px;
        box-shadow: 0 10px 25px rgba(7, 22, 44, 0.15);
        display: flex;
        align-items: center;
        justify-content: space-between;
        flex-wrap: wrap;
        gap: 15px;
    }
    .brand-title {
        font-size: 2rem;
        font-weight: 800;
        margin: 0;
        color: white;
        letter-spacing: -0.5px;
    }
    .brand-sub {
        font-size: 0.9rem;
        color: #fbbf24;
        font-weight: 600;
        margin: 0;
    }
    
    /* Stat Cards */
    .stat-box {
        background: white;
        border: 1px solid #e2e8f0;
        border-radius: 14px;
        padding: 20px;
        text-align: center;
        box-shadow: 0 4px 12px rgba(15, 23, 42, 0.04);
        transition: transform 0.2s;
    }
    .stat-val {
        font-size: 2.2rem;
        font-weight: 800;
        color: #1a488e;
        line-height: 1;
        margin-bottom: 5px;
    }
    .stat-lbl {
        font-size: 0.85rem;
        color: #64748b;
        font-weight: 600;
    }
    
    /* Card Container */
    .portal-card {
        background: white;
        border: 1px solid #e2e8f0;
        border-radius: 14px;
        padding: 22px;
        margin-bottom: 18px;
        box-shadow: 0 4px 12px rgba(15, 23, 42, 0.03);
    }
    
    /* Badges */
    .badge-blue {
        background-color: #e0f2fe;
        color: #0369a1;
        padding: 4px 10px;
        border-radius: 20px;
        font-size: 0.75rem;
        font-weight: 700;
        display: inline-block;
    }
    .badge-gold {
        background-color: #fef3c7;
        color: #b45309;
        padding: 4px 10px;
        border-radius: 20px;
        font-size: 0.75rem;
        font-weight: 700;
        display: inline-block;
    }
    .badge-green {
        background-color: #dcfce7;
        color: #15803d;
        padding: 4px 10px;
        border-radius: 20px;
        font-size: 0.75rem;
        font-weight: 700;
        display: inline-block;
    }
</style>
""", unsafe_allow_html=True)

# --- Top Header ---
st.markdown("""
<div class="brand-banner">
    <div>
        <h1 class="brand-title">🎓 CampusConnect</h1>
        <p class="brand-sub">INSTITUTE OF TECHNOLOGY • NAAC 'A++' (3.72/4) • NBA TIER-1 ACCREDITED</p>
    </div>
    <div>
        <span class="badge-gold">Autonomous Institution</span>
        <span class="badge-blue">NIRF Top 30</span>
    </div>
</div>
""", unsafe_allow_html=True)

# --- Sidebar Navigation ---
with st.sidebar:
    st.markdown('<img src="https://upload.wikimedia.org/wikipedia/commons/2/2f/Google_2015_logo.svg" width="110" style="margin-bottom:10px;">', unsafe_allow_html=True)
    st.markdown("### 🏛️ Navigation")
    menu = st.radio(
        "Go to",
        [
            "🏠 Home",
            "🏛️ About Us",
            "📚 Departments",
            "🎓 Academics",
            "📝 Admissions",
            "👨‍🏫 Faculty Directory",
            "📢 Events & Notices",
            "💼 Placements",
            "🎒 Student Corner",
            "📞 Contact Us",
            "🔐 Admin Portal"
        ],
        label_visibility="collapsed"
    )
    
    st.markdown("---")
    st.markdown("**Admissions Helpline:**")
    st.markdown("📞 `+91 80 2345 6789`")
    st.markdown("📧 `admissions@campusconnect.edu`")
    st.markdown("---")
    st.caption("CampusConnect Portal © 2026")

conn = get_db()

# ==============================================================================
# 1. HOME PAGE
# ==============================================================================
if menu == "🏠 Home":
    st.markdown("### Empowering Minds, Engineering Tomorrow")
    st.write(
        "Welcome to **CampusConnect Institute of Technology** — a premier autonomous citadel of innovation, "
        "interdisciplinary research, and academic rigor nurturing global engineering leaders."
    )
    
    # Animated Statistics Counters
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown("""<div class="stat-box"><div class="stat-val">12,500+</div><div class="stat-lbl">Enrolled Students</div></div>""", unsafe_allow_html=True)
    with c2:
        st.markdown("""<div class="stat-box"><div class="stat-val">450+</div><div class="stat-lbl">Distinguished Faculty</div></div>""", unsafe_allow_html=True)
    with c3:
        st.markdown("""<div class="stat-box"><div class="stat-val">6</div><div class="stat-lbl">Core Departments</div></div>""", unsafe_allow_html=True)
    with c4:
        st.markdown("""<div class="stat-box"><div class="stat-val">98.4%</div><div class="stat-lbl">Placement Track Record</div></div>""", unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Latest Announcements & Upcoming Events
    col_left, col_right = st.columns(2)
    
    with col_left:
        st.markdown("#### 📢 Latest Announcements")
        try:
            notices = conn.execute("SELECT * FROM announcements WHERE is_active=1 ORDER BY publish_date DESC LIMIT 3").fetchall()
            for n in notices:
                urgent_badge = '<span class="badge-gold">Urgent</span>' if n['is_important'] else ''
                st.markdown(f"""
                <div class="portal-card">
                    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
                        <span class="badge-blue">{n['category']}</span>
                        <small style="color:#64748b;">{n['publish_date']}</small>
                    </div>
                    <h5 style="color:#07162c; margin-bottom:6px; font-weight:700;">{n['title']} {urgent_badge}</h5>
                    <p style="color:#475569; font-size:0.9rem; margin:0;">{n['summary']}</p>
                </div>
                """, unsafe_allow_html=True)
        except Exception:
            st.info("No announcements logged yet.")
            
    with col_right:
        st.markdown("#### 📅 Upcoming Events & Hackathons")
        try:
            events = conn.execute("SELECT * FROM events ORDER BY event_date ASC LIMIT 3").fetchall()
            for e in events:
                st.markdown(f"""
                <div class="portal-card">
                    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
                        <span class="badge-green">{e['category']}</span>
                        <small style="color:#64748b;">{e['event_date']} • {e['event_time']}</small>
                    </div>
                    <h5 style="color:#07162c; margin-bottom:6px; font-weight:700;">{e['title']}</h5>
                    <p style="color:#475569; font-size:0.85rem; margin-bottom:8px;">📍 <strong>Venue:</strong> {e['venue']}</p>
                    <p style="color:#64748b; font-size:0.85rem; margin:0;">Organizer: {e['organizer']}</p>
                </div>
                """, unsafe_allow_html=True)
        except Exception:
            st.info("No upcoming events logged yet.")

    st.markdown("---")
    
    # Placement Highlights
    st.markdown("#### 💼 Placement Highlights")
    p1, p2, p3, p4 = st.columns(4)
    p1.metric("Highest Package", "₹54.5 LPA", "Google")
    p2.metric("Average Package", "₹8.4 LPA", "+12% YoY")
    p3.metric("Total Job Offers", "1,280+", "2025-26 Batch")
    p4.metric("Partner Companies", "210+", "Tier-1 Tech Giants")
    
    st.markdown("##### 🤝 Prestigious Recruiting Partners")
    st.markdown("`Google` • `Microsoft` • `Amazon` • `Cisco` • `Goldman Sachs` • `Oracle` • `TCS` • `Infosys` • `Qualcomm` • `Adobe`")

# ==============================================================================
# 2. ABOUT US
# ==============================================================================
elif menu == "🏛️ About Us":
    st.markdown("### About CampusConnect Institute of Technology")
    st.markdown(
        "Established in 2002, CampusConnect Institute of Technology is an autonomous, premier engineering institution "
        "sprawling across 75 acres of state-of-the-art academic infrastructure."
    )
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="portal-card">
            <h4 style="color:#1a488e;">🎯 Our Vision</h4>
            <p style="color:#475569;">
                To be a globally admired center of holistic technological higher education and translational research,
                producing visionary engineers committed to societal progress and sustainable industrial innovation.
            </p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="portal-card">
            <h4 style="color:#b45309;">🚀 Our Mission</h4>
            <p style="color:#475569;">
                To provide student-centric, experiential learning grounded in fundamentals, powered by advanced infrastructure,
                and enriched by continuous industrial co-creation and entrepreneurial incubation.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
    st.markdown("#### 🏛️ Campus Infrastructure & World-Class Facilities")
    f1, f2, f3 = st.columns(3)
    f1.markdown("**📖 Central Digital Library**\n110,000+ volumes, 15,000+ IEEE/ACM journals, 24/7 silent study lounges.")
    f2.markdown("**🔬 Advanced R&D Labs**\n50+ specialized labs with NVIDIA GPU compute clusters and Cadence VLSI EDA.")
    f3.markdown("**🏟️ Olympic Sports Complex**\nSynthetic running track, floodlit turf, indoor basketball and badminton courts.")
    
    st.markdown("#### 🏆 Institutional Accreditations")
    st.success("✅ **NAAC 'A++' Grade** (Score 3.72/4.0)")
    st.info("✅ **NBA Tier-1 (Washington Accord)** for all 6 Engineering Disciplines")
    st.warning("✅ **NIRF Ranked Top 30** Engineering Institution")

# ==============================================================================
# 3. DEPARTMENTS
# ==============================================================================
elif menu == "📚 Departments":
    st.markdown("### Academic Engineering Departments")
    try:
        depts = conn.execute("SELECT * FROM departments ORDER BY id ASC").fetchall()
        dept_names = [d['name'] for d in depts]
        selected_dept_name = st.selectbox("Select Department to Explore:", dept_names)
        
        dept = next((d for d in depts if d['name'] == selected_dept_name), depts[0])
        
        st.markdown(f"#### Department of {dept['name']} ({dept['code']})")
        st.markdown(f"<span class=\"badge-blue\">Code: {dept['code']}</span> <span class=\"badge-gold\">Annual Intake: {dept['intake']} Seats</span> <span class=\"badge-green\">Active Labs: {dept['labs_count']}</span>", unsafe_allow_html=True)
        
        st.markdown(f"**Overview:** {dept['description']}")
        
        st.markdown(f"**Head of Department:** {dept['hod_name']} ({dept['hod_qualification']})")
        st.markdown(f"**HOD Email:** `{dept['hod_email']}`")
        
        st.markdown("##### 👨‍🏫 Department Faculty")
        facs = conn.execute("SELECT * FROM faculty WHERE department_id=? ORDER BY experience_years DESC", (dept['id'],)).fetchall()
        for f in facs:
            st.markdown(f"- **{f['name']}** — {f['designation']} ({f['qualification']})\n  *Specialization:* {f['specialization']} | 📧 `{f['email']}`")
    except Exception as e:
        st.error(f"Error loading departments: {e}")

# ==============================================================================
# 4. ACADEMICS
# ==============================================================================
elif menu == "🎓 Academics":
    st.markdown("### Academic Programs & Curriculum Framework")
    st.markdown(
        "CampusConnect follows the **Choice Based Credit System (CBCS)** aligned with the **National Education Policy (NEP 2020)**. "
        "Undergraduate students complete a comprehensive 160-credit framework including core disciplines, open electives, and industrial internships."
    )
    
    st.markdown("#### 📚 Programs Offered")
    t1, t2 = st.tabs(["Undergraduate (B.Tech - 4 Years)", "Postgraduate (M.Tech - 2 Years & Ph.D.)"])
    with t1:
        st.markdown("""
        - B.Tech in **Computer Science and Engineering** (180 Seats)
        - B.Tech in **Artificial Intelligence and Data Science** (120 Seats)
        - B.Tech in **Electronics and Communication Engineering** (180 Seats)
        - B.Tech in **Mechanical Engineering** (120 Seats)
        - B.Tech in **Civil Engineering** (60 Seats)
        - B.Tech in **Electrical and Electronics Engineering** (120 Seats)
        """)
    with t2:
        st.markdown("""
        - M.Tech in **Cloud Computing & Distributed Architectures** (24 Seats)
        - M.Tech in **VLSI System Design & Microelectronics** (24 Seats)
        - M.Tech in **Renewable Energy & Smart Grid Systems** (24 Seats)
        - Ph.D. in **Engineering & Computational Sciences** (Full-time / Part-time)
        """)
        
    st.markdown("#### 📅 Academic Calendar 2026-2027")
    st.markdown("""
    | Date | Milestone / Event |
    | :--- | :--- |
    | **Aug 03, 2026** | Commencement of Odd Semester Instruction |
    | **Oct 15, 2026** | Continuous Internal Assessment (CIA-I) & Practical Mid-Terms |
    | **Dec 01, 2026** | Autonomous End-Semester Comprehensive Examinations |
    | **Jan 08, 2027** | Commencement of Even Semester 2027 |
    """)

# ==============================================================================
# 5. ADMISSIONS
# ==============================================================================
elif menu == "📝 Admissions":
    st.markdown("### Admissions 2026-2027")
    st.markdown(
        "Applications are invited from eligible candidates for merit-based and sports quota engineering seats."
    )
    
    tab_apply, tab_enquire, tab_info = st.tabs(["📄 Online Application Form", "💬 Quick Enquiry", "ℹ️ Eligibility & Fees"])
    
    with tab_apply:
        st.markdown("##### Official Admission Application Form")
        with st.form("admission_form"):
            name = st.text_input("Applicant Full Name (as per 10th Certificate) *")
            col_a, col_b = st.columns(2)
            email = col_a.text_input("Email Address *")
            phone = col_b.text_input("Mobile Number (WhatsApp Enabled) *")
            
            col_c, col_d = st.columns(2)
            dob = col_c.date_input("Date of Birth", min_value=date(1995, 1, 1), max_value=date(2010, 12, 31), value=date(2005, 5, 15))
            gender = col_d.selectbox("Gender", ["Male", "Female", "Other"])
            
            parent_name = st.text_input("Parent / Guardian Name *")
            parent_phone = st.text_input("Parent Mobile Number *")
            
            dept_choice = st.selectbox(
                "Preferred Department Choice *",
                [
                    "Computer Science and Engineering (CSE)",
                    "Artificial Intelligence and Data Science (AIDS)",
                    "Electronics and Communication Engineering (ECE)",
                    "Mechanical Engineering (MECH)",
                    "Civil Engineering (CIVIL)",
                    "Electrical and Electronics Engineering (EEE)"
                ]
            )
            
            col_e, col_f = st.columns(2)
            tenth = col_e.number_input("10th Standard Percentage (%)", min_value=40.0, max_value=100.0, value=90.0, step=0.1)
            twelfth = col_f.number_input("12th / +2 PCM Percentage (%)", min_value=40.0, max_value=100.0, value=88.5, step=0.1)
            
            entrance_score = st.text_input("Entrance Exam Score (e.g. JEE Main 94.2 %ile or KCET Rank 4120)")
            address = st.text_area("Residential Permanent Address *")
            
            submitted = st.form_submit_button("Submit Online Application", use_container_width=True)
            
            if submitted:
                if name and email and phone and address:
                    app_no = f"CCIT-2026-{random.randint(10000, 99999)}"
                    conn.execute("""
                        INSERT INTO admission_applications 
                        (application_no, full_name, email, phone, dob, gender, parent_name, parent_phone, department_choice, tenth_percentage, twelfth_percentage, entrance_score, address, status, created_at)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 'Submitted', ?)
                    """, (app_no, name, email, phone, str(dob), gender, parent_name, parent_phone, dept_choice, tenth, twelfth, entrance_score, address, datetime.utcnow()))
                    conn.commit()
                    st.success(f"🎉 Application Submitted Successfully! Your Reference Application Number is: **{app_no}**")
                else:
                    st.error("Please fill in all mandatory fields.")

    with tab_enquire:
        st.markdown("##### Quick Admission Enquiry")
        with st.form("enquiry_form"):
            enq_name = st.text_input("Your Name *")
            enq_email = st.text_input("Email *")
            enq_phone = st.text_input("Mobile Phone *")
            enq_course = st.selectbox("Program of Interest", [
                "B.Tech Computer Science & Engg",
                "B.Tech AI & Data Science",
                "B.Tech Electronics & Comm",
                "B.Tech Mechanical Engg",
                "B.Tech Civil Engg",
                "B.Tech Electrical & Electronics",
                "M.Tech / Ph.D. Programs"
            ])
            enq_msg = st.text_area("Your Query Message")
            enq_submit = st.form_submit_button("Send Enquiry")
            
            if enq_submit:
                if enq_name and enq_email and enq_phone:
                    conn.execute("""
                        INSERT INTO admission_enquiries (student_name, email, phone, course_interested, message, status, created_at)
                        VALUES (?, ?, ?, ?, ?, 'New', ?)
                    """, (enq_name, enq_email, enq_phone, enq_course, enq_msg, datetime.utcnow()))
                    conn.commit()
                    st.success("✅ Thank you! Our admissions counseling cell will contact you within 24 hours.")
                else:
                    st.error("Please fill in Name, Email, and Phone.")
                    
    with tab_info:
        st.markdown("##### Eligibility Criteria")
        st.markdown("- Passed 10+2 with Physics, Chemistry, and Mathematics (PCM) with a minimum aggregate of 60%.")
        st.markdown("- Accepted Entrances: JEE Main, State CET, COMEDK, or CampusConnect Aptitude Test.")
        
        st.markdown("##### Annual Academic Tuition Fee")
        st.markdown("""
        | Branch Category | Annual Tuition | Lab & Tech Fee | Total 1st Year |
        | :--- | :--- | :--- | :--- |
        | **CSE / AI&DS** | ₹1,45,000 | ₹25,000 | **₹1,95,000** |
        | **ECE / EEE** | ₹1,25,000 | ₹22,000 | **₹1,72,000** |
        | **MECH / CIVIL** | ₹1,05,000 | ₹20,000 | **₹1,50,000** |
        """)
        st.info("💡 **Chancellor's Merit Scholarships:** Up to 75% tuition fee waiver for candidates securing 95%+ in 10+2 PCM.")

# ==============================================================================
# 6. FACULTY DIRECTORY
# ==============================================================================
elif menu == "👨‍🏫 Faculty Directory":
    st.markdown("### Distinguished Faculty & Research Scholars")
    
    col_search, col_dept = st.columns([2, 1])
    search_q = col_search.text_input("🔍 Search by name, specialization, or qualification:")
    
    depts = conn.execute("SELECT * FROM departments ORDER BY code ASC").fetchall()
    dept_options = ["ALL"] + [d['code'] for d in depts]
    filter_dept = col_dept.selectbox("Filter Department:", dept_options)
    
    query = """
        SELECT f.*, d.code as dept_code, d.name as dept_name 
        FROM faculty f 
        JOIN departments d ON f.department_id = d.id
        WHERE 1=1
    """
    params = []
    if filter_dept != "ALL":
        query += " AND d.code = ?"
        params.append(filter_dept)
    if search_q:
        query += " AND (f.name LIKE ? OR f.specialization LIKE ? OR f.qualification LIKE ?)"
        s = f"%{search_q}%"
        params.extend([s, s, s])
        
    facs = conn.execute(query, params).fetchall()
    
    st.markdown(f"Found **{len(facs)}** faculty profiles matching your criteria.")
    
    for f in facs:
        with st.container():
            st.markdown(f"""
            <div class="portal-card">
                <div style="display:flex; justify-content:space-between; align-items:start;">
                    <div>
                        <h4 style="color:#07162c; margin-bottom:2px; font-weight:800;">{f['name']}</h4>
                        <div style="color:#1a488e; font-weight:600; font-size:0.9rem; margin-bottom:4px;">{f['designation']} • Department of {f['dept_name']}</div>
                        <div style="color:#64748b; font-size:0.85rem;"><i class="fa fa-graduation-cap"></i> {f['qualification']}</div>
                    </div>
                    <span class="badge-blue">{f['dept_code']}</span>
                </div>
                <hr style="margin:10px 0;">
                <p style="color:#334155; font-size:0.88rem; margin-bottom:6px;"><strong>Focus Areas:</strong> {f['specialization']}</p>
                <div style="font-size:0.84rem; color:#64748b;">
                    📧 <strong>Email:</strong> <a href="mailto:{f['email']}">{f['email']}</a> | ⏳ <strong>Experience:</strong> {f['experience_years']} Years
                </div>
            </div>
            """, unsafe_allow_html=True)

# ==============================================================================
# 7. EVENTS & NOTICE BOARD
# ==============================================================================
elif menu == "📢 Events & Notices":
    st.markdown("### Notice Board & Events Hub")
    
    tab_notices, tab_events = st.tabs(["📢 Official Notices", "🎉 Upcoming Events"])
    
    with tab_notices:
        notices = conn.execute("SELECT * FROM announcements ORDER BY publish_date DESC").fetchall()
        for n in notices:
            with st.expander(f"📌 {n['title']} ({n['publish_date']})"):
                st.markdown(f"<span class=\"badge-blue\">{n['category']}</span>", unsafe_allow_html=True)
                st.write(n['content'])
                if n['summary']:
                    st.caption(f"Summary: {n['summary']}")

    with tab_events:
        events = conn.execute("SELECT * FROM events ORDER BY event_date ASC").fetchall()
        for e in events:
            with st.container():
                st.markdown(f"""
                <div class="portal-card">
                    <span class="badge-green">{e['category']}</span>
                    <h4 style="color:#07162c; margin-top:8px;">{e['title']}</h4>
                    <p style="color:#475569;">{e['description']}</p>
                    <p style="color:#1a488e; font-size:0.88rem;">
                        📅 <strong>Date:</strong> {e['event_date']} ({e['event_time']})<br>
                        📍 <strong>Venue:</strong> {e['venue']}<br>
                        👥 <strong>Organizer:</strong> {e['organizer']}
                    </p>
                </div>
                """, unsafe_allow_html=True)
                
                # Registration for this event
                with st.expander(f"Register for {e['title']}"):
                    with st.form(f"reg_form_{e['id']}"):
                        reg_name = st.text_input("Your Name *")
                        reg_email = st.text_input("Your Email *")
                        reg_phone = st.text_input("Mobile Phone *")
                        reg_college = st.text_input("College / Dept *")
                        if st.form_submit_button("Confirm Registration"):
                            if reg_name and reg_email and reg_phone:
                                conn.execute("""
                                    INSERT INTO event_registrations (event_id, participant_name, email, phone, college_or_dept, registered_at)
                                    VALUES (?, ?, ?, ?, ?, ?)
                                """, (e['id'], reg_name, reg_email, reg_phone, reg_college, datetime.utcnow()))
                                conn.commit()
                                st.success(f"🎉 Registered for {e['title']} successfully!")

# ==============================================================================
# 8. PLACEMENTS
# ==============================================================================
elif menu == "💼 Placements":
    st.markdown("### Centre for Corporate Relations & Placements")
    
    c1, c2, c3 = st.columns(3)
    c1.metric("Highest Package", "₹54.5 LPA", "Google")
    c2.metric("Average CTC", "₹8.4 LPA", "2025-26")
    c3.metric("Placement Rate", "98.4%", "Audited")
    
    st.markdown("#### 📊 Audited Batch Placement Statistics")
    records = conn.execute("SELECT * FROM placement_records ORDER BY academic_year DESC").fetchall()
    st.table([
        {
            "Academic Batch": r['academic_year'],
            "Total Offers": r['total_offers'],
            "Placement %": f"{r['placed_percentage']}%",
            "Highest CTC (LPA)": f"₹{r['highest_package_lpa']} LPA",
            "Average CTC (LPA)": f"₹{r['avg_package_lpa']} LPA",
            "Companies Visited": r['companies_visited']
        }
        for r in records
    ])
    
    st.markdown("#### 🤝 Premier Recruiting Partners")
    recruiters = conn.execute("SELECT * FROM recruiters ORDER BY highest_pkg_offered DESC").fetchall()
    r_cols = st.columns(4)
    for idx, rc in enumerate(recruiters):
        with r_cols[idx % 4]:
            st.markdown(f"""
            <div class="portal-card" style="text-align:center;">
                <h5 style="color:#07162c; margin-bottom:4px;">{rc['company_name']}</h5>
                <span class="badge-blue">{rc['tier']}</span>
                <p style="color:#64748b; font-size:0.8rem; margin-top:6px;">Max: ₹{rc['highest_pkg_offered']} LPA</p>
            </div>
            """, unsafe_allow_html=True)

# ==============================================================================
# 9. STUDENT CORNER
# ==============================================================================
elif menu == "🎒 Student Corner":
    st.markdown("### Student Corner & Digital Repositories")
    
    q1, q2, q3, q4 = st.columns(4)
    q1.markdown("""<div class="stat-box"><div style="font-size:1.8rem;">💻</div><div class="stat-lbl">Student ERP</div></div>""", unsafe_allow_html=True)
    q2.markdown("""<div class="stat-box"><div style="font-size:1.8rem;">🎓</div><div class="stat-lbl">Moodle LMS</div></div>""", unsafe_allow_html=True)
    q3.markdown("""<div class="stat-box"><div style="font-size:1.8rem;">📖</div><div class="stat-lbl">Digital Library</div></div>""", unsafe_allow_html=True)
    q4.markdown("""<div class="stat-box"><div style="font-size:1.8rem;">💳</div><div class="stat-lbl">Fee Portal</div></div>""", unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("#### ❓ Frequently Asked Questions")
    with st.expander("What is the mandatory attendance requirement?"):
        st.write("A minimum of 75% attendance in theory and practical courses is strictly required to appear for end-semester examinations.")
    with st.expander("How do I request official transcripts?"):
        st.write("Apply through the Student ERP portal under 'Certificates' or visit the Office of the Controller of Examinations. Processing time is 3-5 working days.")
    with st.expander("Can I pursue an engineering minor in another branch?"):
        st.write("Yes! Students maintaining a CGPA of 7.5 or above can enroll for minor specializations in AI, Cybersecurity, or Robotics starting semester 3.")

    st.markdown("---")
    st.markdown("#### 📝 Student Grievance & Suggestion Redressal Cell")
    with st.form("grievance_form"):
        g_name = st.text_input("Student Full Name *")
        g_roll = st.text_input("Roll / Registration Number *")
        g_email = st.text_input("College Email *")
        g_cat = st.selectbox("Category", ["Academic / Exam", "Hostel & Dining", "Lab Infrastructure", "General Suggestion"])
        g_desc = st.text_area("Detailed Grievance / Feedback *")
        if st.form_submit_button("Submit Request"):
            if g_name and g_roll and g_desc:
                st.success("✅ Your redressal request has been registered with the Office of the Dean of Student Affairs.")
            else:
                st.error("Please fill in all mandatory fields.")

# ==============================================================================
# 10. CONTACT US
# ==============================================================================
elif menu == "📞 Contact Us":
    st.markdown("### Contact CampusConnect")
    
    col_c1, col_c2 = st.columns(2)
    with col_c1:
        st.markdown("""
        <div class="portal-card">
            <h4>📍 Campus Address</h4>
            <p><strong>CampusConnect Institute of Technology</strong><br>
            Knowledge City, Innovation Boulevard<br>
            Electronic City, Bengaluru, Karnataka - 560100</p>
            <p>📞 <strong>Helpline:</strong> +91 80 2345 6789<br>
            📧 <strong>Email:</strong> info@campusconnect.edu<br>
            🕒 <strong>Hours:</strong> Mon - Sat: 8:30 AM - 5:30 PM</p>
        </div>
        """, unsafe_allow_html=True)
    with col_c2:
        st.markdown("##### Send an Inquiry Message")
        with st.form("contact_msg_form"):
            c_name = st.text_input("Your Name *")
            c_email = st.text_input("Your Email *")
            c_msg = st.text_area("Your Message *")
            if st.form_submit_button("Dispatch Message"):
                if c_name and c_email and c_msg:
                    st.success("✅ Thank you! Our administrative staff will reply to your message shortly.")

# ==============================================================================
# 11. ADMIN PORTAL
# ==============================================================================
elif menu == "🔐 Admin Portal":
    st.markdown("### Administration Control Panel")
    
    if "is_admin" not in st.session_state:
        st.session_state.is_admin = False
        
    if not st.session_state.is_admin:
        st.markdown("Please sign in with administrator credentials.")
        with st.form("admin_login_form"):
            u = st.text_input("Username", value="admin")
            p = st.text_input("Password", type="password", value="admin123")
            btn = st.form_submit_button("Sign In")
            if btn:
                if u == "admin" and p == "admin123":
                    st.session_state.is_admin = True
                    st.rerun()
                else:
                    st.error("Invalid credentials.")
    else:
        st.success("Authenticated as Administrator (Superadmin)")
        if st.button("Sign Out"):
            st.session_state.is_admin = False
            st.rerun()
            
        st.markdown("---")
        
        # Telemetry
        app_cnt = conn.execute("SELECT COUNT(*) FROM admission_applications").fetchone()[0]
        enq_cnt = conn.execute("SELECT COUNT(*) FROM admission_enquiries").fetchone()[0]
        ann_cnt = conn.execute("SELECT COUNT(*) FROM announcements").fetchone()[0]
        evt_cnt = conn.execute("SELECT COUNT(*) FROM events").fetchone()[0]
        
        m1, m2, m3, m4 = st.columns(4)
        m1.metric("Admission Applications", app_cnt)
        m2.metric("Enquiries / Leads", enq_cnt)
        m3.metric("Announcements", ann_cnt)
        m4.metric("Events", evt_cnt)
        
        st.markdown("---")
        
        adm_tab1, adm_tab2, adm_tab3 = st.tabs(["📄 Admission Applications", "📢 Post Announcement", "💬 Inquiries"])
        
        with adm_tab1:
            st.markdown("##### Recent Admission Applications")
            apps = conn.execute("SELECT * FROM admission_applications ORDER BY created_at DESC").fetchall()
            if apps:
                for a in apps:
                    with st.expander(f"{a['application_no']} — {a['full_name']} ({a['status']})"):
                        st.markdown(f"**Department Choice:** {a['department_choice']}")
                        st.markdown(f"**Marks:** 10th: {a['tenth_percentage']}% | 12th: {a['twelfth_percentage']}%")
                        st.markdown(f"**Contact:** 📧 {a['email']} | 📞 {a['phone']}")
                        st.markdown(f"**Address:** {a['address']}")
                        
                        # Change status
                        new_stat = st.selectbox("Update Status", ["Submitted", "Under Review", "Approved", "Rejected"], index=["Submitted", "Under Review", "Approved", "Rejected"].index(a['status']) if a['status'] in ["Submitted", "Under Review", "Approved", "Rejected"] else 0, key=f"stat_{a['id']}")
                        if st.button("Save Status", key=f"btn_stat_{a['id']}"):
                            conn.execute("UPDATE admission_applications SET status=? WHERE id=?", (new_stat, a['id']))
                            conn.commit()
                            st.success(f"Status updated to {new_stat}")
                            st.rerun()
            else:
                st.info("No applications submitted yet.")

        with adm_tab2:
            st.markdown("##### Post New Official Notice")
            with st.form("new_notice_form"):
                n_title = st.text_input("Notice Title *")
                n_cat = st.selectbox("Category", ["General", "Examination", "Academic", "Holiday", "Workshop", "Circular"])
                n_sum = st.text_input("Short Summary *")
                n_desc = st.text_area("Detailed Content *")
                n_imp = st.checkbox("Mark as Urgent")
                
                if st.form_submit_button("Publish Announcement"):
                    if n_title and n_sum and n_desc:
                        conn.execute("""
                            INSERT INTO announcements (title, category, summary, content, is_important, is_active, publish_date, created_at)
                            VALUES (?, ?, ?, ?, ?, 1, ?, ?)
                        """, (n_title, n_cat, n_sum, n_desc, 1 if n_imp else 0, str(date.today()), datetime.utcnow()))
                        conn.commit()
                        st.success("🎉 Announcement Published Successfully!")
                        st.rerun()
                    else:
                        st.error("Please fill in all mandatory fields.")

        with adm_tab3:
            st.markdown("##### Inquiries & Leads")
            enqs = conn.execute("SELECT * FROM admission_enquiries ORDER BY created_at DESC").fetchall()
            for eq in enqs:
                st.markdown(f"- **{eq['student_name']}** ({eq['course_interested']}) — 📧 `{eq['email']}` | 📞 `{eq['phone']}`\n  *Query:* {eq['message']}")

conn.close()
