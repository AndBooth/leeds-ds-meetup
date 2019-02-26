# Leeds Data Science
Repository for code and documents from Leeds Data Science meetup talk

# Productionise Python ML models with Azure Functions how-to guide

We can use Azure Functions to deploy a machine learning model that has been developed in Python as an API. Once the API is created we can ask the model to make predictions on new data by sending it a request.

I have found that the main difficulty in getting this to work lies in ensuring that the steps required to get everything set up have been followed correctly. The documentation to get it working does exist, but can be tricky to piece together. I have written this document with the intention of it being a guide that will allow anyone to get to the point where they have successfully created a machine learning API.

However, it is not intended as a guide to creating full production, enterprise ready software, so it should not be used with that intention.

## Sources

This how-to guide is a collated and abridged version of multiple sources, including Microsoft documentation and the Github repos of one of the developers of the Python Azure Functions worker. For further reading and information you can find these at the following links

- [Azure Functions Python developer guide](https://docs.microsoft.com/en-us/azure/azure-functions/functions-reference-python)
- [Create you first Python function in Azure](https://docs.microsoft.com/en-us/azure/azure-functions/functions-create-first-function-python#create-a-function)
- [Create your first function using Visual Studio Code](https://docs.microsoft.com/en-us/azure/azure-functions/functions-create-first-function-vs-code)
- [Asavari Tayal's github](https://github.com/asavaritayal?utf8=%E2%9C%93&tab=repositories&q=&type=&language=python)

# Prerequisites

To follow this guide you will need to have the following in place

**To create and test functions locally**
- Installation of Python 3.6
- Install [Azure Functions Core Tools](https://docs.microsoft.com/en-us/azure/azure-functions/functions-run-local#v2)
- Visual Studio Code IDE (you don't actually *need* this)*

**To deply to Azure**
- All of the above
- An active Azure subscription (free to create)
- Install the Azure [Command-line Interface](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli?view=azure-cli-latest)

\* You don't have to use Visual Studio Code but it has some tools that I find make the deployment process run a bit smoother

With these things in place we can now begin development of our Azure Function.

# Create and test a function locally

You can create, run and test a Python Azure Function locally without an Azure subscription, so you can carry out the majority of the process without the worry of incurring any costs. The instructions given here assume you are using the Visual Studio Code IDE.

## Install the Azure Functions extension in VS Code

The Azure Functions extension in VS Code provides some functionality that automates some of the tasks, such as creating an Azure Functions project and Azure Function templates.

<img src="https://github.com/AndBooth/leeds-ds-meetup/blob/master/Misc/Images/azurefunctionsextension.PNG" width="450" height="200">

Once installed we can get straight into creating our first locally deployed Azure Function. The first thing to do is to create an Azure Functions project.

<img src="https://github.com/AndBooth/leeds-ds-meetup/blob/master/Misc/Images/azurefunctionsextension.PNG" width="450" height="200">



