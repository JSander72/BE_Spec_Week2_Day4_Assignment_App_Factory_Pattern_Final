from flask import Flask
from flask_marshmallow import Marshmallow
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_caching import Cache

# app = Flask(__name__)

ma = Marshmallow()

limiter = Limiter( key_func=get_remote_address, default_limits=["25 per day", "2 per hour"], storage_uri="memory://")

Cache = Cache()