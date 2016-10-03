import sys
import site
sys.path.insert(0, '/var/www/danielle')
site.addsitedir('/var/www/danielle/lib/python2.7/site-packages')
from app import app as application
