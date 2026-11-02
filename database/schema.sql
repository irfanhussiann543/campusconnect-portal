-- CampusConnect College Information Portal
-- Complete MySQL Database Schema

CREATE DATABASE IF NOT EXISTS campusconnect CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE campusconnect;

-- 1. Admin Users Table
CREATE TABLE IF NOT EXISTS admin_users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(64) NOT NULL UNIQUE,
    email VARCHAR(120) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    full_name VARCHAR(120) NOT NULL,
    role VARCHAR(32) DEFAULT 'admin',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- 2. Departments Table
CREATE TABLE IF NOT EXISTS departments (
    id INT AUTO_INCREMENT PRIMARY KEY,
    code VARCHAR(16) NOT NULL UNIQUE,
    name VARCHAR(128) NOT NULL,
    short_intro TEXT NOT NULL,
    description LONGTEXT NOT NULL,
    hod_name VARCHAR(100) NOT NULL,
    hod_email VARCHAR(120) NOT NULL,
    hod_qualification VARCHAR(120) DEFAULT 'Ph.D.',
    intake INT DEFAULT 120,
    established_year INT DEFAULT 2005,
    labs_count INT DEFAULT 8,
    icon VARCHAR(64) DEFAULT 'fa-laptop-code',
    featured BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- 3. Faculty Table
CREATE TABLE IF NOT EXISTS faculty (
    id INT AUTO_INCREMENT PRIMARY KEY,
    department_id INT NOT NULL,
    name VARCHAR(120) NOT NULL,
    designation VARCHAR(100) NOT NULL,
    qualification VARCHAR(150) NOT NULL,
    specialization VARCHAR(255) NOT NULL,
    email VARCHAR(120) NOT NULL,
    phone VARCHAR(32),
    experience_years INT DEFAULT 5,
    photo_url VARCHAR(255) DEFAULT '/static/img/faculty/default.jpg',
    bio TEXT,
    research_areas TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (department_id) REFERENCES departments(id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- 4. Announcements Table
CREATE TABLE IF NOT EXISTS announcements (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    category VARCHAR(64) NOT NULL DEFAULT 'General',
    summary VARCHAR(500) NOT NULL,
    content LONGTEXT NOT NULL,
    attachment_url VARCHAR(255),
    is_important BOOLEAN DEFAULT FALSE,
    is_active BOOLEAN DEFAULT TRUE,
    publish_date DATE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- 5. Events Table
CREATE TABLE IF NOT EXISTS events (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    category VARCHAR(64) NOT NULL DEFAULT 'Workshop',
    description LONGTEXT NOT NULL,
    event_date DATE NOT NULL,
    event_time VARCHAR(64) NOT NULL,
    venue VARCHAR(150) NOT NULL,
    organizer VARCHAR(150) NOT NULL,
    image_url VARCHAR(255) DEFAULT '/static/img/campus/event-default.jpg',
    max_seats INT DEFAULT 150,
    is_featured BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- 6. Event Registrations Table
CREATE TABLE IF NOT EXISTS event_registrations (
    id INT AUTO_INCREMENT PRIMARY KEY,
    event_id INT NOT NULL,
    participant_name VARCHAR(120) NOT NULL,
    email VARCHAR(120) NOT NULL,
    phone VARCHAR(32) NOT NULL,
    college_or_dept VARCHAR(150) NOT NULL,
    registered_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (event_id) REFERENCES events(id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- 7. Placement Statistics Table
CREATE TABLE IF NOT EXISTS placement_records (
    id INT AUTO_INCREMENT PRIMARY KEY,
    academic_year VARCHAR(32) NOT NULL UNIQUE,
    total_offers INT NOT NULL,
    placed_percentage DECIMAL(5,2) NOT NULL,
    highest_package_lpa DECIMAL(5,2) NOT NULL,
    avg_package_lpa DECIMAL(5,2) NOT NULL,
    companies_visited INT NOT NULL,
    is_current BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- 8. Recruiting Companies Table
CREATE TABLE IF NOT EXISTS recruiters (
    id INT AUTO_INCREMENT PRIMARY KEY,
    company_name VARCHAR(120) NOT NULL,
    tier VARCHAR(32) DEFAULT 'Tier-1',
    logo_url VARCHAR(255) NOT NULL,
    roles_offered VARCHAR(255),
    highest_pkg_offered DECIMAL(5,2) DEFAULT 0.0,
    featured BOOLEAN DEFAULT TRUE
) ENGINE=InnoDB;

-- 9. Student Testimonials Table
CREATE TABLE IF NOT EXISTS student_testimonials (
    id INT AUTO_INCREMENT PRIMARY KEY,
    student_name VARCHAR(120) NOT NULL,
    department VARCHAR(100) NOT NULL,
    graduation_year VARCHAR(16) NOT NULL,
    placed_company VARCHAR(120) NOT NULL,
    package_lpa DECIMAL(5,2) NOT NULL,
    quote TEXT NOT NULL,
    photo_url VARCHAR(255) DEFAULT '/static/img/faculty/default.jpg'
) ENGINE=InnoDB;

-- 10. Admission Enquiries Table
CREATE TABLE IF NOT EXISTS admission_enquiries (
    id INT AUTO_INCREMENT PRIMARY KEY,
    student_name VARCHAR(120) NOT NULL,
    email VARCHAR(120) NOT NULL,
    phone VARCHAR(32) NOT NULL,
    course_interested VARCHAR(120) NOT NULL,
    message TEXT NOT NULL,
    status VARCHAR(32) DEFAULT 'New',
    admin_notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- 11. Admission Applications Table
CREATE TABLE IF NOT EXISTS admission_applications (
    id INT AUTO_INCREMENT PRIMARY KEY,
    application_no VARCHAR(32) NOT NULL UNIQUE,
    full_name VARCHAR(120) NOT NULL,
    email VARCHAR(120) NOT NULL,
    phone VARCHAR(32) NOT NULL,
    dob DATE NOT NULL,
    gender VARCHAR(16) NOT NULL,
    parent_name VARCHAR(120) NOT NULL,
    parent_phone VARCHAR(32) NOT NULL,
    department_choice VARCHAR(120) NOT NULL,
    tenth_percentage DECIMAL(5,2) NOT NULL,
    twelfth_percentage DECIMAL(5,2) NOT NULL,
    entrance_score VARCHAR(64),
    address TEXT NOT NULL,
    status VARCHAR(32) DEFAULT 'Submitted',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- 12. Documents Table (Academic Circulars, Syllabus, Handbooks)
CREATE TABLE IF NOT EXISTS documents (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    category VARCHAR(64) NOT NULL,
    file_path VARCHAR(255) NOT NULL,
    file_size VARCHAR(32) DEFAULT '1.5 MB',
    file_type VARCHAR(16) DEFAULT 'PDF',
    department_code VARCHAR(16),
    semester VARCHAR(16),
    upload_date DATE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- 13. Student Grievances & Feedback
CREATE TABLE IF NOT EXISTS grievances (
    id INT AUTO_INCREMENT PRIMARY KEY,
    student_name VARCHAR(120) NOT NULL,
    roll_number VARCHAR(32) NOT NULL,
    email VARCHAR(120) NOT NULL,
    category VARCHAR(64) NOT NULL,
    subject VARCHAR(255) NOT NULL,
    description LONGTEXT NOT NULL,
    status VARCHAR(32) DEFAULT 'Pending',
    admin_reply TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;
