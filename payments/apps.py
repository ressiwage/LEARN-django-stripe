from django.apps import AppConfig
from django.conf import settings # new
import stripe


class PaymentsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'payments'
