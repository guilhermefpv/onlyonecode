# -*- coding: utf-8 -*-
"""Application configuration.

Most configuration is set via environment variables.

For local development, use a .env file to set
environment variables.
"""
from environs import Env

env = Env()
env.read_env()

ENV = env.str("FLASK_ENV", default="production")
DEBUG = ENV == "development"
DSN_SENTRY = env("DSN_SENTRY", default=None)
SECRET_KEY = env.str("SECRET_KEY")
DEBUG_TB_ENABLED = DEBUG
DEBUG_TB_INTERCEPT_REDIRECTS = False
CACHE_TYPE = "SimpleCache"  # Can be "MemcachedCache", "RedisCache", etc.
CACHE_DEFAULT_TIMEOUT = 300
# OpenTelemetry + SigNoz
OTEL_RESOURCE_ATTRIBUTES = "service.name=clocktime-app"
# Replace to appropriate SigNoz OtelCollector endpoint, if applicable
# OTEL_EXPORTER_OTLP_ENDPOINT = "http://signoz:4318"
OTEL_EXPORTER_OTLP_ENDPOINT = "http://signoz:4317"
OTEL_PYTHON_FLASK_EXCLUDED_URLS = "client/.*/info,healthcheck"
