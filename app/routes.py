from flask import Response, request
from flask.views import MethodView

from app import app
from app.models import Category, Product
from app.schema import (categories_schema, category_schema, product_schema,
                        products_schema)

from .utils import jsonify_exception


class CategoriesHandler(MethodView):
    """Класс хэндлеров для показа всего списка объектов категории и создания их."""

    decorators = [jsonify_exception]

    def get(self) -> Response:
        """Хэндлер возвращает список json объектов Категорий."""
        categories = Category.query.all()
        return categories_schema.jsonify(categories)

    def post(self) -> Response:
        """Хэнрел для создания объекта категории."""
        data = category_schema.load(request.json)
        category = Category(**data)
        category.commit()
        return category_schema.dump(category)


class ProductHandler(MethodView):
    """Хэндлер для создания, получения списка, изменения товаров."""

    decorators = [jsonify_exception]

    def get(self) -> Response:
        """Хэндлер возвращает список json объектов товаров с возможностью фильтраци по типу категории."""
        category_id = request.args.get('category_id')
        if category_id:
            products = Product.query.filter_by(category_id=category_id).all()
        else:
            products = Product.query.all()
        return products_schema.jsonify(products)

    def post(self) -> Response:
        """Хэндлер создания объекта товара."""
        data = product_schema.load(request.json)
        product = Product(**data)
        product.commit()
        return product_schema.dump(product)

    def delete(self, product_id):
        """Хэнждел удаление товара."""
        product = Product.query.get(product_id)
        product.delete()
        return product_schema.dump(product)

    def put(self, product_id) -> Response:
        """Хэндлер изменения остатка товара на складе."""
        data = request.json['stock_balance']
        product = Product.query.get(product_id)
        product.stock_balance = data
        product.update()

        return product_schema.dump(product)


product_handler = ProductHandler.as_view('products_handler')
app.add_url_rule('/api/v1/category', view_func=CategoriesHandler.as_view('categories_handler'))
app.add_url_rule('/api/v1/product/<product_id>', view_func=product_handler, methods=['PUT', 'DELETE'])
app.add_url_rule('/api/v1/product', view_func=product_handler, methods=['GET', 'POST'])
