import pytest

from app import app as _app


@pytest.fixture(scope='session')
def app():
    """Фикстура приложения."""
    return _app


@pytest.mark.parametrize(
    'parameters',
    (
        ('api/v1/product', 200),
        ('api/v1/product?category_id=1', 200),
        ('api/v1/category', 200)
    )
)
@pytest.mark.smoke
def test_handler_get_product_and_category(client, parameters):
    url, status = parameters
    response = client.get(url)
    assert response.status_code == 200
    assert response.content_type == 'application/json'
    assert response.is_json is True


def test_handler_post_category_success(client):
    url = 'api/v1/category'
    data = {'name': 'category1'}
    response = client.post(url, json=data)
    assert response.status_code == 200
    assert response.content_type == 'application/json'
    assert response.is_json is True
    assert 'name' in response.json
    assert response.json['name'] == data['name']
    assert response.json['id'] is not None


@pytest.mark.parametrize(
    'parameters',
    (
        #  data, data response error
        ({'name2': 'qwe'}, {'name': ['Missing data for required field.'], 'name2': ['Unknown field.']}),
        ({'name': 123}, {'name': ['Not a valid string.']}),
        ({}, {'name': ['Missing data for required field.']})
    )
)
def test_handler_post_category_error(client, parameters):
    url = 'api/v1/category'
    data, data_error = parameters
    response = client.post(url, json=data)
    assert response.status_code == 400
    assert response.content_type == 'application/json'
    assert response.is_json is True
    assert response.json == data_error


def test_handler_product_success(client):
    url = 'api/v1/product'
    data = {
        'name': 'product1',
        'sku': 123321,
        'stock_balance': 100
    }
    response = client.post(url, json=data)
    assert response.status_code == 200
    assert response.is_json is True
    assert response.content_type == 'application/json'
    assert response.json['id']


@pytest.mark.parametrize(
    'parameters',
    (
        #  data, data response error
        ({}, {'name': ['Missing data for required field.'],
              'sku': ['Missing data for required field.']}),
        ({'name': 123,
          'sku': 'qwe',
          'stock_balance': 'qwe'}, {'name': ['Not a valid string.'],
                                    'sku': ['Not a valid integer.'],
                                    'stock_balance': ['Not a valid integer.']})
    )
)
def test_handler_product_error(client, parameters):
    url = 'api/v1/product'
    data, data_error = parameters
    response = client.post(url, json=data)
    assert response.status_code == 400
    assert response.json == data_error
