[![Python application test with Github Actions](https://github.com/j-c-o-r/cicd-exercise/actions/workflows/main.yml/badge.svg)](https://github.com/j-c-o-r/cicd-exercise/actions/workflows/main.yml)

# Overview

This source code is an exercise with the goal to deploy a flask app to predict housing prices in boston. The focus is on the ci/cd and not on the flask app itself, which was given as starter code.
This code will allow to deploy the webapp in Azure CloudShell and deploy the webapp as an azure service. The code contains a "github actions" workflow, but was also created a azure DevOps pipeline 

## Project Plan

* trelo board: https://trello.com/b/LSFC9HFg/building-a-ci-cd-pipeline
* project plan spreadsheet: https://github.com/j-c-o-r/cicd-exercise/blob/main/project-plan.xlsx
* link to demo video: https://youtu.be/vY2UKMiSpn8


## Architectural Diagram

![image](https://user-images.githubusercontent.com/40064297/167179700-41ec175c-6191-4087-9729-9fca72c201a0.png)

## Instructions


How to run the project:
1. Clone the project in Azure cloud shell:
```bash
git clone git@github.com:j-c-o-r/cicd-exercise.git 
```

![image](https://user-images.githubusercontent.com/40064297/167175829-4b286b92-6e5d-4c42-b4e8-72c0fea7eb0c.png)

2. source the virtual environment:

```bash
source ~/cicd-exercise/bin/activate
```

3. run ```make all``` to run the Makefile steps

This will install all dependencies in the virtual environment

![image](https://user-images.githubusercontent.com/40064297/167176648-580adaca-9e34-4e96-a5f9-9078ef50d226.png)


4. start the application:

```bash
python app.py
```

![image](https://user-images.githubusercontent.com/40064297/167180627-b5b40a52-5e5e-4dda-a16c-a879ec3b2442.png)


5. do a prediction: 

open a separate cloudShell while app.py is running, and run:

```bash
./make_prediction.sh
```

5.1 if prediction fails with permission denied, give permissions with chmod command:

```bash
chmod 777 ./make_prediction.sh
```

![image](https://user-images.githubusercontent.com/40064297/167180767-0d6276ef-2a9a-42bd-9d57-18d3d5f33bf3.png)







6.Deploy the project with Azure DevOps (oficial documentation [here](https://docs.microsoft.com/en-us/azure/devops/pipelines/ecosystems/python-webapp?view=azure-devops):
    a. Go to azure DevOps
    b. Run the pipeline to deploy the project 
![image](https://user-images.githubusercontent.com/40064297/167246719-2da1a30d-e06b-4fce-98b4-23b1883621b6.png)


7. access the newly created application through the browser:

![image](https://user-images.githubusercontent.com/40064297/167246782-89340018-2863-4ea3-9e29-b5b4d63e4154.png)

```bash
https://flask-exercise-service.azurewebsites.net/
```

9. do a prediction with 
```bash
./make_predict_azure_app.sh
```
once again, if needed, change the permission of that file with chmod

output:

![image](https://user-images.githubusercontent.com/40064297/167246980-05bacf4d-86a5-4042-ad6f-173fd20adc3d.png)

10. Checking the log files:
 ```bash
 az webapp log tail --name flask-exercise-service -g jcor_19_rg_0749
 ```
 
 ![image](https://user-images.githubusercontent.com/40064297/167247197-44361ee9-1d11-464a-bd6d-9ac9c8245d40.png)

## Enhancements

Enhancements can be done in two major directions: performance and stability. DevOps pipeline is taking a while to complete so an effort can be done to improve the deployment. 
On stability we can work on improving tests, since there are only a dew demo tests in place for the purpose of this demo

## Demo 

https://youtu.be/vY2UKMiSpn8

