# Документация по API

## Категории


Объект `Категория`:

- `id` -- ID Категории в БД.
- `name` -- Название категории.
- `products` -- Список ID связанных товаров.


### Создание категорий

Запрос:  `POST /api/v1/category`

Тело запроса:

```json5
{
    "name": "string"
}

```

Ответ:

```json5
{
    "id": "integer",
    "name": "string",
    "products": ["integer"]
}
```


### Получения списка категорий

Запрос: `GET /api/v1/category`

Ответ:
```json5
[
    {
        "id": "integer",
        "name": "string",
        "products": ["integer"]
    }
]
```


## Товары

Объект `Категории`:

- `id` -- ID товара в БД.
- `name` -- Имя товара.
- `sku` -- Идентификатор товарной позиции (Stock Keeping Unit).
- `stock_balance` -- Остаток на складе.
- `category_id` -- ID категории товара.


### Получение списка товаров
Запрос:

- `GET /api/v1/product`

Ответ:

```json5
[
    {
        "id": "integer",
        "name": "string",
        "sku": "integer",
        "stock_balance": "integer",
        "category_id": "integer"
    }
]
```
Фильтрация:
- `GET /api/v1/product?category_id=<integer>` -- Доступна фильтрация по типу категории товара. Принимает ID категории.

### Создание товара

Запрос:

- `POST /api/v1/product`

Тело запроса:

```json5
{
    "name": "string",
    "sku": "integer",
    "stock_balance": "integer",
    "category_id": "integer"
}
```

Ответ:
```json5
 {
    "id": "integer",
    "name": "string",
    "sku": "integer",
    "stock_balance": "integer",
    "category_id": "integer"
}
```


### Изменение кол-во остатка на складе товара

Запрос:
- `PUT /api/v1/product/<product_id>`
- - `product_id` -- ID товара

Ответ:

```json5
 {
    "id": "integer",
    "name": "string",
    "sku": "integer",
    "stock_balance": "integer",
    "category_id": "integer"
}
```

### Удаление товара

Запрос:

- `DELETE /api/v1/product/<product_id>`
- - `product_id` -- ID товара

Ответ:

```json5
 {
    "id": "integer",
    "name": "string",
    "sku": "integer",
    "stock_balance": "integer",
    "category_id": "integer"
}
```
