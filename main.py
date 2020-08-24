import logging

from app import app

log = logging.getLogger(__name__)


app.run(host='0.0.0.0', port='8080', debug=True)