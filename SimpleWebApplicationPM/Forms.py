from flask_wtf import Form
from wtforms import StringField, SelectField, DecimalField, FileField
from wtforms.validators import DataRequired

from flask_wtf import Form
from wtforms import StringField, SelectField, DecimalField, FileField
from wtforms.validators import DataRequired, NumberRange

class CreateListingForm(Form):
    name = StringField('Shirt Name', validators=[DataRequired()])
    sizing = SelectField('Size', choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large')], validators=[DataRequired()])
    category = SelectField('Category', choices=[('men', 'Men'), ('women', 'Women'), ('kids', 'Kids')], validators=[DataRequired()])
    price = DecimalField('Price', places=2, validators=[DataRequired(), NumberRange(min=0.01, max=60, message="Price must be between $0 and $60")])
    picture = FileField('Picture', validators=[DataRequired()])

