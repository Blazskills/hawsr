from .base import *  # noqa
from .base import env


DEBUG = env.bool("DJANGO_DEBUG", False)

CURRENT_ENV = env("CURRENT_ENV")


ADMINS = [("Ilesanmi Temitope", "ilesanmiisaac@gmail.com")]

# TODO:Change from localhost DOMAIN NAME  of the production server


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ROOT_DIR / 'db.sqlite3',
    }
}


SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="oXPWQPA3C3sdBCuBeXUKq3LBp9YDJ33-306p9EAKf1ja1xkWnKY",
)

ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

CSRF_TRUSTED_ORIGINS = ["http://localhost:8080", "http://127.0.0.1:8080",
                        "http://localhost:5173", "http://localhost:3000",
                        ]


CORS_ALLOWED_ORIGINS = ["http://localhost:5173", "http://localhost:5174", "http://localhost:3000", "http://localhost",
                        ]

CORS_ALLOW_CREDENTIALS = True

ADMIN_URL = env("DJANGO_ADMIN_URL")


SITE_NAME = "Hawsr"


DOMAIN = env("DOMAIN")

CORS_URLS_REGEX = r"^/api/.*$"


if CURRENT_ENV == "local":
    SECURE_SSL_REDIRECT = False
    SESSION_COOKIE_SECURE = False
    CSRF_COOKIE_SECURE = False

elif CURRENT_ENV == "live":
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

    SECURE_SSL_REDIRECT = env.bool("DJANGO_SECURE_SSL_REDIRECT", default=True)

    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True

    # TODO: Change to 518400 later
    SECURE_HSTS_SECONDS = 518400

    SECURE_HSTS_INCLUDE_SUBDOMAINS = env.bool("DJANGO_SECURE_HSTS_INCLUDE_SUBDOMAINS", default=True)

    SECURE_CONTENT_TYPE_NOSNIFF = env.bool("DJANGO_SECURE_CONTENT_TYPE_NOSNIFF", default=True)
