from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, SelectField,\
    SubmitField, IntegerField
from wtforms.validators import DataRequired, Length, NumberRange, Email, Regexp
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms import ValidationError
from flask_pagedown.fields import PageDownField
from .. import db
from ..models import Product, Category, Location, ProductStatus, ProductCatalogue


def categoryQuery():
    return db.session.query(Category)

def locationQuery():
    return db.sesson.query(Location)

def productStatusQuery():
    return db.session.query(ProductStatus)

def productStatusQuery():
    return db.session.query(ProductCatalogue)

class NewProduct(FlaskForm):

    product_catalogue = QuerySelectField(
        get_label='name', query_factory=productStatusQuery())
    product_name = StringField(
        'Name', validators=[Length(0, 80), InputRequired()])
    product_description = StringField('Description', validators=[
                                      Length(0, 250), InputRequired()])
    product_price = IntegerField(
        'Price', validators=[NumberRange(min=0, max=10000), InputRequired()])
    category = QuerySelectField(get_label='name', query_factory=categoryQuery)
    quantity = IntegerField('Quantity', validators=[
                            NumberRange(min=0, max=100), InputRequired()])
    locaton = QuerySelectField(get_label='name', query_factory=locationQuery)
    status = QuerySelectField(
        get_label='name', query_factory=productStatusQuery())
    submit - SubmitField('Submit')
