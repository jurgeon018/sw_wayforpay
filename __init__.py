from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class WayforpayConfig(AppConfig):
    name = 'sw_wayforpay'
    verbose_name = _("Wayforpay")
    verbose_name_plural = verbose_name


default_app_config = 'sw_wayforpay.WayforpayConfig'



