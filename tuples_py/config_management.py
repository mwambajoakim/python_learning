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
ports = range(1, 65535)
print(ports)

# 3. Create a function that validates port numbers (1-65535)
def port_validator(config):
    errors = []
    for env, config in config.items():
        if config.port < 1 and config.port > 65535:
            print("Enter a valid port number")
        else:
            print("Initializing...")
# 4. Convert config to connection string format
for env, config in configs.items():
    str(config)

print(configs)
