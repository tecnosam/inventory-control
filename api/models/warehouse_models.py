from .. import db

from .utils import push_instance, edit_instance


class Warehouse(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    n_floors = db.Column(db.Integer, nullable=False, default=1)
    capacity = db.Column(db.Float, nullable=False)
    location = db.Column(db.String(200), nullable=False)
    goods = db.relationship("StockPile", backref='warehouse', lazy=True)

    @staticmethod
    def add(**kwargs):
        _warehouse = Warehouse(**kwargs)
        return push_instance(_warehouse)

    @staticmethod
    def edit(wid, **kwargs):
        _warehouse = Warehouse.query.get(wid)
        return edit_instance(_warehouse)

    def delete(self):
        # TODO: delete all stocks in warehouse or move them to another warehouse
        db.session.delete(self)
        db.session.commit()
        return self

    def full(self) -> bool:
        # sum all area of stockPiles and subtract from capacity
        return False
