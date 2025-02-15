import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash

# Database Configuration (Match your app.py settings)
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'users.db')  # Or your PostgreSQL/MySQL URL

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
db = SQLAlchemy(app)

class User(db.Model):  # User Model (same as in app.py)
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

# Create the database tables (if they don't exist)
with app.app_context():
    db.create_all()

def create_initial_admin(username, password):
    with app.app_context():
        if User.query.filter_by(username=username).first() is None:  # Check if admin exists
            admin_user = User(username=username, is_admin=True)
            admin_user.set_password(password)  # Hash the password
            db.session.add(admin_user)
            db.session.commit()
            print(f"Admin user '{username}' created successfully.")
        else:
            print(f"Admin user '{username}' already exists.")

if __name__ == '__main__':
    admin_username = "admin"  # **Change if needed**
    admin_password = "Admin1#"  # **REPLACE with a STRONG password**
    create_initial_admin(admin_username, admin_password)