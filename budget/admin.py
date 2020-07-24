from django.contrib import admin
from .models import b2bWallet, b2bTransactions


# Register your models here.
admin.site.register(b2bWallet)
admin.site.register(b2bTransactions)

