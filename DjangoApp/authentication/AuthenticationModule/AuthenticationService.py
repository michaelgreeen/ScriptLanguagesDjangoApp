import hashlib
from common.logging import LOGGER

class AuthenticationModule:
    def authenticate(request):
        try:
            LOGGER.info('Trying to authenticate user')
            password = hashlib.sha256((str.password).encode())
        except Exception:
            LOGGER.info('User couldn''t have been authenticated')
            return None