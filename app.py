
import re
from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from wtforms import Form, StringField, PasswordField, validators, ValidationError
from sqlalchemy import func

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # CHANGE THIS!
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def _repr_(self):
        return '<User %r>' % self.username

with app.app_context():
    db.create_all()

def validate_username(form, field):
    if not re.match(r'^[a-zA-Z0-9_]+$', field.data):
        raise ValidationError('Username can only contain letters, numbers, and underscores.')

def validate_password(form, field):
    if len(field.data) < 6:
        raise ValidationError("Password must be at least 6 characters long.")
    if not re.search("[a-z]", field.data):
        raise ValidationError("Password must contain at least one lowercase letter.")
    if not re.search("[A-Z]", field.data):
        raise ValidationError("Password must contain at least one uppercase letter.")
    if not re.search("[^a-zA-Z0-9]", field.data):
        raise ValidationError("Password must contain at least one special character.")


class RegistrationForm(Form):
    username = StringField('Username', [
        validators.Length(min=4, max=80),
        validators.DataRequired(),
        validate_username
    ])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validate_password,
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Confirm Password')

class LoginForm(Form):
    username = StringField('Username', [validators.DataRequired()])
    password = PasswordField('Password', [validators.DataRequired()])

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        username = form.username.data
        password = form.password.data

        if User.query.filter_by(username=username).first():
            flash('Username already exists.')
            return redirect(url_for('register'))

        new_user = User(username=username.lower())
        new_user.set_password(password)

        db.session.add(new_user)
        db.session.commit()
        print(f"User registered: {new_user.username}")
        flash('Registration successful! Please login.')
        return redirect(url_for('login'))

    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    usernames = [user.username for user in User.query.order_by(func.lower(User.username)).all()]
    print(f"Usernames fetched: {usernames}")

    if request.method == 'POST' and form.validate():
        username = form.username.data.strip().lower()
        password = form.password.data

        user = User.query.filter(func.lower(User.username) == username).first()

        if user and user.check_password(password):
            session['user_id'] = user.id
            session['username'] = user.username
            session['is_admin'] = user.is_admin
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password.')
            return redirect(url_for('login'))

    return render_template('login.html', form=form, usernames=usernames)

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    user = User.query.get(session['user_id'])
    users = User.query.all()
    return render_template('dashboard.html', users=users, current_user=user)

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('username', None)
    session.pop('is_admin', None)
    return redirect(url_for('index'))

@app.route('/user/delete/<int:id>')
def delete_user(id):
    if 'user_id' not in session or not session.get('is_admin'):
        flash("You are not authorized to perform this action.")
        return redirect(url_for('dashboard'))

    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('dashboard'))

if __name__ == '__main__':
    app.run(debug=True)