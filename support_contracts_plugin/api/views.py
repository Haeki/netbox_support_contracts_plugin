from rest_framework.viewsets import ModelViewSet

from support_contracts_plugin.models import SupportContract
from .serializers import SupportContractSerializer


class SupportContractViewSet(ModelViewSet):
    queryset = SupportContract.objects.all()
    serializer_class = SupportContractSerializer

