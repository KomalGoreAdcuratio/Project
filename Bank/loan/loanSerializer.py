from rest_framework import serializers
from Bank.loan.loan import Loan

class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = '__all__'