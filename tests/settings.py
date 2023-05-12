"""Settings module for test app."""
ENV = "development"
TESTING = True
SECRET_KEY = "not-so-secret-in-tests"
DEBUG_TB_ENABLED = False
CACHE_TYPE = "simple"  # Can be "memcached", "redis", etc.
