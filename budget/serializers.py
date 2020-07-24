from rest_framework import serializers

from budget.models import b2bWallet, b2bTransactions


class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = b2bWallet
        fields = '__all__'


WALLET_CHOICES = (
    (1, 'BitCoin'),
    (2, 'Etherium'),
    (3, 'Basic Attention Token'),
    (4, 'Ripple'),
)


class TransactionSerializer(serializers.ModelSerializer):
    wallet = WalletSerializer(read_only=True)
    wallet_id = serializers.ChoiceField(choices=WALLET_CHOICES)

    class Meta:
        model = b2bTransactions
        fields = '__all__'


class WalletUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = b2bWallet
        fields = '__all__'
