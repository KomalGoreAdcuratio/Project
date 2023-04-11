from rest_framework import serializers
from Bank.account.account import Account

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ["accountNumber","branch_Id","name","type","address","balance"]

    