from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import AccessToken
from datetime import datetime

User = get_user_model()


def create_jwt_pair_for_user(user: User):
    refresh = RefreshToken.for_user(user)
    decoded_token = AccessToken(token=str(refresh.access_token))
    expiration_timestamp = decoded_token['exp']
    expiration_date = datetime.utcfromtimestamp(expiration_timestamp)
    tokens = {
        "access": str(refresh.access_token),
        "refresh": str(refresh),
        "expiresAt": expiration_date
    }
    return tokens
