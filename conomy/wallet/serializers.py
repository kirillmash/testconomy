from rest_framework import serializers

from .models import Wallet, Transaction


class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ('id', 'name', 'balance')
        read_only_fields = ('id', 'balance',)


class TransactionSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S", required=False)

    class Meta:
        model = Transaction
        fields = ('wallet', 'amount', 'type', 'status', 'created_at', 'description')
        read_only_fields = ('created_at', 'status')
