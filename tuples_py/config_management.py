#!/usr/bin/python3

from collections import namedtuple

# Database configuration
DatabaseConfig = namedtuple('DatabaseConfig', ['host', 'port', 'username', 'database'])

# 1. Create configs for development, staging, and production
development = DatabaseConfig(
    host = "myhost",
    port = 123,
    username = "root",
    database = "postgres_db"
    )
staging = DatabaseConfig(
    host = "yourhost",
    port = 808,
    username = "joe",
    database = "postgres_db"
    )
production = DatabaseConfig(
    host = "localhost",
    port = 2355,
    username = "meridian",
    database = "postgres_db"
    )

# 2. Store them in a dictionary by environment name
configs = {
    "development": development,
    "staging": staging,
    "production": production
    }

