from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class AccountType(models.Model):
    account_type                    = models.CharField(max_length=20,choices=(("Savings", "Savings"),
                                                                        ("Current", "Current"),
                                                                        ("BasicSavings", "BasicSavings")
                                                                    )
                                                                )
class Account(models.Model):
    account_id                      = models.AutoField(primary_key=True)
    amount                          = models.IntegerField(validators=[MinValueValidator(0),
                                       MaxValueValidator(5000000)])
    type_of                         = models.ManyToManyField(AccountType)

class TransferAmount(models.Model):
    transfer_from_account                    = models.ForeignKey('Account', on_delete=models.DO_NOTHING, related_name='from_account')
    transfer_to_account                      = models.ForeignKey('Account', on_delete=models.DO_NOTHING,related_name='to_account')
    transfer_amount                          = models.IntegerField(default=0)
    transfered_at                            = models.DateTimeField(auto_now_add=False)