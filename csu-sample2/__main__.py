"""An Azure Python Pulumi program"""
import pulumi
from pulumi import get_stack
from pulumi_azure import core
from accountstorage import aStorage
from logan import logan

config = pulumi.Config()
mi=config.get_int('maxinstance')
env = get_stack()

# Create an Azure Resource Group
resource_group = core.ResourceGroup('resource_group',name='rgsa-' + env, location='uksouth')
accounts = []

log=logan(resource_group.name, resource_group.location)

# Create an Azure resource (Storage Account)
for x in range(mi):
        accounts.append(aStorage(resource_group.name,env + str(x)))
# Export the connection string for the storage account
for x in range(mi):
        pulumi.export('connection_string ' + env + str(x), accounts[x])
pulumi.export('Loganalytics', log)
