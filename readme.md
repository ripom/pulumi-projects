# Pulumi Sample Projects
These two projects are only an example to test an Azure deployment using Python with Pulumi

The firts project create a simple Resource Group and a Storage Account using a random name
The second project, create a Resource Group, a Log Analythics Workspace and a number of storage account mased on maxinstances value you set during the configuration. 

```CSU-SAMPLE1
Instruction to use CSU-SAMPLE1:
* Clone the repo
* Run this command to create the python virtual environment: __python3 -m venv venv__
* Run this command to create the first stack: __pulumi stack init <stack name>__
```

```CSU-SAMPLE2
Instruction to use CSU-SAMPLE2:
* Clone the repo
* Run this command to create the python virtual environment: __python3 -m venv venv__
* Run this command to create the first stack: __pulumi stack init <stack name>__
* Add location variable in the stack: __pulumi config set azure:location <azure region name>__
* Add maxinstances variable in the stack: __pulumi config set maxinstances <number of storage account to create>__
```
