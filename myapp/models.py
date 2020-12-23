from django.db import models

class Transaction(models.Model):
    trans_from = models.CharField(max_length=32)
    trans_to = models.CharField(max_length=32)
    amount = models.IntegerField()
    date = models.DateField()

    