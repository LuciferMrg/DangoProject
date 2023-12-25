from django.apps import AppConfig


class TableorderappConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "tableOrderApp"
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = 'localhost.domain'
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True
    EMAIL_HOST_USER = 'dev23@localhost.domain'
    EMAIL_HOST_PASSWORD = '11111111'