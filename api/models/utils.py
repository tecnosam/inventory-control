import sqlalchemy.exc

from .. import db

from .exceptions import *


def push_instance(instance):
    try:
        db.session.add(instance)
        db.session.commit()

        return instance
    except sqlalchemy.exc.IntegrityError:
        raise DuplicateKeyException()


def edit_instance(instance, kwargs: list, preprocessors: dict):
    try:

        for key in kwargs:
            if key in preprocessors:
                processor = preprocessors[key]
                val = kwargs[key]
                setattr(instance, key, processor(val))

        db.session.commit()
        return instance

    except sqlalchemy.exc.IntegrityError:
        raise DuplicateKeyException()
