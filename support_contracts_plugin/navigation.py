from extras.plugins import PluginMenuButton, PluginMenuItem
from utilities.choices import ButtonColorChoices


# Declare a list of menu items to be added to NetBox's built-in naivgation menu
menu_items = (

    # Each PluginMenuItem instance renders a custom menu item. Each item may have zero or more buttons.
    PluginMenuItem(
        link='plugins:support_contracts_plugin:list_contracts',
        link_text='List all Support Contracts',
        permissions=[],
        buttons=(
            # Add a green button which links to the admin view to add a new contract. This
            # button will appear only if the user has the "add_animal" permission.
            PluginMenuButton(
                link='admin:support_contracts_plugin_supportContract_add',
                title='Add a new Contract',
                icon_class='fa fa-plus',
                color=ButtonColorChoices.GREEN,
                permissions=['support_contracts_plugin.add_contract']
            ),
        )
    ),

)

