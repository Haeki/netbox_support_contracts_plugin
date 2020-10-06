from rest_framework.serializers import ModelSerializer
from support_contracts_plugin.models import SupportContract

class SupportContractSerializer(ModelSerializer):

    class Meta:
        model = SupportContract
        fields = ('id', 'name', 'start_date', 'end_date')

