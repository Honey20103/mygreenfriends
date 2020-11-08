from .settings import * 
import os

# Testing should use a local db
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'), 
        'TEST': {
            'NAME': 'testingdb',
        },
    }
}

SECRET_KEY = 'hello2020'
