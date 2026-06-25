from functools import wraps

from flask import redirect, session, url_for


def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'logged' not in session or not session['logged']:
            return redirect(url_for('index'))

        return func(*args, **kwargs)

    return wrapper
