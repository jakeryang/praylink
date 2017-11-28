from functools import wraps
from flask import session, request, redirect, url_for, abort

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get('is_admin') is None:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function