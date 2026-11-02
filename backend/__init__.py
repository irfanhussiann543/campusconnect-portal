import os
from flask import Flask
from backend.config import Config, BASE_DIR
from backend.database import configure_database, db
from backend.seed_data import seed_database

def create_app(config_class=Config):
    app = Flask(
        __name__,
        template_folder=os.path.join(BASE_DIR, "templates"),
        static_folder=os.path.join(BASE_DIR, "static")
    )
    app.config.from_object(config_class)

    # Ensure uploads directory exists
    os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

    # Configure Database with MySQL or SQLite fallback
    configure_database(app)

    # Register Blueprints
    from backend.routes_public import public_bp
    from backend.routes_admin import admin_bp
    from backend.auth import auth_bp

    app.register_blueprint(public_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(auth_bp)

    # Initialize tables and seed data
    with app.app_context():
        db.create_all()
        seed_database()

    return app
