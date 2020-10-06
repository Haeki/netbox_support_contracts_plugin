from django.contrib import admin

from .models import SupportContract


@admin.register(SupportContract)
class SupportContractAdmin(admin.ModelAdmin):
    """
    This class defines a Django administrative view for the Animal model. The register()
    decorator above registers the view with NetBox's admin site object.
    """
    list_display = ('name', 'start_date', 'end_date')

