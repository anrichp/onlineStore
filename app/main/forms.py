from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, SelectField,\
    SubmitField
from wtforms.validators import DataRequired, Length, Email, Regexp
from wtforms import ValidationError
from flask_pagedown.fields import PageDownField
from ..models import Product


class NewProduct(FlaskForm):
    def categoryQuery():
        return db.session.query(Category)

    def locationQuery():
        return db.sesson.query(Location)

    def productStatusQuery():
        return db.session.query(ProductStatus)

    product_name  = StringField('Name' validators=[Length(0,80), InputRequired()])
    product_description = StringField('Description', validators=[Length(0, 250), InputRequired()])
    category = QuerySelectField(get_label='name', query_factory=categoryQuery)
    locaton = QuerySelectField(get_label='name', query_factory=locationQuery)
    status = QuerySelectField(get_label='name', query_factory=productStatusQuery())