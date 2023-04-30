from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.core.exceptions import ValidationError
import datetime

from .algo_choices import ALGORITHM_CHOICES

class OrdersData(models.Model):
    
    coin = models.TextField()
    amount = models.FloatField(null=False)
    n_orders = models.IntegerField(null=False)
    init_price = models.FloatField(null=False)
    rate_changes = models.IntegerField(null=False)
    martingale = models.IntegerField(null=False)
    f_order_indent = models.FloatField(null=False)
    commission = models.FloatField(null=False)
    algorithm = models.CharField(
        max_length=5,
        choices=ALGORITHM_CHOICES,
        default='short',
    )

    def __str__(self):
        return str(self.coin)