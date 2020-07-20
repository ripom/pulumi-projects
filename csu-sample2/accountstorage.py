"""An Azure Python Pulumi program"""

import pulumi
from pulumi_azure import storage

def aStorage(rg_name, suff):
# Create an Azure resource (Storage Account)
    account=storage.Account('storagerick' + suff,
                          name='cicciopasticcio' + suff.lower(),
                          # The location for the storage account will be derived automatically from the resource group.
                          resource_group_name=rg_name,
                          account_tier='Standard',
                          account_replication_type='LRS',
                          tags={"Environment": "Dev", "CostCenter": "12345"})
# Export the connection string for the storage account
    return account.primary_connection_string
