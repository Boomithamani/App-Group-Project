from wtforms import Form, StringField, RadioField, SelectField, TextAreaField, validators
from wtforms.fields import EmailField, DateField

def validate_name(form, field):
    if not field.data.replace(" ", "").isalpha():
        raise validators.ValidationError("Name must contain only letters.")

def validate_email_domain(form, field):
    allowed_domains = ["gmail.com", "yahoo.com"]
    if "@" not in field.data or field.data.split("@")[-1] not in allowed_domains:
        raise validators.ValidationError("Email must be from a valid domain (gmail.com, yahoo.com).")

def validate_feedback_length(form, field):
    if len(field.data.split()) < 2:
        raise validators.ValidationError("Feedback must be at least 2 words long.")

# Updated form class with additional validations
class CreateUserForm(Form):
    first_name = StringField('First Name', [
        validators.Length(min=1, max=150),
        validators.DataRequired(),
        validate_name
    ])

    last_name = StringField('Last Name', [
        validators.Length(min=1, max=150),
        validators.DataRequired(),
        validate_name
    ])

    email = EmailField('Email', [
        validators.Email(),
        validators.DataRequired(),
        validate_email_domain
    ])

    remarks = TextAreaField('Feedback', [
        validators.DataRequired(),
        validate_feedback_length
    ])


