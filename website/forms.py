from wtforms import StringField, Form, SubmitField, IntegerField, TextAreaField, validators, BooleanField
from flask_wtf.file import FileAllowed, FileField, FileRequired


# class SearchForm(Form):
# search = StringField('search', [DataRequired()])
# submit = SubmitField('Search', render_kw={'class': 'btn btn-success btn-block'})

class Addproducts(Form):
    name = StringField('Name', [validators.DataRequired()])
    price = IntegerField('Price', [validators.DataRequired()])
    discount = IntegerField('Discount', default=0)
    stock = IntegerField('Stock', [validators.DataRequired()])
    description = TextAreaField("Description", [validators.DataRequired()])
    colors = TextAreaField('Colors', [validators.DataRequired()])

    #image_1 = FileField('Image 1', validators=[FileRequired(), FileAllowed(['jpg', 'png']), 'Accepts images'])
    #image_2 = FileField('Image 1', validators=[FileRequired(), FileAllowed(['jpg', 'png']), 'Accepts images'])
    #image_3 = FileField('Image 1', validators=[FileRequired(), FileAllowed(['jpg', 'png']), 'Accepts images'])
