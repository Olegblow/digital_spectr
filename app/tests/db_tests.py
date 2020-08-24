import pytest

from app import db as _db
from app.models import Category, Product


@pytest.fixture(scope='session')
def db(request):
    """Фикстура базы данных."""
    def close():
        _db.drop_all()

    _db.create_all()
    request.addfinalizer(close)
    return _db


@pytest.fixture
def category(db):
    _category = Category(name='name1')
    db.session.add(_category)
    db.session.commit()
    return _category


def test_db_create_category(db):
    category = Category(name='name1')
    assert category.id is None
    db.session.add(category)
    db.session.commit()
    assert category.id is not None
    category2 = Category.query.get(category.id)
    assert category is category2


def test_db_create_product(db, category):
    product1 = Product(name='product1', stock_balance=10, sku=123321, category_id=category.id)
    db.session.add(product1)
    product2 = Product(name='product2', stock_balance=10, sku=123321)
    db.session.add(product2)
    assert product1.id is None
    assert product2.id is None
    db.session.commit()
    assert product1.id is not None
    assert product2.id is not None
    product3 = Product.query.get(product1.id)
    assert product1 is product3
