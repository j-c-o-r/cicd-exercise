# Overview

This source code is an exercise with the goal to deploy a flask app to predict housing prices in boston. The focus is on the ci/cd and not on the flask app itself, which was given as starter code.
This code will allow to deploy the webapp in Azure CloudShell and deploy the webapp as an azure service. The code contains a "github actions" workflow, but was also created a azure DevOps pipeline 

## Project Plan

* trelo board: https://trello.com/b/LSFC9HFg/building-a-ci-cd-pipeline
* project plan spreadsheet: https://github.com/j-c-o-r/cicd-exercise/blob/main/project-plan.xlsx

## Instructions


How to run the project:
1. Clone the project in Azure cloud shell:

_git clone git@github.com:j-c-o-r/cicd-exercise.git_

![image](https://user-images.githubusercontent.com/40064297/167175829-4b286b92-6e5d-4c42-b4e8-72c0fea7eb0c.png)

2. source the virtual environment:
source ~/cicd-exercise/bin/activate

3. run make all to run the Makefile steps
This will install all dependencies in the virtual environment

![image](https://user-images.githubusercontent.com/40064297/167176648-580adaca-9e34-4e96-a5f9-9078ef50d226.png)


4. start the application:
python app.py

5. do a prediction. 


<TODO:  
* Architectural Diagram (Shows how key parts of the system work)>

<TODO:  Instructions for running the Python project.  How could a user with no context run this project without asking you for any help.  Include screenshots with explicit steps to create that work. Be sure to at least include the following screenshots:

* Project running on Azure App Service


* Output of a test run

* Successful deploy of the project in Azure Pipelines.  [Note the official documentation should be referred to and double checked as you setup CI/CD](https://docs.microsoft.com/en-us/azure/devops/pipelines/ecosystems/python-webapp?view=azure-devops).

* Running Azure App Service from Azure Pipelines automatic deployment

* Successful prediction from deployed flask app in Azure Cloud Shell.  [Use this file as a template for the deployed prediction](https://github.com/udacity/nd082-Azure-Cloud-DevOps-Starter-Code/blob/master/C2-AgileDevelopmentwithAzure/project/starter_files/flask-sklearn/make_predict_azure_app.sh).
The output should look similar to this:

```bash
udacity@Azure:~$ ./make_predict_azure_app.sh
Port: 443
{"prediction":[20.35373177134412]}
```

* Output of streamed log files from deployed application

> 

## Enhancements

<TODO: A short description of how to improve the project in the future>

## Demo 

<TODO: Add link Screencast on YouTube>


