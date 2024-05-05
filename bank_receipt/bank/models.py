from django.db import models

# Create your models here.

class details(models.Model):
    Transaction = models.CharField(max_length=50, blank=True, null=True)
    Sender_name = models.CharField(max_length=50, blank=True, null=True)
    Senders_country = models.CharField(max_length=50, blank=True, null=True)
    Recipents_name = models.CharField(max_length=20, blank=True, null=True)
    Recipents_country = models.CharField(max_length=20, blank=True, null=True)
    Senders_bank = models.CharField(max_length=20, blank=True, null=True)
    Recipents_bank = models.CharField(max_length=20, blank=True, null=True)
    Transfer_amount = models.CharField(max_length=20, blank=True, null=True)
    Transfer_date = models.DateTimeField(max_length=20, blank=True, null=True)
    Status_update = models.CharField(max_length=20, blank=True, null=True)
    Estimated_delivery = models.CharField(max_length=20, blank=True, null=True)
    Recipents_IBAN = models.CharField(max_length=20, blank=True, null=True)
    
    def __str__(self):
        return str(self.Sender_name)