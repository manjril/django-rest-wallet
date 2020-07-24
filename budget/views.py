from budget.models import b2bWallet, b2bTransactions
from budget.serializers import WalletSerializer, TransactionSerializer, WalletUpdateSerializer

from rest_framework import viewsets
from rest_framework.response import Response

from django.db import connection


### Viewsets


class TransactionViewset(viewsets.ModelViewSet):
    queryset = b2bTransactions.objects.all()
    serializer_class = TransactionSerializer


class WalletViewset(viewsets.ReadOnlyModelViewSet):
    queryset = b2bWallet.objects.all()
    serializer_class = WalletSerializer


class BalanceUpdateViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = WalletUpdateSerializer

    def list(self, request):
        sql = 'UPDATE budget_b2bwallet ' \
              'SET budget_b2bwallet.balance = (' \
              'SELECT SUM(budget_b2btransactions.amount) ' \
              'FROM budget_b2btransactions ' \
              'WHERE budget_b2bwallet.id = budget_b2btransactions.wallet_id ' \
              'GROUP BY budget_b2btransactions.wallet_id' \
              ')'

        with connection.cursor() as cursor:
            cursor.execute(sql)

        return Response("Wallet Balance Updated. Please go back to API-ROOT to continue!")
