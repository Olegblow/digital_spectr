from app import ma

from app.models import Category
from app.models import Product


class CategorySchema(ma.SQLAlchemySchema):
    """Схема данных категорий товара."""

    class Meta:
        model = Category

    id = ma.auto_field()
    name = ma.auto_field()
    products = ma.auto_field()


class ProductSchema(ma.SQLAlchemyAutoSchema):
    """Схема данных товара."""

    class Meta:
        model = Product
        include_fk = True


category_schema = CategorySchema()
categories_schema = CategorySchema(many=True)
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)
