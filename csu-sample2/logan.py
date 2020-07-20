import pulumi
import pulumi_azure as azure

def logan(rg_name,rg_location):
    example_analytics_workspace = azure.operationalinsights.AnalyticsWorkspace("logworkspace",
        location=rg_location,
        resource_group_name=rg_name,
        sku="PerGB2018",
        retention_in_days=30)
    return example_analytics_workspace.id
