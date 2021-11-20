from .. import db

from .utils import push_instance, edit_instance


class Product(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    name = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Float, nullable=False, default=0)

    SKU = db.Column(db.String(10), nullable=False, unique=True)
    size = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(100), nullable=False)

    warehouses = db.relationship("Warehouse", backref="product")
