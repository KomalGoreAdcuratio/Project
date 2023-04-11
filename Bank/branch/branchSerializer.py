from rest_framework import serializers

from Bank.branch.branch  import Branch

class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ['id', 'name', 'loc']
    