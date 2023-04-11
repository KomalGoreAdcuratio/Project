from rest_framework import serializers
from Bank.transferAmount.transferAmount import TransferAmount

class TransferAmountSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransferAmount
        fields = ['transactionId','accountNumber','type','amount']