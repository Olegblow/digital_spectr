from functools import wraps

from flask import abort, jsonify, make_response
from marshmallow import ValidationError


def jsonify_exception(func):
    """Декоратор проверяющий ошибки и переводит их в json."""
    @wraps(func)
    def decorator(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValidationError as e:
            abort(make_response(jsonify(e.messages), 400))
        except Exception as e:
            err = {
                "status": "error",
                "description": e.args
            }
            abort(make_response(jsonify(err), 400))
    return decorator
