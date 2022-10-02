from datetime import timedelta

from django.conf import settings
from django.test.signals import setting_changed
from rest_framework.settings import APISettings, api_settings

from backend.settings import REST_AtAUTH

USER_SETTINGS = getattr(settings, 'REST_AtAUTH', REST_AtAUTH)

DEFAULTS = {
    'SECURE_HASH_ALGORITHM': 'cryptography.hazmat.primitives.hashes.SHA512',
    'AUTH_TOKEN_CHARACTER_LENGTH': 64,
    'TOKEN_TTL': timedelta(hours=10),
    'USER_SERIALIZER': None,
    'TOKEN_LIMIT_PER_USER': None,
    'AUTO_REFRESH': False,
    'MIN_REFRESH_INTERVAL': 60,
    'AUTH_HEADER_PREFIX': 'Token',
    'EXPIRY_DATETIME_FORMAT': api_settings.DATETIME_FORMAT,
}

IMPORT_STRINGS = {
    'SECURE_HASH_ALGORITHM',
    'USER_SERIALIZER',
}

AtAUTH_settings = APISettings(USER_SETTINGS, DEFAULTS, IMPORT_STRINGS)

def reload_api_settings(*args, **kwargs):
    global AtAUTH_settings
    setting, value = kwargs['setting'], kwargs['value']
    if setting == 'REST_AtAUTH':
        AtAUTH_settings = APISettings(value, DEFAULTS, IMPORT_STRINGS)


setting_changed.connect(reload_api_settings)


class _CONSTANTS:
    '''
    Constants cannot be changed at runtime
    '''
    TOKEN_KEY_LENGTH = 8
    DIGEST_LENGTH = 128

    def __setattr__(self, *args, **kwargs):
        raise Exception('''
            Constant values must NEVER be changed at runtime, as they are
            integral to the structure of database tables
            ''')


CONSTANTS = _CONSTANTS()
