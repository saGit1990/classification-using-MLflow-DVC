# classification-using-MLflow-DVC

## Workflows

1. Update config.yaml
2. Update secrets.yaml [optional]
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline
8. Update the main.py
9. Update the dvc.yaml 


#### cmd
- mlflow ui

### dagshub
[dagshub](https://dagshub.com/)

MLFLOW_TRACKING_URI = "https://dagshub.com/saGit1990/classification-using-MLflow-DVC.mlflow"

MLFLOW_TRACKING_USERNAME = personal access token

python script.py

Run this to export as env variable:

```bash
export MLFLOW_TRACKING_URI = https://dagshub.com/saGit1990/classification-using-MLflow-DVC.mlflow
export MLFLOW_TRACKING_USERNAME = <token>
```