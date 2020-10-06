from django.shortcuts import get_object_or_404, render
from django.views.generic import View

from .models import SupportContract


class ListSupportContractsView(View):
    """
    List all Support Contracts in the database.
    """
    def get(self, request):
        contracts = SupportContract.objects.all()
        return render(request, 'support_contracts_plugin/contracts_list.html', {
            'contracts': contracts,
        })


class SupportContractView(View):
    """
    Display a single Support Contract, identified by name in the URL.
    """
    def get(self, request, name):
        contract = get_object_or_404(SupportContract.objects.filter(name=name))
        return render(request, 'support_contracts_plugin/contract.html', {
            'contract': contract,
        })
