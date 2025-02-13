from wtforms import Form, StringField, RadioField, SelectField, TextAreaField, validators, IntegerField, DecimalField

class CreateSaleForm(Form):
    item_name = StringField('Item Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    category = RadioField('Category',[validators.DataRequired()], choices=[('W', 'Women'), ('M', 'Men'), ('K', 'Kids')], default='W')
    quantity_sold = IntegerField('Quantity Sold', [validators.DataRequired()])
    unit_price = DecimalField('Unit Price',[validators.DataRequired()], places=2, rounding=None, use_locale=False, number_format=None)
