import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/home/josh/Public/mapa_app/")

from mapa_app import app as application
application.secret_key = 'fhkjdskjgf'
