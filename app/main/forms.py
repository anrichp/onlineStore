from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, SelectField,\
    SubmitField, IntegerField, DecimalField
from wtforms.validators import DataRequired, Length, NumberRange, Email, InputRequired
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.widgets.html5 import NumberInput
from wtforms import ValidationError
from flask_pagedown.fields import PageDownField
from .. import db
from ..models import *


class NewProduct(FlaskForm):
    def categoryQuery():
        return db.session.query(Category)

    def locationQuery():
        return db.session.query(Location)

    def productStatusQuery():
        return db.session.query(ProductStatus)

    def productCatalogueQuery():
        return db.session.query(ProductCatalogue)

    product_catalogue = QuerySelectField(
        get_label='catalogue_id', query_factory=productCatalogueQuery)
    product_name = StringField(
        'Name', validators=[Length(0, 80), InputRequired()])
    product_description = StringField('Description', validators=[
                                      Length(0, 250), InputRequired()])
    product_price = IntegerField(
        'Price', validators=[InputRequired()], places=2, widget=NumberInput())
    category = QuerySelectField(
        get_label='category_name', query_factory=categoryQuery)
    quantity = IntegerField('Quantity', validators=[
                            NumberRange(min=0, max=100), InputRequired()])
    location = QuerySelectField(
        get_label='product_location', query_factory=locationQuery)
    status = QuerySelectField(
        get_label='product_status', query_factory=productStatusQuery)
    submit = SubmitField('Submit')


class NewCategory(FlaskForm):

    category_name = StringField(
        'Category Name', validators=[Length(0, 80), InputRequired()])
    submit = SubmitField('Submit')
