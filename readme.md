# Pulumi Sample Projects
These two projects are only an example to test an Azure deployment using Python with Pulumi

The firts project create a simple Resource Group and a Storage Account using a random name
The second project, create a Resource Group, a Log Analythics Workspace and a number of storage account mased on maxinstances value you set during the configuration. 

## Instruction to use CSU-SAMPLE1:
1. Clone the repo
2. Run this command to create the python virtual environment: __python3 -m venv venv__
3. Run this command to create the first stack: __pulumi stack init < stack name >__
4. Run this command to create the first stack: __pulumi up__

## Instruction to use CSU-SAMPLE2:
1. Clone the repo
2. Run this command to create the python virtual environment: __python3 -m venv venv__
3. Run this command to create the first stack: __pulumi stack init < stack name >__
4. Add location variable in the stack: __pulumi config set azure:location < azure region name >__
5. Add maxinstances variable in the stack: __pulumi config set maxinstances < number of storage account to create >__
6. Run this command to create the first stack: __pulumi up__