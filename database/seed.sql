-- CampusConnect Initial Seed Data for MySQL
USE campusconnect;

-- Default Admin: admin / admin123 (werkzeug pbkdf2 hash)
INSERT INTO admin_users (username, email, password_hash, full_name, role)
VALUES ('admin', 'admin@campusconnect.edu', 'scrypt:32768:8:1$dOq8aHwT7F0J3X2q$1c9fdbb790d19e917d8e6a10065b21919a716768393521d9fa49ebfe21b6d92ec2b5f63d04e5781a8684ad419736c2e352f5ad45a86a02dfc059e69335ef07eb', 'Dr. Arthur Vance (Chief Academic Administrator)', 'superadmin')
ON DUPLICATE KEY UPDATE id=id;

-- Insert Departments
INSERT INTO departments (code, name, short_intro, description, hod_name, hod_email, hod_qualification, intake, established_year, labs_count, icon, featured)
VALUES 
('CSE', 'Computer Science and Engineering', 'Pioneering education and research in distributed computing, cyber systems, and modern software architecture.', 'World-class education bridging theoretical foundations with real-world industry applications with high-throughput labs.', 'Dr. Raghavan Sundaram', 'hod.cse@campusconnect.edu', 'Ph.D. in Computer Science (IIT Madras)', 180, 2002, 12, 'fa-laptop-code', 1),
('AIDS', 'Artificial Intelligence and Data Science', 'Empowering the next generation of AI researchers, machine learning architects, and big data specialists.', 'Dedicated to producing visionary engineers with NVIDIA GPU clusters and intelligent autonomous systems.', 'Dr. Ananya Sharma', 'hod.aids@campusconnect.edu', 'Ph.D. in Machine Learning (IISc Bangalore)', 120, 2020, 8, 'fa-brain', 1),
('ECE', 'Electronics and Communication Engineering', 'Driving breakthroughs in VLSI design, wireless 5G/6G communication, embedded systems, and photonics.', 'Features Cadence VLSI EDA Laboratory, Keysight RF & Microwave Test Suite, and an IoT Innovation Hub.', 'Dr. Venkatraman Iyer', 'hod.ece@campusconnect.edu', 'Ph.D. in Microelectronics (IIT Bombay)', 180, 2002, 10, 'fa-microchip', 1),
('MECH', 'Mechanical Engineering', 'Leading innovation in electric mobility, advanced robotics, additive manufacturing, and thermal energy systems.', 'Blends classical mechanics with cutting-edge digital twin technologies, CFD, and mechatronics.', 'Dr. Rajeshwari Menon', 'hod.mech@campusconnect.edu', 'Ph.D. in Thermal Science (IIT Delhi)', 120, 2003, 9, 'fa-cogs', 1),
('CIVIL', 'Civil Engineering', 'Shaping sustainable smart cities, earthquake-resistant infrastructures, and green environmental engineering.', 'Prepares engineers to tackle climate change, urban transportation crises, and sustainable infrastructure design.', 'Dr. K. S. Mukherjee', 'hod.civil@campusconnect.edu', 'Ph.D. in Structural Engineering (IIT Kharagpur)', 60, 2005, 7, 'fa-city', 1),
('EEE', 'Electrical and Electronics Engineering', 'Spearheading renewable grid integration, electric vehicle drives, high-voltage systems, and smart automation.', 'Delivers deep technical competencies across power systems, smart grids, renewable energy, and power electronic converters.', 'Dr. Meera Nambiar', 'hod.eee@campusconnect.edu', 'Ph.D. in Renewable Power Systems (NIT Trichy)', 120, 2004, 8, 'fa-bolt', 1)
ON DUPLICATE KEY UPDATE code=code;

-- Insert Placement Summary
INSERT INTO placement_records (academic_year, total_offers, placed_percentage, highest_package_lpa, avg_package_lpa, companies_visited, is_current)
VALUES 
('2025-2026', 1284, 98.40, 54.50, 8.40, 210, 1),
('2024-2025', 1190, 97.20, 48.00, 7.90, 195, 0),
('2023-2024', 1105, 96.50, 44.00, 7.40, 180, 0)
ON DUPLICATE KEY UPDATE academic_year=academic_year;
