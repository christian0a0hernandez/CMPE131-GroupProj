from wtforms import StringField, Form, DecimalField, SubmitField, IntegerField, TextAreaField, validators, BooleanField
from flask_wtf.file import FileAllowed, FileField, FileRequired


# class SearchForm(Form):
# search = StringField('search', [DataRequired()])
# submit = SubmitField('Search', render_kw={'class': 'btn btn-success btn-block'})

class Addproducts(Form):
    name = StringField('Name', [validators.DataRequired()])
    price = DecimalField('Price', [validators.DataRequired()])
    discount = IntegerField('Discount', default=0)
    stock = IntegerField('Stock', [validators.DataRequired()])
    description = TextAreaField("Description", [validators.DataRequired()])
    #colors = TextAreaField('Colors', [validators.DataRequired()])
    image_1 = FileField('Image 1', validators=[FileRequired(), FileAllowed(['jpg', 'png'])])
    image_2 = FileField('Image 1', validators=[FileRequired(), FileAllowed(['jpg', 'png'])])
    image_3 = FileField('Image 1', validators=[FileRequired(), FileAllowed(['jpg', 'png'])])
