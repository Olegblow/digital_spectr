from app import db


class Category(db.Model):
    """Модель данных категори товара."""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(127), nullable=False) #  Название категории.
    products = db.relationship('Product', backref='category', lazy=True)

    def __repr__(self):
        return f'Category {self.name!r}'

    def commit(self) -> None:
        """Создает запись в базе."""
        db.session.add(self)
        db.session.commit()


class Product(db.Model):
    """Модель данных товара."""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(127), nullable=False) #  Название товара.
    stock_balance = db.Column(db.Integer) #  Остаток на складе.
    sku = db.Column(db.Integer, nullable=False) #  Stock Keeping Unit
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))

    def __repr__(self):
        return f'Product {self.name!r}.'

    def commit(self) -> None:
        """Создает запись в базе."""
        db.session.add(self)
        db.session.commit()

    def delete(self) -> None:
        """Удаление записи из базы."""
        db.session.delete(self)
        db.session.commit()

    def update(self) -> None:
        db.session.commit()
