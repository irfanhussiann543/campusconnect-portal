import logging
from flask_sqlalchemy import SQLAlchemy
from backend.config import Config

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("CampusConnectDB")

db = SQLAlchemy()

def configure_database(app):
    """
    Attempts to connect to MySQL using configured credentials.
    If MySQL server is unreachable or fails, falls back gracefully to local SQLite.
    """
    mysql_uri = Config.get_mysql_uri()
    use_sqlite = False
    
    # Try probing MySQL connection
    try:
        import pymysql
        conn = pymysql.connect(
            host=Config.MYSQL_HOST,
            user=Config.MYSQL_USER,
            password=Config.MYSQL_PASSWORD,
            port=Config.MYSQL_PORT,
            connect_timeout=2
        )
        # Check if database exists, otherwise create it
        with conn.cursor() as cursor:
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS `{Config.MYSQL_DB}` CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;")
        conn.close()
        
        app.config["SQLALCHEMY_DATABASE_URI"] = mysql_uri
        app.config["ACTIVE_DB_ENGINE"] = "MySQL"
        logger.info(f"Connected to MySQL Database at {Config.MYSQL_HOST}:{Config.MYSQL_PORT}/{Config.MYSQL_DB}")
    except Exception as e:
        logger.warning(f"MySQL unavailable ({e}). Gracefully falling back to SQLite database at {Config.SQLITE_PATH}.")
        app.config["SQLALCHEMY_DATABASE_URI"] = Config.get_sqlite_uri()
        app.config["ACTIVE_DB_ENGINE"] = "SQLite (MySQL-Ready)"

    db.init_app(app)
    return db
