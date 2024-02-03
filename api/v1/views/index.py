#!/usr/bin/python3
"""Define routes for blueprint
"""

from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status', strict_slashes=False)
def status():
    """Return status of application
    """
    return jsonify({'status': 'OK'})
