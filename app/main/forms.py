from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, SelectField,\
    SubmitField, IntegerField
from wtforms.validators import DataRequired, Length, NumberRange, Email, InputRequired
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms import ValidationError
from flask_pagedown.fields import PageDownField
from .. import db
from ..models import Product, Category, Location, ProductStatus, ProductCatalogue


class NewProduct(FlaskForm):
    def categoryQuery():
        return db.session.query(Category)

    def locationQuery():
        return db.sesson.query(Location)

    def productStatusQuery():
        return db.session.query(ProductStatus)

    def productStatusQuery():
        return db.session.query(ProductCatalogue)

    product_catalogue = QuerySelectField(
        get_label='catalogue_id', query_factory=productStatusQuery)
    product_name = StringField(
        'Name', validators=[Length(0, 80), InputRequired()])
    product_description = StringField('Description', validators=[
                                      Length(0, 250), InputRequired()])
    product_price = IntegerField(
        'Price', validators=[NumberRange(min=0, max=10000), InputRequired()])
    category = QuerySelectField(get_label='category_name', query_factory=categoryQuery)
    quantity = IntegerField('Quantity', validators=[
                            NumberRange(min=0, max=100), InputRequired()])
    locaton = QuerySelectField(get_label='product_location', query_factory=locationQuery)
    status = QuerySelectField(
        get_label='product_status', query_factory=productStatusQuery())
    submit = SubmitField('Submit')
