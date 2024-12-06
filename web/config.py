import os
import logging

LOGGING_CONFIG = {
    'version': 1,
    'formatters': {
        'default': {
            'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
        }
    },
    'handlers': {
        'file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': '/var/log/secureauth/app.log',
            'maxBytes': 1024 * 1024,  # 1MB
            'backupCount': 10,
            'formatter': 'default',
        },
    },
    'root': {
        'level': 'INFO',
        'handlers': ['file']
    }
} 