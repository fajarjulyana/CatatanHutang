import os
import logging
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from werkzeug.middleware.proxy_fix import ProxyFix

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Inisialisasi SQLAlchemy (pakai db.Model)
db = SQLAlchemy()

# Create the app
app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "dev-secret-key-change-in-production")
app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)

# Path absolut database SQLite
db_path = os.path.join(os.getcwd(), "debt_tracker.db")
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_path}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {
    "pool_recycle": 300,
    "pool_pre_ping": True,
}

# Initialize app dengan db
db.init_app(app)

# Import routes setelah app dibuat
from routes import *

with app.app_context():
    # Import models untuk bisa baca data
    import models
    
    # Tidak perlu db.create_all() karena database sudah ada
    from sqlalchemy import inspect
    inspector = inspect(db.engine)
    logging.info(f"Tabel yang ada di database: {inspector.get_table_names()}")

if __name__ == '__main__':
    import webbrowser
    import threading
    import time
    import platform
    import subprocess

    def open_browser():
        time.sleep(2)
        url = "http://127.0.0.1:5002/"
        if platform.system() == "Windows":
            try:
                subprocess.Popen(["cmd", "/c", f'start chrome --kiosk {url}'])
            except Exception as e:
                print(f"Gagal buka fullscreen: {e}")
                webbrowser.open(url)
        else:
            webbrowser.open(url)

    threading.Thread(target=open_browser).start()
    app.run(host='0.0.0.0', port=5002, debug=True)
