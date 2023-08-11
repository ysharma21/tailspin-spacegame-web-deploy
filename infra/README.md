#### A. To create an openai deployment from local dev terminal, run following

1. ```az login```

2. ```az deployment group create --resource-group <resource group name> --template-file arm_template.json```

Change the resource group name above

#### B. To create an openai deployment from ADO pipeline stage, see arm_templates.json in infra/ai and azure-pipelines.yml stage DeployOpenAI and 

checkout a successful run in https://dev.azure.com/yachnasharma0274/Space%20Game%20-%20web%20-%20Multistage/_build/results?buildId=79&view=results

TO DO: Replicate automated openai deployment in pipeline for PaaS copilot repo once permission issue is resolved.

#### Known Issues: Below error gets generated from pipeline in ADO
```ERROR: {"code": "InvalidTemplateDeployment", "message": "Deployment failed with multiple errors: 'Authorization failed for template resource 'ys-testB-openai' of type 'Microsoft.CognitiveServices/accounts'. The client '********02c' with object id '***
***02c' does not have permission to perform action 'Microsoft.CognitiveServices/accounts/write' at scope '/subscriptions/<subscriptionId/resourceGroups/rg-openai-dev/providers/Microsoft.CognitiveServices/accounts/ys-testB-openai'.:Authorization failed for template resource 'ys-testB-openai/ys-gpt-35-turbo' of type 'Microsoft.CognitiveServices/accounts/deployments'. The client '********02c' with object id '********02c' does not have permission to perform action 'Microsoft.CognitiveServices/accounts/deployments/write' at scope '/subscriptions/<subscriptionId>/resourceGroups/rg-openai-dev/providers/Microsoft.CognitiveServices/accounts/ys-testB-openai/deployments/ys-gpt-35-turbo'.'"}
##[error]Script failed with exit code: 1 ```

To mitigate use following from local command line [change the subscriptionId and resource group to relevant values]

```az role assignment create --assignee **********02c --role Contributor --scope /subscriptions/<subscriptionId>/resourceGroups/<resource group name>```