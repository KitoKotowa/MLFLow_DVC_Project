# MLFLow_DVC_Project

## Workflows
1. Update config.yaml
2. Update schema.yaml
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline
8. Update the main.py
9. Update the dvc.yaml
10. Update app.py


# How to run this?

### Clone the repository
```
https://github.com/KitoKotowa/MLFLow_DVC_Project
```
### Step 01: Create a conda environment after opening the repository

```
conda create -n mlproj python=3.11 -y
```

```
conda activate mlproj
```

### Step 02: Install dependencies
```
pip install -r requirements.txt
```

### [DagsHub](https://dagshub.com/)
```
MLFLOW_TRACKING_URI=https://dagshub.com/KitoKotowa/MLFLow_DVC_Project.mlflow
MLFLOW_TRACKING_USERNAME=KitoKotowa
MLFLOW_TRACKING_PASSWORD=1fd093cec2104e924b81fe3a1948271a308f19cb
python script.py
```
### Getting environment variable
- With bash/Linux terminal
```
export MLFLOW_TRACKING_URI=https://dagshub.com/KitoKotowa/MLFLow_DVC_Project.mlflow
export MLFLOW_TRACKING_USERNAME=KitoKotowa
export MLFLOW_TRACKING_PASSWORD=1fd093cec2104e924b81fe3a1948271a308f19cb
```
- With Windows Powershell
```
$env:MLFLOW_TRACKING_URI='https://dagshub.com/KitoKotowa/MLFLow_DVC_Project.mlflow'
$env:MLFLOW_TRACKING_USERNAME='KitoKotowa'
$env:MLFLOW_TRACKING_PASSWORD='1fd093cec2104e924b81fe3a1948271a308f19cb'
```

### Run the file
```
python main.py
```


