# Database Configuration for PostgreSQL Connection

import os

DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://user:password@localhost/dbname')
POOL_SIZE = int(os.getenv('POOL_SIZE', 5))
MAX_OVERFLOW = int(os.getenv('MAX_OVERFLOW', 10))

# Example configuration
def get_database_config():
    return {
        'DATABASE_URL': DATABASE_URL,
        'POOL_SIZE': POOL_SIZE,
        'MAX_OVERFLOW': MAX_OVERFLOW
    }