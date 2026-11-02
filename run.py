import sys
import os

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from backend import create_app

app = create_app()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    print("=" * 65)
    print("  [CampusConnect] College Information Portal starting...")
    print(f"  * Public Portal URL:  http://127.0.0.1:{port}")
    print(f"  * Admin Portal URL:   http://127.0.0.1:{port}/admin/login")
    print("  * Admin Default:      Username: admin | Password: admin123")
    print(f"  * Database:           {app.config.get('ACTIVE_DB_ENGINE')}")
    print("=" * 65)
    app.run(host="0.0.0.0", port=port, debug=False)
