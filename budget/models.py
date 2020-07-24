from django.db import models
from django.utils.translation import ugettext as _


class b2bWallet(models.Model):
    LABEL_CHOICES = (
        ('btc', 'BitCoin'),
        ('eth', 'Etherium'),
        ('bat', 'Basic Attention Token'),
        ('xrp', 'Ripple'),
    )

    label = models.CharField(max_length=15, choices=LABEL_CHOICES, default='btc')
    balance = models.DecimalField(decimal_places=18, max_digits=36, blank=True, default=0.00)

    class Meta:
        verbose_name = "Wallet"
        verbose_name_plural = "Wallets"
        ordering = ('id',)

    def __str__(self):
        return str(self.id)


class b2bTransactions(models.Model):
    wallet = models.ForeignKey(b2bWallet, verbose_name='Wallet', on_delete=models.CASCADE)
    tx_id = models.CharField(max_length=50, unique=True)
    amount = models.DecimalField(max_digits=36, decimal_places=18)

    class Meta:
        verbose_name = _("Transaction")
        verbose_name_plural = _("Transactions")
        ordering = ('-tx_id',)

    def __str__(self):
        return str('$ %s (%s)' % (self.amount, self.tx_id))
