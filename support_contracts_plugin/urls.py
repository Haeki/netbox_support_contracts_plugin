from django.urls import path

from . import views


# Define a list of URL patterns to be imported by NetBox. Each pattern maps a URL to
# a specific view so that it can be accessed by users.
urlpatterns = (
    path('', views.ListSupportContractsView.as_view(), name='list_contracts'),
    path('<str:name>/', views.SupportContractView.as_view(), name='contract'),
)

