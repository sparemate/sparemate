from flask_wtf.file import FileAllowed,FileField,FileRequired
from wtforms import Form,IntegerField,BooleanField,TextAreaField,validators,StringField,DecimalField

class Addproducts(Form):
    
    
    name=StringField('Name',[validators.DataRequired()])
    price=IntegerField('price',[validators.DataRequired()])
    discount=IntegerField('discount',)
    stock=IntegerField('stock',[validators.DataRequired()])
    origin=StringField('origin',[validators.DataRequired()])
    condition=StringField('condition',[validators.DataRequired()])
    description=TextAreaField('description',[validators.DataRequired()])
    install_service=StringField('install_service',[validators.DataRequired()])
    colors=TextAreaField('colors',[validators.DataRequired()],default=None)
    image_1 = FileField('image_1', validators=[FileAllowed(['jpg','png','gif','jpeg'])])
    image_2 = FileField('image_2', validators=[FileAllowed(['jpg','png','gif','jpeg'])])
    image_3 = FileField('image_3', validators=[FileAllowed(['jpg','png','gif','jpeg'])])
    certificate = FileField('certificate', validators=[FileAllowed(['jpg','png','gif','jpeg'])])
    yt=StringField('Youtube Video')

    

