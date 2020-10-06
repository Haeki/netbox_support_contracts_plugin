from extras.plugins import PluginConfig


class SupportContractsConfig(PluginConfig):
    """
    This class defines attributes for the NetBox Support Contracts plugin.
    """
    # Plugin package name
    name = 'support_contracts_plugin'

    # Human-friendly name and description
    verbose_name = 'Support Contracts'
    description = 'Plugin that allows to create support contracts and add them to devices'

    # Plugin version
    version = '0.1'

    # Plugin author
    author = 'Mika Busch'
    author_email = 'mika.busch@allgeier-es.com'

    # Configuration parameters that MUST be defined by the user (if any)
    required_settings = []

    # Default configuration parameter values, if not set by the user
    #default_settings = {
    #    'loud': True
    #}

    # Base URL path. If not set, the plugin name will be used.
    base_url = 'support-contracts'

    # Caching config
    caching_config = {}


config = SupportContractsConfig

