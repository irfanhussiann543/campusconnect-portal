from datetime import date, datetime, timedelta
from backend.database import db
from backend.models import (
    AdminUser, Department, Faculty, Announcement, Event,
    PlacementRecord, Recruiter, StudentTestimonial, Document
)

def seed_database():
    """Populates the database with rich, realistic university data if empty."""
    # Check if already seeded
    if AdminUser.query.first():
        return

    print("Seeding CampusConnect database with initial university data...")

    # 1. Default Admin User
    admin = AdminUser(
        username="admin",
        email="admin@campusconnect.edu",
        full_name="Dr. Arthur Vance (Chief Academic Administrator)",
        role="superadmin"
    )
    admin.set_password("admin123")
    db.session.add(admin)

    # 2. Departments
    dept_cse = Department(
        code="CSE",
        name="Computer Science and Engineering",
        short_intro="Pioneering education and research in distributed computing, cyber systems, and modern software architecture.",
        description="The Department of Computer Science and Engineering at CampusConnect offers world-class education bridging theoretical foundations with real-world industry applications. Equipped with state-of-the-art supercomputing labs, cloud infrastructure, and collaborative centers of excellence with tech giants, our curriculum is aligned with ACM/IEEE standards and Industry 4.0 requirements.",
        hod_name="Dr. Raghavan Sundaram",
        hod_email="hod.cse@campusconnect.edu",
        hod_qualification="Ph.D. in Computer Science (IIT Madras), PostDoc (NUS)",
        intake=180,
        established_year=2002,
        labs_count=12,
        icon="fa-laptop-code",
        featured=True
    )

    dept_aids = Department(
        code="AIDS",
        name="Artificial Intelligence and Data Science",
        short_intro="Empowering the next generation of AI researchers, machine learning architects, and big data specialists.",
        description="The Department of Artificial Intelligence & Data Science is dedicated to producing visionary engineers capable of conceptualizing, deploying, and ethical stewardship of intelligent systems. Featuring NVIDIA GPU compute clusters, high-throughput data pipelines, and research labs focused on Natural Language Processing, Computer Vision, and Autonomous Robotics.",
        hod_name="Dr. Ananya Sharma",
        hod_email="hod.aids@campusconnect.edu",
        hod_qualification="Ph.D. in Machine Learning (IISc Bangalore)",
        intake=120,
        established_year=2020,
        labs_count=8,
        icon="fa-brain",
        featured=True
    )

    dept_ece = Department(
        code="ECE",
        name="Electronics and Communication Engineering",
        short_intro="Driving breakthroughs in VLSI design, wireless 5G/6G communication, embedded systems, and photonics.",
        description="The Department of Electronics and Communication Engineering provides comprehensive exposure to microelectronics, semiconductor devices, signal processing, and antenna design. The department hosts an advanced Cadence VLSI EDA Laboratory, Keysight RF & Microwave Test Suite, and an IoT Innovation Hub.",
        hod_name="Dr. Venkatraman Iyer",
        hod_email="hod.ece@campusconnect.edu",
        hod_qualification="Ph.D. in Microelectronics (IIT Bombay)",
        intake=180,
        established_year=2002,
        labs_count=10,
        icon="fa-microchip",
        featured=True
    )

    dept_mech = Department(
        code="MECH",
        name="Mechanical Engineering",
        short_intro="Leading innovation in electric mobility, advanced robotics, additive manufacturing, and thermal energy systems.",
        description="Mechanical Engineering at CampusConnect blends classical mechanics with cutting-edge digital twin technologies, computational fluid dynamics (CFD), and mechatronics. Students design formula student cars, conduct aerospace simulations, and work in advanced CNC and 3D printing fabrication centers.",
        hod_name="Dr. Rajeshwari Menon",
        hod_email="hod.mech@campusconnect.edu",
        hod_qualification="Ph.D. in Thermal Science (IIT Delhi)",
        intake=120,
        established_year=2003,
        labs_count=9,
        icon="fa-cogs",
        featured=True
    )

    dept_civil = Department(
        code="CIVIL",
        name="Civil Engineering",
        short_intro="Shaping sustainable smart cities, earthquake-resistant infrastructures, and green environmental engineering.",
        description="The Department of Civil Engineering prepares engineers to tackle climate change, urban transportation crises, and sustainable infrastructure design. Facilities include high-capacity structural testing frames, total station geospatial survey laboratories, GIS analysis centers, and environmental testing units.",
        hod_name="Dr. K. S. Mukherjee",
        hod_email="hod.civil@campusconnect.edu",
        hod_qualification="Ph.D. in Structural Engineering (IIT Kharagpur)",
        intake=60,
        established_year=2005,
        labs_count=7,
        icon="fa-city",
        featured=True
    )

    dept_eee = Department(
        code="EEE",
        name="Electrical and Electronics Engineering",
        short_intro="Spearheading renewable grid integration, electric vehicle drives, high-voltage systems, and smart automation.",
        description="The Department of Electrical and Electronics Engineering delivers deep technical competencies across power systems, smart grids, renewable energy, and power electronic converters. The department maintains specialized testbeds for solar microgrids, motor drives, and industrial SCADA automation.",
        hod_name="Dr. Meera Nambiar",
        hod_email="hod.eee@campusconnect.edu",
        hod_qualification="Ph.D. in Renewable Power Systems (NIT Trichy)",
        intake=120,
        established_year=2004,
        labs_count=8,
        icon="fa-bolt",
        featured=True
    )

    db.session.add_all([dept_cse, dept_aids, dept_ece, dept_mech, dept_civil, dept_eee])
    db.session.flush()

    # 3. Faculty Members
    faculties = [
        # CSE
        Faculty(
            department_id=dept_cse.id,
            name="Dr. Raghavan Sundaram",
            designation="Professor & Head of Department",
            qualification="Ph.D. (IIT Madras), M.Tech (NITK)",
            specialization="Distributed Cloud Systems, Blockchain Architecture & Edge Computing",
            email="raghavan.s@campusconnect.edu",
            phone="+91 98765 43210",
            experience_years=21,
            photo_url="https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=400&q=80",
            bio="Author of 4 books and over 50 international journal publications in cloud architectures. Recipient of Best Faculty Researcher Award 2024.",
            research_areas="Cloud Virtualization, Zero-Knowledge Proofs, High Performance Computing"
        ),
        Faculty(
            department_id=dept_cse.id,
            name="Prof. Divya Krishnan",
            designation="Associate Professor",
            qualification="M.Tech (IISc Bangalore), Ph.D. (Pursuing - IITB)",
            specialization="Cybersecurity, Cryptography & Secure Software Engineering",
            email="divya.k@campusconnect.edu",
            phone="+91 98765 43211",
            experience_years=12,
            photo_url="https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?auto=format&fit=crop&w=400&q=80",
            bio="Leads the CampusConnect Cyber Defense Center. Certified Ethical Hacker (CEH) with extensive industry consulting background.",
            research_areas="Penetration Testing, Post-Quantum Cryptography, Secure SDLC"
        ),
        Faculty(
            department_id=dept_cse.id,
            name="Dr. Arjun Nair",
            designation="Assistant Professor",
            qualification="Ph.D. in Computer Science (BITS Pilani)",
            specialization="Full-Stack Web Architectures, Database Systems & DevOps",
            email="arjun.nair@campusconnect.edu",
            phone="+91 98765 43212",
            experience_years=8,
            photo_url="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&w=400&q=80",
            bio="Passionate educator and mentor for Google Solution Challenge and ACM ICPC finalists.",
            research_areas="Distributed Databases, Microservices, Observability"
        ),

        # AI & DS
        Faculty(
            department_id=dept_aids.id,
            name="Dr. Ananya Sharma",
            designation="Professor & Head of Department",
            qualification="Ph.D. (IISc Bangalore), M.Tech (IIT Roorkee)",
            specialization="Deep Learning, Large Language Models & Generative AI",
            email="ananya.sharma@campusconnect.edu",
            phone="+91 98765 43213",
            experience_years=16,
            photo_url="https://images.unsplash.com/photo-1580489944761-15a19d654956?auto=format&fit=crop&w=400&q=80",
            bio="Keynote speaker at NeurIPS workshops, principal investigator for multi-crore DST-sponsored AI healthcare initiative.",
            research_areas="Medical Image Segmentation, Transformer Models, Responsible AI"
        ),
        Faculty(
            department_id=dept_aids.id,
            name="Dr. Siddharth Verma",
            designation="Associate Professor",
            qualification="Ph.D. in Data Science (IIT Hyderabad)",
            specialization="Reinforcement Learning, Computer Vision & Autonomous Systems",
            email="siddharth.v@campusconnect.edu",
            phone="+91 98765 43214",
            experience_years=11,
            photo_url="https://images.unsplash.com/photo-1500648767791-00dcc994a43e?auto=format&fit=crop&w=400&q=80",
            bio="Directs the Autonomous Driving Systems Lab at CampusConnect. Former Senior Research Scientist at Mercedes-Benz R&D.",
            research_areas="Object Detection, SLAM Algorithms, Multi-Agent RL"
        ),

        # ECE
        Faculty(
            department_id=dept_ece.id,
            name="Dr. Venkatraman Iyer",
            designation="Professor & Head of Department",
            qualification="Ph.D. (IIT Bombay), M.E. (Anna University)",
            specialization="VLSI System Design, Low-Power Embedded Architectures & FPGA",
            email="venkat.iyer@campusconnect.edu",
            phone="+91 98765 43215",
            experience_years=23,
            photo_url="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?auto=format&fit=crop&w=400&q=80",
            bio="Senior Member IEEE with 6 published patents in energy-harvesting semiconductor sensors.",
            research_areas="Cadence EDA, Nanoscale Transistors, ASIC Synthesis"
        ),
        Faculty(
            department_id=dept_ece.id,
            name="Dr. Preethi Mohan",
            designation="Associate Professor",
            qualification="Ph.D. (NIT Tiruchirappalli)",
            specialization="5G/6G Wireless Networks, Massive MIMO & Optical Fiber Comms",
            email="preethi.m@campusconnect.edu",
            phone="+91 98765 43216",
            experience_years=14,
            photo_url="https://images.unsplash.com/photo-1544005313-94ddf0286df2?auto=format&fit=crop&w=400&q=80",
            bio="Published extensively in IEEE Transactions on Wireless Communications. Advisor to telecom startups.",
            research_areas="Beamforming, Millimeter Wave Communications, Network Slicing"
        ),

        # MECH
        Faculty(
            department_id=dept_mech.id,
            name="Dr. Rajeshwari Menon",
            designation="Professor & Head of Department",
            qualification="Ph.D. (IIT Delhi), M.Tech (IIT Madras)",
            specialization="Thermal & Fluid Dynamics, Renewable Hydrogen Energy Systems",
            email="rajeshwari.m@campusconnect.edu",
            phone="+91 98765 43217",
            experience_years=20,
            photo_url="https://images.unsplash.com/photo-1567532939604-b6b5b0db2604?auto=format&fit=crop&w=400&q=80",
            bio="Consultant to ISRO and automotive OEMs. Fellow of the Institution of Engineers (India).",
            research_areas="Computational Fluid Dynamics (ANSYS), Green Hydrogen Storage"
        ),

        # CIVIL
        Faculty(
            department_id=dept_civil.id,
            name="Dr. K. S. Mukherjee",
            designation="Professor & Head of Department",
            qualification="Ph.D. (IIT Kharagpur)",
            specialization="Earthquake Resistant Structures, Smart Geotechnical Engineering",
            email="ks.mukherjee@campusconnect.edu",
            phone="+91 98765 43218",
            experience_years=25,
            photo_url="https://images.unsplash.com/photo-1519085360753-af0119f7cbe7?auto=format&fit=crop&w=400&q=80",
            bio="Structural consultant for metro rail tunnels and high-rise commercial structures.",
            research_areas="Base Isolation Systems, Geosynthetics, Structural Health Monitoring"
        ),

        # EEE
        Faculty(
            department_id=dept_eee.id,
            name="Dr. Meera Nambiar",
            designation="Professor & Head of Department",
            qualification="Ph.D. (NIT Trichy), M.Tech (IISc)",
            specialization="Smart Grid Infrastructure, Electric Vehicle Powertrains & Power Electronics",
            email="meera.n@campusconnect.edu",
            phone="+91 98765 43219",
            experience_years=18,
            photo_url="https://images.unsplash.com/photo-1598550874175-4d0ef436c909?auto=format&fit=crop&w=400&q=80",
            bio="Lead Investigator for the University's 250 kW Rooftop Solar Microgrid Smart Project.",
            research_areas="Wide Bandgap Semiconductors, Battery Management Systems (BMS)"
        )
    ]
    db.session.add_all(faculties)

    # 4. Announcements
    today = date.today()
    announcements = [
        Announcement(
            title="End-Semester Examination Schedule Announced for Even Semester 2026",
            category="Examination",
            summary="The Office of the Controller of Examinations has published the final timetable for B.Tech & M.Tech degree examinations starting Dec 1, 2026.",
            content="All regular and arrear students across all engineering branches are requested to download their official examination timetables and hall tickets from the student portal. Practical examinations will commence on Nov 20, 2026.",
            attachment_url="/static/uploads/Exam_Schedule_2026.pdf",
            is_important=True,
            is_active=True,
            publish_date=today - timedelta(days=1)
        ),
        Announcement(
            title="Campus Placement Drive by Google & Microsoft — Registration Deadline",
            category="Circular",
            summary="Final year and pre-final year students eligible for the upcoming joint Tech Giants Placement Drive must submit resumes by Friday 5:00 PM.",
            content="Eligibility: Minimum 7.5 CGPA with no active backlogs. Branches eligible: CSE, AI&DS, ECE, EEE. Shortlisted students will participate in the online coding assessment next Monday.",
            attachment_url="",
            is_important=True,
            is_active=True,
            publish_date=today - timedelta(days=3)
        ),
        Announcement(
            title="National Hackathon 'CodeStorm 2026' Cash Prizes Worth ₹5 Lakhs Announced",
            category="Workshop",
            summary="CampusConnect Innovation Cell cordially invites student teams across India to submit software & hardware prototypes.",
            content="Themes include AI for Healthcare, Smart Clean Energy, FinTech, and Disaster Mitigation. Winning teams will receive immediate incubation support and pre-placement interview waivers.",
            attachment_url="",
            is_important=False,
            is_active=True,
            publish_date=today - timedelta(days=5)
        ),
        Announcement(
            title="Diwali & Mid-Term Recess Notification for Academic Year 2026-27",
            category="Holiday",
            summary="College campus, instructional laboratories, and academic departments will observe the scheduled mid-term vacation.",
            content="Hostel messes and digital library access will remain operational 24/7. Classes will resume according to the master academic timetable on Monday.",
            attachment_url="",
            is_important=False,
            is_active=True,
            publish_date=today - timedelta(days=7)
        ),
        Announcement(
            title="Admissions Open for Undergraduate B.Tech Programs 2026-2027",
            category="Academic",
            summary="Online applications are invited from eligible candidates for merit-based and sports quota engineering seats.",
            content="Candidates can submit applications online or visit the campus Admissions Advisory Desk. Early admission applicants are eligible for Chancellor's Merit Scholarship up to 50% tuition waiver.",
            attachment_url="",
            is_important=True,
            is_active=True,
            publish_date=today - timedelta(days=10)
        )
    ]
    db.session.add_all(announcements)

    # 5. Events
    events = [
        Event(
            title="CodeStorm 2026: 36-Hour National Hackathon",
            category="Hackathon",
            description="Our flagship national level hackathon brings together 500+ top student hackers, industry mentors from Google, AWS, and Microsoft, and venture capitalists. Grand cash prize pool of ₹5,00,000 plus cloud computing credits.",
            event_date=today + timedelta(days=12),
            event_time="09:00 AM - 09:00 PM (36 Hours)",
            venue="Dr. APJ Abdul Kalam Convention Center, Tech Park",
            organizer="CampusConnect Department of CSE & ACM Student Chapter",
            image_url="https://images.unsplash.com/photo-1504384308090-c894fdcc538d?auto=format&fit=crop&w=800&q=80",
            max_seats=200,
            is_featured=True
        ),
        Event(
            title="International Summit on Generative AI & Robotics",
            category="Seminar",
            description="A two-day premier research symposium featuring keynote addresses by distinguished scientists from Stanford, IISc, NVIDIA, and OpenAI, discussing multimodal foundation models and human-robot teaming.",
            event_date=today + timedelta(days=20),
            event_time="10:00 AM - 05:00 PM",
            venue="Sir C.V. Raman Auditorium, Main Block",
            organizer="Department of AI & Data Science",
            image_url="https://images.unsplash.com/photo-1485827404703-89b55fcc595e?auto=format&fit=crop&w=800&q=80",
            max_seats=350,
            is_featured=True
        ),
        Event(
            title="Hands-on Workshop: VLSI Chip Design & Cadence Virtuoso",
            category="Workshop",
            description="Intensive practical workshop focusing on 7nm FinFET standard cell design, DRC/LVS physical verification, and static timing analysis using Cadence tools suite.",
            event_date=today + timedelta(days=15),
            event_time="09:30 AM - 04:30 PM",
            venue="Cadence Advanced VLSI Lab (Lab Block 3)",
            organizer="Department of ECE & IEEE Electron Devices Society",
            image_url="https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=800&q=80",
            max_seats=60,
            is_featured=False
        ),
        Event(
            title="AURA 2026: Annual Inter-Collegiate Cultural Festival",
            category="Cultural",
            description="Three days of music, dance, theater, celebrity DJ nights, battle of the bands, fashion pageants, and food carnivals featuring 40+ colleges nationwide.",
            event_date=today + timedelta(days=35),
            event_time="04:00 PM - 10:30 PM",
            venue="University Open Air Amphitheater",
            organizer="CampusConnect Student Cultural Council",
            image_url="https://images.unsplash.com/photo-1514525253161-7a46d19cd819?auto=format&fit=crop&w=800&q=80",
            max_seats=5000,
            is_featured=True
        ),
        Event(
            title="All-India Inter-University Athletics & Sports Meet",
            category="Sports",
            description="Track and field events, basketball tournaments, football championship, cricket league, and badminton matches hosted on our Olympic standard turf.",
            event_date=today + timedelta(days=28),
            event_time="07:00 AM - 06:00 PM",
            venue="CampusConnect Multi-Purpose Sports Complex",
            organizer="Department of Physical Education",
            image_url="https://images.unsplash.com/photo-1461896836934-ffe607ba8211?auto=format&fit=crop&w=800&q=80",
            max_seats=800,
            is_featured=False
        )
    ]
    db.session.add_all(events)

    # 6. Placement Records
    placements = [
        PlacementRecord(
            academic_year="2025-2026",
            total_offers=1284,
            placed_percentage=98.4,
            highest_package_lpa=54.5,
            avg_package_lpa=8.4,
            companies_visited=210,
            is_current=True
        ),
        PlacementRecord(
            academic_year="2024-2025",
            total_offers=1190,
            placed_percentage=97.2,
            highest_package_lpa=48.0,
            avg_package_lpa=7.9,
            companies_visited=195,
            is_current=False
        ),
        PlacementRecord(
            academic_year="2023-2024",
            total_offers=1105,
            placed_percentage=96.5,
            highest_package_lpa=44.0,
            avg_package_lpa=7.4,
            companies_visited=180,
            is_current=False
        )
    ]
    db.session.add_all(placements)

    # 7. Recruiters
    recruiters = [
        Recruiter(
            company_name="Google",
            tier="Super Dream",
            logo_url="https://upload.wikimedia.org/wikipedia/commons/2/2f/Google_2015_logo.svg",
            roles_offered="Software Development Engineer, Cloud Associate",
            highest_pkg_offered=54.5,
            featured=True
        ),
        Recruiter(
            company_name="Microsoft",
            tier="Super Dream",
            logo_url="https://upload.wikimedia.org/wikipedia/commons/9/96/Microsoft_logo_%282012%29.svg",
            roles_offered="Software Engineer, Data & Applied Scientist",
            highest_pkg_offered=51.0,
            featured=True
        ),
        Recruiter(
            company_name="Amazon",
            tier="Super Dream",
            logo_url="https://upload.wikimedia.org/wikipedia/commons/a/a9/Amazon_logo.svg",
            roles_offered="SDE-1, Solutions Architect, Support Engineer",
            highest_pkg_offered=45.0,
            featured=True
        ),
        Recruiter(
            company_name="Cisco",
            tier="Dream",
            logo_url="https://upload.wikimedia.org/wikipedia/commons/0/08/Cisco_logo_blue_2016.svg",
            roles_offered="Network Engineer, Security Analyst",
            highest_pkg_offered=24.0,
            featured=True
        ),
        Recruiter(
            company_name="Goldman Sachs",
            tier="Super Dream",
            logo_url="https://upload.wikimedia.org/wikipedia/commons/6/61/Goldman_Sachs.svg",
            roles_offered="Quantitative Analyst, Software Engineer",
            highest_pkg_offered=38.0,
            featured=True
        ),
        Recruiter(
            company_name="Tata Consultancy Services",
            tier="Mass & Digital",
            logo_url="https://upload.wikimedia.org/wikipedia/commons/b/b1/Tata_Consultancy_Services_Logo.svg",
            roles_offered="TCS Digital, TCS Prime, Systems Engineer",
            highest_pkg_offered=11.5,
            featured=True
        ),
        Recruiter(
            company_name="Infosys",
            tier="Specialist",
            logo_url="https://upload.wikimedia.org/wikipedia/commons/9/95/Infosys_logo.svg",
            roles_offered="Power Programmer, Digital Specialist Engineer",
            highest_pkg_offered=9.5,
            featured=True
        ),
        Recruiter(
            company_name="Oracle",
            tier="Dream",
            logo_url="https://upload.wikimedia.org/wikipedia/commons/5/50/Oracle_logo.svg",
            roles_offered="Server Technology Engineer, Cloud Infrastructure",
            highest_pkg_offered=22.0,
            featured=True
        )
    ]
    db.session.add_all(recruiters)

    # 8. Student Testimonials
    testimonials = [
        StudentTestimonial(
            student_name="Rohit Shenoy",
            department="Computer Science & Engineering",
            graduation_year="Batch of 2025",
            placed_company="Google",
            package_lpa=54.5,
            quote="CampusConnect provided me with the ultimate launchpad. The faculty's mentorship in distributed algorithms and the round-the-clock labs gave me the confidence to ace technical interviews at Google.",
            photo_url="https://images.unsplash.com/photo-1539571696357-5a69c17a67c6?auto=format&fit=crop&w=300&q=80"
        ),
        StudentTestimonial(
            student_name="Sneha Pattanaik",
            department="Artificial Intelligence & Data Science",
            graduation_year="Batch of 2025",
            placed_company="Microsoft",
            package_lpa=51.0,
            quote="The high-end NVIDIA GPU compute facilities at the AI Department enabled me to train cutting-edge transformer models during my capstone project. CampusConnect's placement cell made my dream offer possible!",
            photo_url="https://images.unsplash.com/photo-1517841905240-472988babdf9?auto=format&fit=crop&w=300&q=80"
        ),
        StudentTestimonial(
            student_name="Aditya Kulkarni",
            department="Electronics & Communication Engineering",
            graduation_year="Batch of 2024",
            placed_company="Qualcomm",
            package_lpa=28.0,
            quote="The hands-on exposure to Cadence EDA tools and FPGA prototyping in our ECE department is on par with leading research institutes. I transitioned seamlessly from classroom to core semiconductor design.",
            photo_url="https://images.unsplash.com/photo-1522075469751-3a6694fb2f61?auto=format&fit=crop&w=300&q=80"
        )
    ]
    db.session.add_all(testimonials)

    # 9. Downloadable Documents
    documents = [
        Document(
            title="B.Tech Computer Science & Engineering - Regulation 2025 Curriculum & Syllabus",
            category="Syllabus",
            file_path="/static/uploads/CSE_Curriculum_2025.pdf",
            file_size="3.2 MB",
            file_type="PDF",
            department_code="CSE",
            semester="All Semesters",
            upload_date=today - timedelta(days=20)
        ),
        Document(
            title="Official Academic Calendar 2026-2027 (Odd & Even Semesters)",
            category="Academic Calendar",
            file_path="/static/uploads/Academic_Calendar_2026_27.pdf",
            file_size="1.1 MB",
            file_type="PDF",
            department_code="ALL",
            semester="2026-2027",
            upload_date=today - timedelta(days=15)
        ),
        Document(
            title="Autonomous Institution Examination Rules, Grading & Evaluation Guidelines",
            category="Regulations",
            file_path="/static/uploads/Exam_Regulations_Handout.pdf",
            file_size="2.4 MB",
            file_type="PDF",
            department_code="ALL",
            semester="General",
            upload_date=today - timedelta(days=30)
        ),
        Document(
            title="Data Structures & Algorithms in Python / C++ — Handcrafted Lecture Notes",
            category="Study Material",
            file_path="/static/uploads/DSA_Notes_Complete.pdf",
            file_size="6.8 MB",
            file_type="PDF",
            department_code="CSE",
            semester="Sem 3",
            upload_date=today - timedelta(days=10)
        ),
        Document(
            title="Campus Student Code of Conduct & Anti-Ragging Policy Handbook",
            category="Regulations",
            file_path="/static/uploads/Student_Handbook_2026.pdf",
            file_size="1.8 MB",
            file_type="PDF",
            department_code="ALL",
            semester="General",
            upload_date=today - timedelta(days=45)
        )
    ]
    db.session.add_all(documents)

    db.session.commit()
    print("Database seeding completed successfully!")
