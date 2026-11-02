import os
from dotenv import load_dotenv

# Load environment variables if .env exists
load_dotenv()

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "campusconnect-secret-key-2026-production")
    
    # MySQL Database Settings
    MYSQL_HOST = os.environ.get("MYSQL_HOST", "localhost")
    MYSQL_PORT = int(os.environ.get("MYSQL_PORT", 3306))
    MYSQL_USER = os.environ.get("MYSQL_USER", "root")
    MYSQL_PASSWORD = os.environ.get("MYSQL_PASSWORD", "")
    MYSQL_DB = os.environ.get("MYSQL_DB", "campusconnect")

    # SQLAlchemy Config
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Upload folder
    UPLOAD_FOLDER = os.path.join(BASE_DIR, "static", "uploads")
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16 MB max upload
    ALLOWED_EXTENSIONS = {"pdf", "png", "jpg", "jpeg", "doc", "docx"}
    
    # Default SQLite fallback path
    SQLITE_PATH = os.path.join(BASE_DIR, "campusconnect.db")
    
    @classmethod
    def get_mysql_uri(cls):
        pwd = f":{cls.MYSQL_PASSWORD}" if cls.MYSQL_PASSWORD else ""
        return f"mysql+pymysql://{cls.MYSQL_USER}{pwd}@{cls.MYSQL_HOST}:{cls.MYSQL_PORT}/{cls.MYSQL_DB}?charset=utf8mb4"

    @classmethod
    def get_sqlite_uri(cls):
        return f"sqlite:///{cls.SQLITE_PATH}"
