import binascii
from os import urandom as generate_bytes

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes

from app_token_auth.settings import AtAUTH_settings

sha = AtAUTH_settings.SECURE_HASH_ALGORITHM


def create_token_string():
    return binascii.hexlify(
        generate_bytes(int(AtAUTH_settings.AUTH_TOKEN_CHARACTER_LENGTH / 2)) # type: ignore
    ).decode()


def hash_token(token):
    '''
    Calculates the hash of a token.
    input is unhexlified

    token must contain an even number of hex digits or a binascii.Error
    exception will be raised
    '''
    digest = hashes.Hash(sha(), backend=default_backend()) #type: ignore
    digest.update(binascii.unhexlify(token))
    return binascii.hexlify(digest.finalize()).decode()
